import re


def get_author(text):
	
	result = re.findall(r"\n\*\*Autor\*\*:\s__(.+)__", text)
	
	if result:
		return re.sub(r"\s+", " ", result[0]).strip()


def get_publisher(text):
	
	result = re.findall(r"\n\*\*Editora\*\*:\s__(.+)__", text)
	
	if result:
		return re.sub(r"\s+", " ", result[0]).strip()


def get_book_type(text):
	
	result = re.findall(r"\n\*\*Tipo\*\*:\s__(.+)__", text)
	
	if result:
		return re.sub(r"\s+", " ", result[0]).strip()


def get_category(text):
	
	result = re.findall(r"\n\*\*Categoria\*\*:\s__(.+)__", text)
	
	if result:
		return re.sub(r"\s+", " ", result[0]).strip()


def get_narrator(text):
	
	result = re.findall(r"\n\*\*Narrador\*\*:\s__(.+)__", text)
	
	if result:
		return re.sub(r"\s+", " ", result[0]).strip()


def get_duration(text):
	
	result = re.findall(r"\n\*\*Duração\*\*:\s__(.+)__", text)
	
	if result:
		return re.sub(r"\s+", " ", result[0]).strip()


def get_year(text):
	
	result = re.findall(r"\n\*\*Ano\*\*:\s__([0-9]{4})__", text)
	
	if result:
		return re.sub(r"\s+", " ", result[0]).strip()


def get_original_language(text):
	
	result = re.findall(r"\n\*\*Idioma\*\*:\s__(.+)__", text)
	
	if result:
		return re.sub(r"\s+", " ", result[0]).strip()


def get_chapters(text):
	
	result = re.findall(r"\n\*\*Capítulos\*\*:\s__(.+)__", text)
	
	if result:
		value = re.sub(r"\s+", " ", result[0]).strip()
		try:
			value = float(value)
		except ValueError:
			return
		else:
			if value.is_integer():
				return int(value)
			return value


def get_volumes(text):
	
	result = re.findall(r"\n\*\*Volumes\*\*:\s__(.+)__", text)
	
	if result:
		value = re.sub(r"\s+", " ", result[0]).strip()
		try:
			value = float(value)
		except ValueError:
			return
		else:
			if value.is_integer():
				return int(value)
			return value


def get_artist(text):
	
	result = re.findall(r"\n\*\*Arte\*\*:\s__(.+)__", text)
	
	if result:
		return re.sub(r"\s+", " ", result[0]).strip()


def get_genres(text):
	
	result = re.findall(r"\n\*\*Gênero\*\*:\s__(.+)__", text)
	
	if result:
		return re.sub(r"\s+", " ", result[0]).strip()

