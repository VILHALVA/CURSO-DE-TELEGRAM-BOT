import utils.msgs as msgs
import random
import redis
import sqlite3
import subprocess
import telebot
from telebot import types

TOKEN = open('utils/token.conf', 'r').read().strip()

bot = telebot.TeleBot(TOKEN)

def get_emoji():
    emojis = random.sample(msgs.emoji_captcha, 4)
    return emojis

def create_buttons(chat_id):
    button = types.InlineKeyboardMarkup()
    emojis = get_emoji()
    possibilities = [chat_id, 'no', 'no', 'no']
    answer = random.sample(possibilities, k=len(possibilities))
    btn0 = types.InlineKeyboardButton(emojis[0].split(':')[0],
        callback_data=answer[0])
    btn1 = types.InlineKeyboardButton(emojis[1].split(':')[0],
        callback_data=answer[1])
    btn2 = types.InlineKeyboardButton(emojis[2].split(':')[0],
        callback_data=answer[2])
    btn3 = types.InlineKeyboardButton(emojis[3].split(':')[0],
        callback_data=answer[3])
    button.row(btn0, btn1)
    button.row(btn2, btn3)
    text = emojis[answer.index(chat_id)].split(':')[1]
    return button, text

def create_table(table):
    if table < 1: table = table*-1
    cursor = sqlite3.connect('RegrasRobot.db').cursor()
    aux = (f'''
        CREATE TABLE regras_{table} (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            chat_id TEXT NOT NULL,
            owner_id TEXT NOT NULL,
            rules_message_id TEXT
        )
    ''')
    cursor.execute(aux)
    sqlite3.connect('RegrasRobot.db').close()

def insert_on_table(table, values):
    table = int(table)
    if table < 1: table = table*-1
    conn = sqlite3.connect('RegrasRobot.db')
    cursor = conn.cursor()
    aux = (f'''
        INSERT INTO regras_{table} 
        (chat_id, owner_id, rules_message_id)
        VALUES ({values})
    ''')
    cursor.execute(aux)
    conn.commit()
    conn.close()

def select_from_table(table):
    table = int(table)
    if table < 1: table = table*-1
    conn = sqlite3.connect('RegrasRobot.db')
    cursor = conn.cursor()
    aux = f'SELECT * from regras_{table}'
    cursor.execute(aux)
    data = cursor.fetchone()
    conn.close()
    return data

def update_database(table, query): 
    table = int(table)
    if table < 1: table = table*-1
    conn = sqlite3.connect('RegrasRobot.db')
    cursor = conn.cursor()
    aux = f'UPDATE regras_{table} {query}'
    try:
        cursor.execute(aux)
    except sqlite3.OperationalError:
        create_table(table)
        cursor.execute(aux)
    conn.commit()
    conn.close()

@bot.chat_join_request_handler(func=lambda m:True)
def on_join(message):
    try:
        data = select_from_table(message.chat.id)
        buttons, answer = create_buttons(message.chat.id)
        bot.copy_message(message.from_user.id, data[2], data[3])
        msg = bot.send_message(message.from_user.id,
            msgs.choose_button.format(answer),
            reply_markup=buttons, parse_mode='HTML'
        )
        subprocess.Popen(
            ['python3', 'utils/auto_decline.py',
                str(message.chat.id),
                str(message.from_user.id),
                str(msg.id)
            ]
        )
    except Exception as e:
        print(e)


@bot.callback_query_handler(lambda q: q.data == 'no')
def refuse(query):
    try:
        bot.answer_callback_query(query.id,
            text=msgs.popup_deny, show_alert=True)
    except:
        pass
    try:
        bot.delete_message(query.from_user.id, query.message.id)
    except:
        pass
    try:
        bot.decline_chat_join_request(query.data, query.from_user.id)
    except:
        pass


@bot.callback_query_handler(func=lambda q:True)
def accept(query):
    button = types.InlineKeyboardMarkup()
    chat_id = query.data
    invite_link = bot.get_chat(chat_id).invite_link
    btn_group = types.InlineKeyboardButton(msgs.btn_group,
        url=f'{invite_link}')
    button.row(btn_group)
    try:
        bot.approve_chat_join_request(query.data, query.from_user.id)
        bot.answer_callback_query(query.id, text=msgs.popup_accept,
            show_alert=False)
        data = select_from_table(query.data)
        bot.send_message(query.from_user.id, msgs.popup_accept,
            reply_markup=button, parse_mode='HTML')
    except:
        pass
    try:
        bot.delete_message(query.from_user.id, query.message.id)
    except:
        pass

@bot.message_handler(content_types=[
    'chat_join_request', 
    'left_chat_member', 
    'new_chat_members'
])
def member_joined(message):
    try:
        bot.delete_message(message.chat.id, message.message_id)
    except telebot.apihelper.ApiTelegramException:
        pass
    if (
            message.new_chat_members and 
            message.new_chat_members[0].username == 'RegrasRobot'
    ):
        bot.set_my_commands([
            telebot.types.BotCommand('set_here', 'Configurar RegrasRobot')
        ], scope=types.BotCommandScopeChat(message.chat.id))
        bot.send_message(message.chat.id, msgs.set_rules, parse_mode='HTML')

