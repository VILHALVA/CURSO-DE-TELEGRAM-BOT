import gdown
import sqlite3
import logging
import os.path
import pafy, requests
import youtube_dl
import moviepy.editor as mp
import os, subprocess, time
from os import remove
from logg import add_data_log
from subprocess import check_output
from colorama import Fore, Style, init
from telegram import MessageEntity, Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
init()

###########################################################################
##codigo de bypass error para seguir el flujo y agrupar funciones iguales##
##########y funcion validadora de las url para todas las down##############
###########################################################################

def create_db():
	ruta = os.getcwd() + "\\db\\"
	conn = sqlite3.connect(ruta+'log_telegram_download.sqlite')
	cur = conn.cursor()
	try:
		cur.execute('CREATE TABLE Registro (key_bot INTEGER PRIMARY KEY AUTOINCREMENT, id VARCHAR(30) NOT NULL, link VARCHAR(60) NOT NULL, time_s TEXT, title VARCHAR(90), tipo VARCHAR(20) NOT NULL, username VARCHAR(45) NOT NULL, firstname VARCHAR(45) NOT NULL, is_bot VARCHAR(10), lenguaje VARCHAR(10));')
	except Exception as e:
		print(Fore.RED,e,Fore.RESET)
	conn.close()
	pass

def add_db(chunk):
	ruta = os.getcwd() + "\\db\\"
	conn = sqlite3.connect(ruta+'log_telegram_download.sqlite')
	cur = conn.cursor()
	cur.execute('INSERT INTO Registro ( id, link, time_s, title, tipo, username, firstname, is_bot, lenguaje) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?)',(chunk))
	conn.commit()
	pass

def clean(file_del):
	if os.path.exists(file_del):
		remove(file_del)
	else:
		print(Fore.RED+"# - Archivo Dont Remove Why Not Exists "+Fore.RESET,file_del)
	pass

def start(update, context):
    context.bot.send_message(update.message.chat_id, "Bienvenido to Download BOT by Jock404!")

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Bot Python Made By Jock404\nBot para descargar musica y videos de Youtube\nAdemas de descargar files GiutHub y files de Mediafire y mucho mas...\nPara descargar un video usa /down en el Menu\nPara descargar musica usa /downmusic\nPara descargar file de github usa /downgithub\nPara descargar videos de Vimeo /platf\nPara descargar file de Google Drive /downdrive')

