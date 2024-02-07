local api = require 'methods'
local redis = require 'redis'
local clr = require 'term.colors'
local u, config, plugins, last_update, last_cron
db = redis.connect('127.0.0.1', 6379)

function bot_init(on_reload) -- The function run when the bot is started or reloaded.

	config = dofile('config.lua') -- Load configuration file.
	assert(not (config.Token == "" or not config.Token), clr.red..'Insert the bot token in config.lua -> Token'..clr.reset)
	assert(#config.superadmins > 0, clr.red..'Insert your Telegram ID in config.lua -> superadmins'..clr.reset)
	assert(config.log.admin, clr.red..'Insert your Telegram ID in config.lua -> log.admin'..clr.reset)

	db:select(config.db or 0) --select the redis db

	u = dofile('utilities.lua') -- Load miscellaneous and cross-plugin functions.
	locale = dofile('languages.lua')
	now_ms = require('socket').gettime

	bot = api.getMe().result -- Get bot info
	bot.revision = u.bash('git rev-parse --short HEAD')

	plugins = {} -- Load plugins.
	for i,v in ipairs(config.plugins) do
		local p = require('plugins.'..v)
		package.loaded['plugins.'..v] = nil
		if p.triggers then
			for funct, trgs in pairs(p.triggers) do
				for i = 1, #trgs do
					-- interpret any whitespace character in commands just as space
					trgs[i] = trgs[i]:gsub(' ', '%%s+')
				end
				if not p[funct] then
					p.trgs[funct] = nil
					print(clr.red..funct..' triggers ignored in '..v..': '..funct..' function not defined'..clr.reset)
				end
			end
		end
		table.insert(plugins, p)
	end

	print('\n'..clr.blue..'BOT RUNNING:'..clr.reset, clr.red..'[@'..bot.username .. '] [' .. bot.first_name ..'] ['..bot.id..']'..clr.reset, clr.green..'\nAt '.. os.date("%A, %d of %B in %Y at %X")..clr.reset)

	last_update = last_update or -2 -- Set loop variables: Update offset
	last_cron = last_cron or os.time() -- the time of the last cron job

	if on_reload then
		return #plugins
	else
		api.sendAdmin(_("*Bot *@%s* started!*\n_%s_\n%d plugins loaded"):format(bot.username:escape(), os.date('!%c UTC'), #plugins), true)
		start_timestamp = os.time()
		current = {h = 0}
		last = {h = 0}
	end
end

local function extract_usernames(msg)
	if msg.from then
		if msg.from.username then
			db:hset('bot:usernames', '@'..msg.from.username:lower(), msg.from.id)
		end
		db:sadd(string.format('chat:%d:members', msg.chat.id), msg.from.id)
	end
	if msg.forward_from and msg.forward_from.username then
		db:hset('bot:usernames', '@'..msg.forward_from.username:lower(), msg.forward_from.id)
	end
	if msg.new_chat_member then
		if msg.new_chat_member.username then
			db:hset('bot:usernames', '@'..msg.new_chat_member.username:lower(), msg.new_chat_member.id)
		end
		db:sadd(string.format('chat:%d:members', msg.chat.id), msg.new_chat_member.id)
	end
	if msg.left_chat_member then
		if msg.left_chat_member.username then
			db:hset('bot:usernames', '@'..msg.left_chat_member.username:lower(), msg.left_chat_member.id)
		end
		db:srem(string.format('chat:%d:members', msg.chat.id), msg.left_chat_member.id)
	end
	if msg.reply_to_message then
		extract_usernames(msg.reply_to_message)
	end
	if msg.pinned_message then
		extract_usernames(msg.pinned_message)
	end
end

local function collect_stats(msg)

	extract_usernames(msg)

	if msg.chat.type ~= 'private' and msg.chat.type ~= 'inline' and msg.from then
		db:hset('chat:'..msg.chat.id..':userlast', msg.from.id, os.time()) --last message for each user
		db:hset('bot:chats:latsmsg', msg.chat.id, os.time()) --last message in the group
	end
end

local function match_triggers(triggers, text)
  	if text and triggers then
		text = text:gsub('^(/[%w_]+)@'..bot.username, '%1')
		for i, trigger in pairs(triggers) do
			local matches = {}
	    	matches = { string.match(text, trigger) }
			if next(matches) then
	    		return matches, trigger
			end
		end
	end
end

local function on_msg_receive(msg, callback) -- The fn run whenever a message is received.
	--u.dump('PARSED', msg)
	if not msg then
		return
	end

	if msg.chat.type ~= 'group' then --do not process messages from normal groups

		if msg.date < os.time() - 7 then print('Old update skipped') return end -- Do not process old messages.
		if not msg.text then msg.text = msg.caption or '' end
		
		locale.language = db:get('lang:'..msg.chat.id) or config.lang --group language
		if not config.available_languages[locale.language] then
			locale.language = config.lang
		end

		collect_stats(msg)

		local continue = true
		local onm_success
		for i, plugin in pairs(plugins) do
			if plugin.onEveryMessage then
				onm_success, continue = pcall(plugin.onEveryMessage, msg)
				if not onm_success then
					api.sendAdmin('An #error occurred (preprocess).\n'..tostring(continue)..'\n'..locale.language..'\n'..msg.text)
				end
			end
			if not continue then return end
		end

		for i,plugin in pairs(plugins) do
			if plugin.triggers then
				local blocks, trigger = match_triggers(plugin.triggers[callback], msg.text)
				if blocks then

					if msg.chat.type ~= 'private' and msg.chat.type ~= 'inline'and not db:exists('chat:'..msg.chat.id..':settings') and not msg.service then --init agroup if the bot wasn't aware to be in
							u.initGroup(msg.chat.id)
						end

					if config.bot_settings.stream_commands then --print some info in the terminal
						print(clr.reset..clr.blue..'['..os.date('%X')..']'..clr.red..' '..trigger..clr.reset..' '..msg.from.first_name..' ['..msg.from.id..'] -> ['..msg.chat.id..']')
					end

					--if not check_callback(msg, callback) then goto searchaction end
					local success, result = xpcall(plugin[callback], debug.traceback, msg, blocks) --execute the main function of the plugin triggered

					if not success then --if a bug happens
							print(result)
							if config.bot_settings.notify_bug then
								api.sendReply(msg, _("🐞 Sorry, a *bug* occurred"), true)
							end
    	      				api.sendAdmin('An #error occurred.\n'..result..'\n'..locale.language..'\n'..msg.text)
							return
						end

					if type(result) == 'string' then --if the action returns a string, make that string the new msg.text
						msg.text = result
					elseif not result then --if the action returns true, then don't stop the loop of the plugin's actions
						return
					end
				end

			end
		end
	else
		if msg.group_chat_created or (msg.new_chat_member and msg.new_chat_member.id == bot.id) then
			-- set the language
			--[[locale.language = db:get(string.format('lang:%d', msg.from.id)) or 'en'
			if not config.available_languages[locale.language] then
				locale.language = 'en'
			end]]

			-- send disclamer
			api.sendMessage(msg.chat.id, _([[
Hello everyone!
My name is %s, and I'm a bot made to help administrators in their hard work.
Unfortunately I can't work in normal groups, please ask the creator to convert this group to a supergroup.
]]):format(bot.first_name))

			-- log this event
			if config.bot_settings.stream_commands then
				print(string.format('%s[%s]%s Bot was added to a normal group %s%s [%d] -> [%d]',
					  clr.blue, os.date('%X'), clr.yellow, clr.reset, msg.from.first_name, msg.from.id, msg.chat.id))
			end
		end
	end
end

local function parseMessageFunction(update)

	db:hincrby('bot:general', 'messages', 1)

	local msg, function_key

	--if update.message or update.edited_message or update.channel_post or update.edited_channel_post then
	if update.message or update.edited_message then

		function_key = 'onTextMessage'

		--if not update.message then
			if update.edited_message then
				update.edited_message.edited = true
				update.edited_message.original_date = update.edited_message.date
				update.edited_message.date = update.edited_message.edit_date
				function_key = 'onEditedMessage'
			--[[elseif update.channel_post then
				update.channel_post.channel_post = true
				function_key = 'onChannelPost'
			elseif update.edited_channel_post then
				update.edited_channel_post.edited_channel_post = true
				update.edited_channel_post.original_date = update.edited_channel_post.date
				update.edited_channel_post.date = update.edited_channel_post.edit_date
				function_key = 'onEditedChannelPost']]
			end
		--end

		--msg = update.message or update.edited_message or update.channel_post or update.edited_channel_post
		msg = update.message or update.edited_message

		if msg.text then
		elseif msg.photo then
			msg.media = true
			msg.media_type = 'photo'
		elseif msg.audio then
			msg.media = true
			msg.media_type = 'audio'
		elseif msg.document then
			msg.media = true
			msg.media_type = 'document'
			if msg.document.mime_type == 'video/mp4' then
				msg.media_type = 'gif'
			end
		elseif msg.sticker then
			msg.media = true
			msg.media_type = 'sticker'
		elseif msg.video then
			msg.media = true
			msg.media_type = 'video'
		elseif msg.voice then
			msg.media = true
			msg.media_type = 'voice'
		elseif msg.contact then
			msg.media = true
			msg.media_type = 'contact'
		elseif msg.venue then
			msg.media = true
			msg.media_type = 'venue'
		elseif msg.location then
			msg.media = true
			msg.media_type = 'location'
		elseif msg.game then
			msg.media = true
			msg.media_type = 'game'
		elseif msg.left_chat_member then
			msg.service = true
			if msg.left_chat_member.id == bot.id then
				msg.text = '###left_chat_member:bot'
			else
				msg.text = '###left_chat_member'
			end
		elseif msg.new_chat_member then
			msg.service = true
			if msg.new_chat_member.id == bot.id then
				msg.text = '###new_chat_member:bot'
			else
				msg.text = '###new_chat_member'
			end
		elseif msg.new_chat_photo then
			msg.service = true
			msg.text = '###new_chat_photo'
		elseif msg.delete_chat_photo then
			msg.service = true
			msg.text = '###delete_chat_photo'
		elseif msg.group_chat_created then
    		msg.service = true
    		msg.text = '###group_chat_created'
		elseif msg.supergroup_chat_created then
			msg.service = true
			msg.text = '###supergroup_chat_created'
		elseif msg.channel_chat_created then
			msg.service = true
			msg.text = '###channel_chat_created'
		elseif msg.migrate_to_chat_id then
			msg.service = true
			msg.text = '###migrate_to_chat_id'
		elseif msg.migrate_from_chat_id then
			msg.service = true
			msg.text = '###migrate_from_chat_id'
		elseif msg.new_chat_title then
			msg.service = true
			msg.text = '###new_chat_title'
		elseif msg.pinned_message then
			msg.service = true
			msg.text = '###pinned_message'
		else
			--callback = 'onUnknownType'
			print('Unknown update type') return
		end

		if msg.forward_from_chat then
			if msg.forward_from_chat.type == 'channel' then
				msg.spam = 'forwards'
			end
		end
		if msg.caption then
			local caption_lower = msg.caption:lower()
			if caption_lower:match('telegram%.me') or caption_lower:match('telegram%.dog') or caption_lower:match('t%.me') then
				msg.spam = 'links'
			end
		end
		if msg.entities then
			for i, entity in pairs(msg.entities) do
				if entity.type == 'text_mention' then
					msg.mention_id = entity.user.id
				end
				if entity.type == 'url' or entity.type == 'text_link' then
					local text_lower = msg.text or msg.caption
					text_lower = entity.url and text_lower..entity.url or text_lower
					text_lower = text_lower:lower()
					if text_lower:match('telegram%.me') or
						text_lower:match('telegram%.dog') or
					--	text_lower:match('') or
						text_lower:match('https://') or
						text_lower:match('http://') or					
						text_lower:match('t.ne/') or								
						text_lower:match('t%.me') then
						msg.spam = 'links'
					else
						msg.media_type = 'link'
						msg.media = true
					end
				end
			end
		end
-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
		-- inicio anti-whatsapp
		if msg.caption then
			local caption_lower = msg.caption:lower()
			if caption_lower:match('whatsapp%.com') or caption_lower:match('chat%.whatsapp%.com') then
				msg.spam = 'linkswp'
			end
		end
		if msg.entities then
			for i, entity in pairs(msg.entities) do
				if entity.type == 'text_mention' then
					msg.mention_id = entity.user.id
				end
				if entity.type == 'url' or entity.type == 'text_link' then
					local text_lower = msg.text or msg.caption
					text_lower = entity.url and text_lower..entity.url or text_lower
					text_lower = text_lower:lower()
					if text_lower:match('whatsapp%.com') or
						text_lower:match('chat%.whatsapp%.com') then
						msg.spam = 'linkswp'
					else
						msg.media_type = 'link'
						msg.media = true
					end
				end
			end
		end
		-- fim anti-whatapp
		-- inicio antiofensa
		if msg.caption then
			local caption_lower = msg.caption:lower()
			if caption_lower:match('vaca') or caption_lower:match('vagabunda') or caption_lower:match('seu arrombado') or caption_lower:match('sua cachorra') or caption_lower:match('sua vadia') or caption_lower:match('imunda') or caption_lower:match('vadia') or caption_lower:match('caralho') or caption_lower:match('filho da puta') or caption_lower:match('vai tomar no cu') or caption_lower:match('arrombado') or caption_lower:match('viado') or caption_lower:match('corno') or caption_lower:match('desgraçado') or caption_lower:match('fi de uma égua') or caption_lower:match('fi de rapariga') or caption_lower:match('baitola') or caption_lower:match('bicha') or caption_lower:match('caralho') or caption_lower:match('porra') or caption_lower:match('porra') or caption_lower:match('merda') or caption_lower:match('bosta') or caption_lower:match('resto de aborto') or caption_lower:match('vai pro inferno') or caption_lower:match('desgraçada') or caption_lower:match('pau no seu cu') or caption_lower:match('buceta') or caption_lower:match('abestado') or caption_lower:match('filha de macaco') or caption_lower:match('filho de um macaco') or caption_lower:match('seu macaco') or caption_lower:match('seu macaco') or caption_lower:match('sua vaca') or caption_lower:match('rapariga') or caption_lower:match('seu estrume') or caption_lower:match('seu inútil') or caption_lower:match('seu miserável') or caption_lower:match('seu bactéria') or caption_lower:match('seu abusado pelo pai') or caption_lower:match('seu doador de cu') or caption_lower:match('sua galinha') or caption_lower:match('seu mutante') or caption_lower:match('seu traveco') or caption_lower:match('vc é uma vadia') or caption_lower:match('seu otario') or caption_lower:match('sua galinha') or caption_lower:match('sua galinha do caralho') or caption_lower:match('vou comer seu cu') or caption_lower:match('comer seu cu') or caption_lower:match('seu mendigo') or caption_lower:match('seu imundo') or caption_lower:match('seu fraco') or caption_lower:match('seu viadinho') or caption_lower:match('lixo é seu cu') or caption_lower:match('seu lixo') or caption_lower:match('seu cu') or caption_lower:match('seu cú') or caption_lower:match('puta da sua mãe') or caption_lower:match('sua puta') or caption_lower:match('nasceu de uma cagada') or caption_lower:match('calada vadia') or caption_lower:match('seu toba') or caption_lower:match('seu hermafrodita') or caption_lower:match('sua hermafrodita') or caption_lower:match('drogado do caralho') or caption_lower:match('resto de aborto') or caption_lower:match('seu fedido') or caption_lower:match('aborto mal sucedido') then
				msg.spam = 'antipo'
			end
		end
	if msg.text then
			local text_lower = msg.text:lower()
	if msg.text == text_lower:match('bot lixo') or text_lower:match('vaca') or text_lower:match('xingar esses lixo') or text_lower:match('esses lixos') or text_lower:match('seu arrombado') or text_lower:match('sua cachorra') or text_lower:match('sua vadia') or text_lower:match('vagabunda') or text_lower:match('imunda') or text_lower:match('vadia') or text_lower:match('caralho') or text_lower:match('filho da puta') or text_lower:match('vai tomar no cu') or text_lower:match('arrombado') or text_lower:match('viado') or text_lower:match('corno') or text_lower:match('desgraçado') or text_lower:match('fi de uma égua') or text_lower:match('fi de rapariga') or text_lower:match('baitola') or text_lower:match('bicha') or text_lower:match('caralho') or text_lower:match('porra') or text_lower:match('porra') or text_lower:match('merda') or text_lower:match('bosta') or text_lower:match('resto de aborto') or text_lower:match('vai pro inferno') or text_lower:match('desgraçada') or text_lower:match('pau no seu cu') or text_lower:match('buceta') or text_lower:match('abestado') or text_lower:match('filha de macaco') or text_lower:match('filho de um macaco') or text_lower:match('seu macaco') or text_lower:match('seu macaco') or text_lower:match('sua vaca') or text_lower:match('rapariga') or text_lower:match('seu estrume') or text_lower:match('seu inútil') or text_lower:match('seu miserável') or text_lower:match('seu bactéria') or text_lower:match('seu abusado pelo pai') or text_lower:match('seu doador de cu') or text_lower:match('sua galinha') or text_lower:match('seu mutante') or text_lower:match('seu traveco') or text_lower:match('vc é uma vadia') or text_lower:match('seu otario') or text_lower:match('sua galinha') or text_lower:match('sua galinha do caralho') or text_lower:match('vou comer seu cu') or text_lower:match('comer seu cu') or text_lower:match('seu mendigo') or text_lower:match('seu imundo') or text_lower:match('seu fraco') or text_lower:match('seu viadinho') or text_lower:match('lixo é seu cu') or text_lower:match('seu lixo') or text_lower:match('seu cu') or text_lower:match('seu cú') or text_lower:match('puta da sua mãe') or text_lower:match('sua puta') or text_lower:match('nasceu de uma cagada') or text_lower:match('calada vadia') or text_lower:match('seu toba') or text_lower:match('seu hermafrodita') or text_lower:match('sua hermafrodita') or text_lower:match('drogado do caralho') or text_lower:match('resto de aborto') or text_lower:match('seu fedido') or text_lower:match('aborto mal sucedido') then
 	 msg.spam = 'antipo'
		end
	end
	if msg.text then
	local msg_text = string.lower(msg.text) 
	if msg_text == string.find(msg.text, 'caralho ') or string.find(msg.text, 'cú ') or string.find(msg.text, 'cu ') or string.find(msg.text, 'porra ') or string.find(msg.text, 'puta que pariu ') or string.find(msg.text, 'filho da puta ') or string.find(msg.text, 'merda ') or string.find(msg.text, 'vai tomar no cu ') or string.find(msg.text, 'vai se foder ') or string.find(msg.text, 'viado ') or string.find(msg.text, 'puta merda ') or string.find(msg.text, 'cacete ') or string.find(msg.text, 'boceta ') or string.find(msg.text, 'puta ') then
	msg.spam = 'antipo'
	if msg_text == string.find(msg.text, ' caralho') or string.find(msg.text, ' cú') or string.find(msg.text, ' cu', string.len(msg.text)-2) or string.find(msg.text, ' porra') or string.find(msg.text, ' puta que pariu') or string.find(msg.text, ' filho da puta') or string.find(msg.text, ' merda') or string.find(msg.text, ' vai tomar no cu') or string.find(msg.text, ' vai se foder') or string.find(msg.text, ' viado') or string.find(msg.text, ' puta merda') or string.find(msg.text, ' cacete') or string.find(msg.text, ' boceta') or string.find(msg.text, ' puta') then
  msg.spam = 'antipo'
	if msg_text == string.find(msg.text, ' caralho ') or string.find(msg.text, 'cú ') or string.find(msg.text, 'cu ') or string.find(msg.text, ' porra ') or string.find(msg.text, ' puta que pariu ') or string.find(msg.text, ' filho da puta ') or string.find(msg.text, ' merda ') or string.find(msg.text, ' vai tomar no cu ') or string.find(msg.text, ' vai se foder ') or string.find(msg.text, ' viado ') or string.find(msg.text, ' puta merda ') or string.find(msg.text, ' cacete ') or string.find(msg.text, ' boceta ') or string.find(msg.text, ' puta ') then
	msg.spam = 'antipo'
	end
	end
	end
	end
    -- fim antiofensa
	-- INICIO anti-Username
	if msg.text then
	local msg_text = string.lower(msg.text) 
	local text_lower = msg.text:lower()
	if msg.text == text_lower:match('(@[%w_]+)$') or text_lower:match('(@[%w_]+)$') or text_lower:match('(@[%w_]+)$') or text_lower:match('^(@[%w_]+)@$') then
				msg.spam = 'antiuser'
	elseif msg.text == text_lower:match('(@[%w_]*) (.*)$') or text_lower:match('(@[%w_]*) (.*)$') then
				msg.spam = false
	end		
end
if msg.text then
	local msg_text = string.lower(msg.text)
	if msg_text == string.find(msg_text,'([%w_]*)@' .. ' ') then
				print(msg_text)
				msg.spam = false
	elseif msg_text == string.find(msg_text,'@') 
		or string.find(msg_text,'(@[%w_]*)@') then
				print(msg_text)
				msg.spam = 'antiuser'
	
		end
	end
		-- fim anti-Username	
-- Inicio Anti-comandos
	if msg.text then
	local msg_text = string.lower(msg.text) 
	local text_lower = msg.text:lower()
	if msg.text == text_lower:match('naoersaasasasaewcasqwr') or text_lower:match('^(/[%w_]+)$') or text_lower:match('^(#[%w_]+)$') or text_lower:match('^(![%w_]+)$') or text_lower:match('^(![%w_]+)@$') then
				msg.spam = 'antico'
	elseif msg.text == text_lower:match('naoersaasasasaewcasqwr') or text_lower:match('(/[%w_]*) (.*)$') or text_lower:match('(#[%w_]*) (.*)$') or text_lower:match('(![%w_]*) (.*)$') then
				msg.spam = false
	end		
end
if msg.text then
	local msg_text = string.lower(msg.text)
	if msg_text == string.find(msg_text,'naoersaasasasaewcasqwr') or string.find(msg_text,'(/[%w_]*)@' .. ' ') then
				print(msg_text)
				msg.spam = false
	elseif msg_text == string.find(msg_text,'naoersaasasasaewcasqwr') or string.find(msg_text,'(/[%w_]*)@') then
				print(msg_text)
				msg.spam = 'antico'
	
		end
end
-- fim anti-comandos
-- inicio conteúdo sujo
		if msg.caption then
			local caption_lower = msg.caption:lower()
			if caption_lower:match('netfree') or caption_lower:match('netfree') or caption_lower:match('net free') or caption_lower:match('arquivo claro') or caption_lower:match('arquivo tim') or caption_lower:match('arquivo vivo') or caption_lower:match('arquivo oi') or caption_lower:match('netflix gratis') or caption_lower:match('netflix grátis') or caption_lower:match('ehi') or caption_lower:match('playload') or caption_lower:match('playload vivo') or caption_lower:match('playload tim') or caption_lower:match('playload claro') or caption_lower:match('playload oi')  or caption_lower:match('cc full') or caption_lower:match('as melhores ehi') or caption_lower:match('eproxy') or caption_lower:match('host da oi') or caption_lower:match('arquivo 30 dias') or caption_lower:match('arquivo vps 30 dias') or caption_lower:match('ehis') or caption_lower:match('infocc') or caption_lower:match('ccfull') or caption_lower:match('tela fake') or caption_lower:match('cadsus') or caption_lower:match('info cc') then
				msg.spam = 'anticsujos'
			end
		end
	if msg.text then
			local text_lower = msg.text:lower()
	if msg.text == text_lower:match('netfree') or text_lower:match('netfree') or text_lower:match('net free') or text_lower:match('arquivo claro') or text_lower:match('arquivo tim') or text_lower:match('arquivo vivo') or text_lower:match('arquivo oi') or text_lower:match('netflix gratis') or text_lower:match('netflix grátis') or text_lower:match('ehi') or text_lower:match('playload') or text_lower:match('playload vivo') or text_lower:match('playload tim') or text_lower:match('playload claro') or text_lower:match('playload oi')  or text_lower:match('cc full') or text_lower:match('as melhores ehi') or text_lower:match('eproxy') or text_lower:match('host da oi') or text_lower:match('arquivo 30 dias') or text_lower:match('arquivo vps 30 dias') or text_lower:match('ehis') or text_lower:match('infocc') or text_lower:match('ccfull') or text_lower:match('tela fake') or text_lower:match('cadsus') or text_lower:match('info cc') then 
				msg.spam = 'anticsujos'
		end
	end
-- inicio conteúdo sujo

--%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

		if msg.reply_to_message then
			msg.reply = msg.reply_to_message
			if msg.reply.caption then
				msg.reply.text = msg.reply.caption
			end
		end
	elseif update.inline_query then
		msg = update.inline_query
		msg.inline = true
		msg.chat = {id = msg.from.id, type = 'inline', title = 'inline'}
		msg.date = os.time()
		msg.text = '###inline:'..msg.query
		function_key = 'onInlineQuery'
	elseif update.chosen_inline_result then
		msg = update.chosen_inline_result
		msg.text = '###chosenresult:'..msg.query
		msg.chat = {type = 'inline', id = msg.from.id, title = msg.from.first_name}
		msg.message_id = msg.inline_message_id
		msg.date = os.time()
		function_key = 'onChosenInlineQuery'
	elseif update.callback_query then
		msg = update.callback_query
		msg.cb = true
		msg.text = '###cb:'..msg.data
		if msg.message then
			msg.original_text = msg.message.text
			msg.original_date = msg.message.date
			msg.message_id = msg.message.message_id
			msg.chat = msg.message.chat
		else --when the inline keyboard is sent via the inline mode
			msg.chat = {type = 'inline', id = msg.from.id, title = msg.from.first_name}
			msg.message_id = msg.inline_message_id
		end
		msg.date = os.time()
		msg.cb_id = msg.id
		msg.message = nil
		msg.target_id = msg.data:match('(-%d+)$') --callback datas often ship IDs
		function_key = 'onCallbackQuery'
	else
		--function_key = 'onUnknownType'
		print('Unknown update type') return
	end

	if (msg.chat.id < 0 or msg.target_id) and msg.from then
		msg.from.admin = u.is_admin(msg.target_id or msg.chat.id, msg.from.id)
		if msg.from.admin then
			msg.from.mod = true
		else
			msg.from.mod = u.is_mod(msg.target_id or msg.chat.id, msg.from.id)
		end
	end

	--print('Mod:', msg.from.mod, 'Admin:', msg.from.admin)
	return on_msg_receive(msg, function_key)
end

bot_init() -- Actually start the script. Run the bot_init function.

api.firstUpdate()
while true do -- Start a loop while the bot should be running.
	local res = api.getUpdates(last_update+1) -- Get the latest updates
	if res then
		clocktime_last_update = os.clock()
		for i, msg in ipairs(res.result) do -- Go through every new message.
			last_update = msg.update_id
			--print(last_update)
			current.h = current.h + 1
			parseMessageFunction(msg)
		end
	else
		print('Connection error')
	end
	if last_cron ~= os.date('%M') then -- Run cron jobs every minute.
		last_cron = os.date('%M')
		last.h = current.h
		current.h = 0
		for i,v in ipairs(plugins) do
			if v.cron then -- Call each plugin's cron function, if it has one.
				local res, err = xpcall(v.cron, debug.traceback)
				if not res then
					print(err)
          			api.sendLog('An #error occurred (cron).\n'..err)
					return
				end
			end
		end
	end
end

print('Halted.\n')
