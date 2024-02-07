import unicodedata
import re


# Este método é usado para converter a primeira letra de cada palavra com mais de
# 3 caracteres para maiúsculo.
def capitalize_words(string):
    
	return " ".join(
		[
			word.capitalize() if not word.istitle() and len(word) > 3 else word for word in string.split(" ")
		]
	)


# Este método é usado para converter letras com acento para sua representação
# em ASCII.
def remove_accents(string):
	
    nfkd = unicodedata.normalize('NFKD', string)
    
    return "".join(
		[
			character for character in nfkd if not unicodedata.combining(character)
		]
	)


# Este método é usado para remover pontuações de strings
def remove_punctuation(string):
	return re.sub(r'[^\w\s]','', string)


# Este método é usado para converter bytes em uma string legível por humanos.
def bytes_to_human(bytes):
	
	bytes = float(bytes)
	kilobytes = float(1024)
	megabytes = float(kilobytes ** 2)
	gigabytes = float(kilobytes ** 3)
	terabytes = float(kilobytes ** 4)
	
	if bytes < kilobytes:
		return '{0} {1}'.format(bytes, 'Bytes' if 0 == bytes > 1 else 'Byte')
	
	if kilobytes <= bytes < megabytes:
		return '{0:.2f} KB'.format(bytes / kilobytes)
	
	if megabytes <= bytes < gigabytes:
		return '{0:.2f} MB'.format(bytes / megabytes)
	
	if gigabytes <= bytes < terabytes:
		return '{0:.2f} GB'.format(bytes / gigabytes)
	
	if terabytes <= bytes:
		return '{0:.2f} TB'.format(bytes / terabytes)

