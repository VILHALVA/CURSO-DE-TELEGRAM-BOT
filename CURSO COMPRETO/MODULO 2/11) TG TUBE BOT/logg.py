import os, time
def add_data_log(error):
	hora = time.strftime("%X")
	filename = '\\logger.dat'
	ruta = os.getcwd()
	file = open(ruta + filename, "a", encoding="ISO-8859-1")
	file.write(hora+ os.linesep)
	file.write(error+os.linesep)
	file.write("###############################################################################################"+os.linesep)
	file.close()