def downdrive(update, context):
	ruta = os.getcwd()
	mess = update.message.chat_id
	user_data_username = update.message.from_user.username
	user_data_first_name = update.message.from_user.first_name
	user_data_id = update.message.from_user.id
	user_data_is_bot = update.message.from_user.is_bot
	user_data_language_code = update.message.from_user.language_code
	print(Fore.MAGENTA+" **** Nueva Descarga Google Drive**** \n"+Fore.RESET)
	print(Fore.CYAN+"################################################################################################"+Fore.RESET)
	carga = update.message.text
	splited_command = carga.split()
	url = splited_command[1]
	hora = time.strftime("%X")
	print("# - Start Time: "+Fore.RED,hora,Fore.RESET)
	msg_bot = update.message.reply_text("Downloading Drive Wait....!")
	output = ""
	if "https://drive.google.com/open?id=" in url:
		# print("Nodo 1 ",url)
		try:
			try:
				x = gdown.download(url, quiet=False)
				output = x
			except:
				gdown.download(url, quiet=False)
		except Exception as e:
			print(Fore.RED+"# - Error al Descargar con Gdown"+Fore.RESET)
			e = str(e)
			add_data_log(e)
	elif "https://drive.google.com/file/d/" in url:
		# print("Nodo 2 ",url)
		try:
			try:
				x = gdown.download(url, quiet=False, fuzzy=True)
				output = x
			except:
				gdown.download(url, quiet=False, fuzzy=True)
			
		except Exception as e:
			print(Fore.RED+"# - Error al Descargar con Gdown"+Fore.RESET)
			e = str(e)
			add_data_log(e)
	elif "https://drive.google.com/uc?id" in url:
		# print("Nodo 3 ",url)
		try:
			try:
				x = gdown.download(url, quiet=False)
				output = x
			except:
				gdown.download(url, quiet=False)
			
		except Exception as e:
			print(Fore.RED+"# - Error al Descargar con Gdown"+Fore.RESET)
			e = str(e)
			add_data_log(e)
	elif "https://drive.google.com/drive/folders/" in url:
		# print("Nodo 4 ",url)
		try:
			try:
				x = gdown.download_folder(url, quiet=True, use_cookies=False)
				output = x
			except:
				gdown.download_folder(url, quiet=True, use_cookies=False)
			
		except Exception as e:
			print(Fore.RED+"# - Error al Descargar con Gdown"+Fore.RESET)
			e = str(e)
			add_data_log(e)
	elif ((len(url) == 33) or (len(url) == 31)):
		# print("Nodo 5 ",url)
		id = url
		try:
			try:
				try:
					x = gdown.download(id=id, quiet=False)
					output = x
				except:
					gdown.download(id=id, quiet=False)
			except Exception as e:
				print(Fore.RED+"# - Error al Descargar con Gdown"+Fore.RESET)
				e = str(e)
				add_data_log(e)
		except:
			try:
				try:
					x = gdown.download_folder(id=id, quiet=True, use_cookies=False)
					output = x
				except:
					gdown.download_folder(id=id, quiet=True, use_cookies=False)
			except Exception as e:
				print(Fore.RED+"# - Error al Descargar con Gdown"+Fore.RESET)
				e = str(e)
				add_data_log(e)
	elif ((len(url) == 33) and ("--" in url)):
		# print("Nodo 6 ",url)
		id = url
		try:
			try:
				x = gdown.download(id=id, quiet=False)
				output = x
			except:
				gdown.download(id=id, quiet=False)
		except:
			try:
				try:
					x = gdown.download_folder(id=id, quiet=True, use_cookies=False)
					output = x
				except:
					gdown.download_folder(id=id, quiet=True, use_cookies=False)
			except Exception as e:
				print(Fore.RED+"# - Error al Descargar con Gdown"+Fore.RESET)
				e = str(e)
				add_data_log(e)
	else:
		print("# - "+Fore.RED+"ERROR ALERT "+Fore.RESET+"No es un Link Valido ")
		try:
			context.bot.delete_message(chat_id=mess,message_id=msg_bot.message_id)
		except Exception as e:
			print(Fore.RED+"your message no deleted ",e,Fore.RESET)
			e = str(e)
			add_data_log(e)
		return

	if output != None:
		if os.path.exists(output):
			context.bot.send_document(chat_id=user_data_id,document=open(output,'rb'),timeout=999, filename=output)
			clean(output)
		else:
			print("# - "+Fore.RED+"ERROR ALERT "+Fore.RESET+"Dont Exists File is a Folder ")
	else:
		print("Is a Folder")

	hora = time.strftime("%X")
	print("# - Finished at, ", hora)
	print(Fore.CYAN+"################################################################################################\n\n\n\n"+Fore.RESET)
	chunk = [user_data_id, url, hora, output, 'Files', user_data_username, user_data_first_name, user_data_is_bot, user_data_language_code]
	add_db(chunk)
	try:
		context.bot.delete_message(chat_id=mess,message_id=msg_bot.message_id)
	except Exception as e:
		print(Fore.RED+"your message no deleted ",e,Fore.RESET)
		e = str(e)
		add_data_log(e)
	msg_bot = update.message.reply_text("Download Drive Finish....!")
	pass