@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id < 0:
        return
    bot.set_my_commands([
        telebot.types.BotCommand('start', 'Informações'),
        telebot.types.BotCommand('pix', 'Faça uma doação')
    ], scope=types.BotCommandScopeChat(f'{message.from_user.id}'))
    if ' ' in message.text:
        data = select_from_table(message.text.replace('/start ', ''))
        try:
            bot.copy_message(message.from_user.id, data[2], data[3])
        except:
            button = types.InlineKeyboardMarkup()
            btn = types.InlineKeyboardButton(msgs.btn_rules,
                url=f'https://t.me/RegrasRobot?start={message.chat.id}')
            button.row(btn)
            bot.send_message(message.chat.id,
                msgs.click_rules.format(message.from_user.id),
                parse_mode='HTML', reply_markup=button
            )
    else:
        bot.send_chat_action(message.chat.id, 'typing')
        button = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton(msgs.btn_blog,
            url=f'https://blog.gabrf.com/posts/RegrasRobot/')
        button.row(btn)
        bot.send_message(message.from_user.id,
            msgs.start.format(message.from_user.first_name),
            parse_mode='HTML', reply_markup=button
        )

@bot.message_handler(commands=['set_here', 'set_rules'])
def set_here(message):
    if message.chat.type == 'private':
        bot.send_message(message.from_user.id, 
            msgs.start.format(message.from_user.first_name),
            parse_mode='HTML'
        )
    elif message.chat.type != 'supergroup':
        bot.send_message(
            message.chat.id, msgs.not_supergroup, parse_mode='HTML'
        )
        return
    if message.chat.id > 0: return
    bot_admin = False
    bot_started = False
    if bot.get_chat_member(
            message.chat.id, 
            message.from_user.id
        ).status == 'creator':
        try:
            bot.send_chat_action(message.from_user.id, 'typing')
            bot_started = True
        except telebot.apihelper.ApiTelegramException:
            name = message.from_user.username
            if not name:
                name = f'''{message.from_user.first_name}
                    {message.from_user.last_name}'''
            bot.reply_to(message,
                msgs.not_started.format(message.from_user.id,
                name), parse_mode='HTML'
            )
        try:
            bot.delete_message(message.chat.id, message.id)
            bot_admin = True
        except telebot.apihelper.ApiTelegramException:
            bot.reply_to(message, msgs.not_admin, parse_mode='HTML')
            pass
    if bot_admin and bot_started:
        bot.delete_my_commands(
            scope=types.BotCommandScopeChat(message.chat.id)
        )
        try:
            create_table(message.chat.id)
        except sqlite3.OperationalError:
            pass
        r = redis.Redis(host='localhost', port=6379, db=0)
        r.set(message.from_user.id, int(message.chat.id)*-1)
        bot.send_message(message.from_user.id, msgs.send_rules,
            parse_mode='HTML')

@bot.message_handler(commands=['rules', 'regras'])
def send_rules(message):
    if message.chat.id > 0: return
    try:
        data = select_from_table(message.chat.id)
    except:
        pass
    try:
        bot.copy_message(message.from_user.id, data[2], data[3])
    except:
        button = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton(msgs.btn_rules,
            url=f'https://t.me/RegrasRobot?start={message.chat.id}')
        button.row(btn)
        msg = bot.send_message(message.chat.id,
            msgs.click_rules.format(message.from_user.id),
            parse_mode='HTML', reply_markup=button,
            reply_to_message_id=message.id
        )
        subprocess.Popen([
            'python3',
            'utils/erase_msg.py',
            str(message.chat.id),
            str(msg.id)
        ])
    try:
        bot.delete_message(message.chat.id, message.id)
        data = select_from_table(message.chat.id)
    except:
        return


@bot.message_handler(commands=['pix'])
def send_rules(message):
    if message.chat.id < 0:
        return
    else:
        bot.send_photo(message.chat.id,
            msgs.donate_qrcode,
            caption=msgs.donate_caption,
            parse_mode='HTML'
        )

@bot.message_handler(content_types=['document', 'photo', 'animation'])
@bot.message_handler(func=lambda m: True)
def message_to_bot(message):
    if message.chat.id < 0:
        return
    bot.set_my_commands([
        telebot.types.BotCommand('start', 'Informações'),
        telebot.types.BotCommand('pix', 'Faça uma doação')
    ], scope=types.BotCommandScopeChat(f'{message.from_user.id}'))
    bot.send_chat_action(message.chat.id, 'typing')
    r = redis.Redis(host='localhost', port=6379, db=0)
    chat_id = r.get(message.from_user.id)
    if not chat_id:
        bot.reply_to(
            message, msgs.start.format(message.from_user.first_name),
            parse_mode='HTML')
    else:
        chat_id = chat_id.decode('utf-8')
        if not select_from_table(chat_id):
            values = f'"{chat_id}", "{message.from_user.id}", "{message.id}"'
            insert_on_table(chat_id, values)
        else:
            query = f'''SET rules_message_id = {message.id} 
                WHERE chat_id = {chat_id}'''
            update_database(chat_id, query)
        r.delete(message.from_user.id)
        bot.reply_to(message, msgs.saved_rules, parse_mode='HTML')
        bot.set_my_commands([
            telebot.types.BotCommand('regras', 'Regras do grupo')
        ], scope=types.BotCommandScopeChat(f'-{chat_id}'))

if __name__ == "__main__":
    bot.polling(allowed_updates=[
        'chat_join_request', 
        'chat_member', 
        'message', 
        'callback_query',
        'inline_query',
        'chat_member',
    ])