def downPlatform(update, context):
	ruta = os.getcwd()
	user_data_username = update.message.from_user.username
	user_data_first_name = update.message.from_user.first_name
	user_data_id = update.message.from_user.id
	user_data_is_bot = update.message.from_user.is_bot
	user_data_language_code = update.message.from_user.language_code
	print(Fore.MAGENTA+" **** Nueva Descarga Video Platform**** \n"+Fore.RESET)
	msg_bot1 = update.message.reply_text(" Descarga en Curso.... ")
	comando = update.message.text
	splited_command = comando.split()
	dirreccion = splited_command[1]
	mess = update.message.chat_id
	hora = time.strftime("%X")
	print(Fore.CYAN+"########################################################################################"+Fore.RESET)
	print("# - link: ",dirreccion," ID: ",mess, "Time: ",hora)
	try:
		ydl_opts = {}
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			info_dict = ydl.extract_info(dirreccion, download=False)
			video_title = info_dict.get('title', None)
			ydl.download([dirreccion])
	except Exception as e:
		print(Fore.RED+"# - Error al Descargar con Youtube_dl"+Fore.RESET)
		e = str(e)
		add_data_log(e)
	hora = time.strftime("%X")
	print("# - Upload to Server Finished at ,", hora)
	vidtitle = video_title
	chat_id = mess
	carct = vidtitle
	new_s = carct
	print("# - Proccess to Sending Video"+Fore.RED, carct, Fore.RESET)
	supres = '*|/?<>:🥵"'
	if "*" or "|" or "/" or "?" or "<" or ">" or ":" or "🥵" or '"' in carct:
		for c_x in supres:
			if c_x in carct:
				if c_x == "🥵":
					new_s = carct.replace(c_x, '🥵')
				else:
					new_s = carct.replace(c_x, '_')
					print("# - Caracter Detect"+Fore.RED+" ALERT"+Fore.RESET+" code: ",c_x)
	else:
		new_s = carct
		print("# - No Caracter NTFS Detect")
	x_x = 'https://vimeo.com/'
	if x_x in dirreccion:
		c = dirreccion.replace(x_x, '-')
		new_name = new_s + c + ".mp4"
	else:
		new_name = new_s + ".mp4"
		pass
	if os.path.exists(new_name):
		context.bot.send_video(chat_id=chat_id,video=open(new_name,'rb'),timeout=999, supports_streaming=True)
		clean(new_name)
	else:
		print("# - "+Fore.RED+"ERROR ALERT "+Fore.RESET+"Dont Exists File ",new_name)
	hora = time.strftime("%X")
	print("# - Finished at, ", hora)
	print(Fore.CYAN+"########################################################################################\n\n\n\n"+Fore.RESET)
	chunk = [user_data_id, dirreccion, hora, new_name, 'Video', user_data_username, user_data_first_name, user_data_is_bot, user_data_language_code]
	add_db(chunk)
	try:
		context.bot.delete_message(chat_id=mess,message_id=msg_bot1.message_id)
	except Exception as e:
		print(Fore.RED+"your message no deleted ",e,Fore.RESET)
		e = str(e)
		add_data_log(e)

def down(update, context):
	ruta = os.getcwd()
	user_data_username = update.message.from_user.username
	user_data_first_name = update.message.from_user.first_name
	user_data_id = update.message.from_user.id
	user_data_is_bot = update.message.from_user.is_bot
	user_data_language_code = update.message.from_user.language_code
	print(Fore.MAGENTA+" **** Nueva Descarga Video**** \n"+Fore.RESET)
	msg_bot1 = update.message.reply_text(" Descargando Video.... ")
	comando = update.message.text
	splited_command = comando.split()
	dirreccion = splited_command[1]
	mess = update.message.chat_id
	hora = time.strftime("%X")
	print(Fore.CYAN+"########################################################################################"+Fore.RESET)
	print("# - link: ",dirreccion," ID: ",mess, "Time: ",hora)
	try:
		video = pafy.new(dirreccion)
		best = video.getbest(preftype="mp4")
		best.download(ruta)
	except Exception as e:
		print(Fore.RED+"# - Error al Descargar con Pafy"+Fore.RESET)
		e = str(e)
		add_data_log(e)
	print("# - Path: ", ruta)
	hora = time.strftime("%X")
	print("# - Upload to Server Finished at ,", hora)
	vidtitle = video.title
	chat_id = mess
	carct = vidtitle
	new_s = carct
	print("# - Proccess to Sending Video"+Fore.RED, carct, Fore.RESET)
	supres = '*|/?<>:🥵"'
	if "*" or "|" or "/" or "?" or "<" or ">" or ":" or "🥵" or '"' in carct:
		for c_x in supres:
			if c_x in carct:
				if c_x == "🥵":
					new_s = carct.replace(c_x, '🥵')
				else:
					new_s = carct.replace(c_x, '_')
					print("# - Caracter Detect"+Fore.RED+" ALERT"+Fore.RESET+" code: ",c_x)
	else:
		new_s = carct
		print("# - No Caracter NTFS Detect")
	new_name = new_s + ".mp4"
	if os.path.exists(new_name):
		context.bot.send_video(chat_id=chat_id,video=open(new_name,'rb'),timeout=999, supports_streaming=True)
		clean(new_name)
	else:
		print("# - "+Fore.RED+"ERROR ALERT "+Fore.RESET+"Dont Exists File ",new_name)
	hora = time.strftime("%X")
	print("# - Finished at, ", hora)
	print(Fore.CYAN+"########################################################################################\n\n\n\n"+Fore.RESET)
	chunk = [user_data_id, dirreccion, hora, new_s, 'Video', user_data_username, user_data_first_name, user_data_is_bot, user_data_language_code]
	add_db(chunk)
	try:
		context.bot.delete_message(chat_id=mess,message_id=msg_bot1.message_id)
	except Exception as e:
		print(Fore.RED+"your message no deleted ",e,Fore.RESET)
		e = str(e)
		add_data_log(e)

def downmusic(update, context):
	ruta = os.getcwd()
	user_data_username = update.message.from_user.username
	user_data_first_name = update.message.from_user.first_name
	user_data_id = update.message.from_user.id
	user_data_is_bot = update.message.from_user.is_bot
	user_data_language_code = update.message.from_user.language_code
	print(Fore.MAGENTA+" **** Nueva Descarga Musica**** \n"+Fore.RESET)
	msg_bot2 = update.message.reply_text(" Descargando Musica....")
	comando = update.message.text
	splited_command = comando.split()
	dirreccion = splited_command[1]
	mess = update.message.chat_id
	hora = time.strftime("%X")
	print(Fore.CYAN+"########################################################################################"+Fore.RESET)
	print("# - link: ",dirreccion," ID: ",mess, "Time: ",hora)
	video = pafy.new(dirreccion)
	chek_mp3 = video.title + ".mp3"
	print("ACA EL CHECK DEL MP3 ",chek_mp3)
	if os.path.exists(chek_mp3):
		print("# - Existe MP3 not Download Video")
	else:
		try:
			best = video.getbest(preftype="mp4")
			best.download(ruta)
		except Exception as e:
			print(Fore.RED+"# - Error al Descargar con Pafy"+Fore.RESET)
			e = str(e)
			add_data_log(e)
	print("# - Path: ", ruta)
	hora = time.strftime("%X")
	print("# - Upload to Server Finished at ,", hora)
	vidtitle = video.title
	chat_id = mess
	carct = vidtitle
	new_s = carct
	print("# - Proccess to Sending Musica"+Fore.RED, carct , Fore.RESET)
	supres = '*|/?<>:🥵"'
	if "*" or "|" or "/" or "?" or "<" or ">" or ":" or "🥵" or '"' in carct:
		for c_x in supres:
			if c_x in carct:
				if c_x == "🥵":
					new_s = carct.replace(c_x, '🥵')
				else:
					new_s = carct.replace(c_x, '_')
					print("# - Caracter Detect"+Fore.RED+" ALERT"+Fore.RESET+" code: ",c_x)
					carct = new_s
	else:
		new_s = carct
		print("# - No Caracter NTFS Detect")
	new_name = new_s + ".mp4"
	chek_mp3_2 = new_s + ".mp3"
	if os.path.exists(new_name):
		clip = mp.VideoFileClip(new_name)
		clip.audio.write_audiofile(new_s + ".mp3")
		clip.close()
		clean(new_name)
		new_name = new_s + ".mp3"
		context.bot.send_audio(chat_id=chat_id,audio=open(new_name,'rb'),timeout=999)
		clean(new_name)
	elif os.path.exists(chek_mp3_2):
		new_name = new_s + ".mp3"
		context.bot.send_audio(chat_id=chat_id,audio=open(new_name,'rb'),timeout=999)
		clean(new_name)
	else:
		print("# - "+Fore.RED+"ERROR ALERT "+Fore.RESET+"Dont Exists File ",new_name)
	hora = time.strftime("%X")
	print("# - Finished at, ", hora)
	print(Fore.CYAN+"########################################################################################\n\n\n\n"+Fore.RESET)
	chunk = [user_data_id, dirreccion, hora, new_s, 'Musica', user_data_username, user_data_first_name, user_data_is_bot, user_data_language_code]
	add_db(chunk)
	try:
		context.bot.delete_message(chat_id=mess,message_id=msg_bot2.message_id)
	except Exception as e:
		print(Fore.RED+"your message no deleted ",e,Fore.RESET)
		e = str(e)
		add_data_log(e)

def downgithub(update, context):
	ruta = os.getcwd()
	mess = update.message.chat_id
	user_data_username = update.message.from_user.username
	user_data_first_name = update.message.from_user.first_name
	user_data_id = update.message.from_user.id
	user_data_is_bot = update.message.from_user.is_bot
	user_data_language_code = update.message.from_user.language_code
	print(Fore.MAGENTA+" **** Nueva Descarga Github**** \n"+Fore.RESET)
	print(Fore.CYAN+"################################################################################################"+Fore.RESET)
	comando = update.message.text
	splited_command = comando.split()
	cmd = splited_command[1]
	hora = time.strftime("%X")
	print("# - Start Time: "+Fore.RED,hora,Fore.RESET)
	msg_bot = update.message.reply_text("Downloading Wait....!")
	try:
		check_output("git clone "+cmd, shell=True).decode()
		update.message.reply_text("Access - Download Garant!!!")
	except Exception as e:
		print(Fore.RED+"# - Error File Same Name Exists in the Directory"+Fore.RESET)
		update.message.reply_text("Error File Already Exists in the Server")
		e = str(e)
		add_data_log(e)
	hora = time.strftime("%X")
	print("# - link: "+Fore.RED,cmd,Fore.RESET+" ID: "+Fore.RED,mess,Fore.RESET+"Finished Time: "+Fore.RED,hora,Fore.RESET)
	print(Fore.CYAN+"################################################################################################\n\n\n"+Fore.RESET)
	chunk = [user_data_id, cmd, hora, 'Fichero GiutHub', 'File GiutHub', user_data_username, user_data_first_name, user_data_is_bot, user_data_language_code]
	add_db(chunk)
	try:
		context.bot.delete_message(chat_id=mess,message_id=msg_bot.message_id)
	except Exception as e:
		print(Fore.RED+"your message no deleted ",e,Fore.RESET)
		e = str(e)
		add_data_log(e)

def downfire(update, context):
	import urllib3
	urllib3.disable_warnings()
	ruta = os.getcwd()
	user_data_username = update.message.from_user.username
	user_data_first_name = update.message.from_user.first_name
	user_data_id = update.message.from_user.id
	user_data_is_bot = update.message.from_user.is_bot
	user_data_language_code = update.message.from_user.language_code
	print(Fore.MAGENTA+" **** Nueva Descarga Mediafire o files**** \n"+Fore.RESET)
	msg_bot2 = update.message.reply_text(" Descargando Mediafire....")
	comando = update.message.text
	splited_command = comando.split()
	url = splited_command[1]
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
	mess = update.message.chat_id
	hora = time.strftime("%X")
	print(Fore.CYAN+"########################################################################################"+Fore.RESET)
	print("# - link: ",url," ID: ",mess, "Time: ",hora)
	try:
		req = requests.get(url, headers=headers, verify=False)
		filename = req.url[url.rfind('/')+1:]
		print('FileName >>> ',filename)
		with requests.get(url, headers=headers, verify=False) as req:
			with open(filename, 'wb') as f:
				for chunk in req.iter_content(chunk_size=8192):
					if chunk:
						f.write(chunk)
			return filename
		try:
			context.bot.delete_message(chat_id=mess,message_id=msg_bot2.message_id)
		except Exception as e:
			print(Fore.RED+"your message no deleted ",e,Fore.RESET)
			e = str(e)
			add_data_log(e)
		msg_bot = update.message.reply_text("Download Finish....!")
		hora = time.strftime("%X")
		print("# - link: "+Fore.RED,url,Fore.RESET+" ID: "+Fore.RED,mess,Fore.RESET+"Finished Time: "+Fore.RED,hora,Fore.RESET)
		print(Fore.CYAN+"################################################################################################\n\n\n"+Fore.RESET)
		chunk = [user_data_id, url, hora, filename, 'File Mediafire', user_data_username, user_data_first_name, user_data_is_bot, user_data_language_code]
		add_db(chunk)
	except Exception as e:
		print(Fore.RED+"Not Working check log dat ",e,Fore.RESET)
		e = str(e)
		add_data_log(e)
		return None

def main():
    with open('API_KEY.HASH',"r") as key:
        TOKEN = key.read()
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    hora = time.strftime("%X")
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('down', down))
    dp.add_handler(CommandHandler('platf', downPlatform))
    dp.add_handler(CommandHandler('downmusic', downmusic))
    dp.add_handler(CommandHandler('downgithub', downgithub))
    dp.add_handler(CommandHandler('downdrive', downdrive))
    dp.add_handler(CommandHandler('downfire', downfire))
    dp.add_handler(CommandHandler("help", help_command))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
	create_db()
	main()
