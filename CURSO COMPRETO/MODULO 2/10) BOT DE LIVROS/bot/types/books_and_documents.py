import datetime
from typing import Union, List, Any
from itertools import zip_longest
import random

from asyncpg.connection import Connection

from .config import CHAT_ID
from .utils import remove_accents, remove_punctuation, capitalize_words, bytes_to_human


class Title(str):
	"""
	Um objeto representando um tipo de título, geralmente
	o nome de um autor, editora, categoria e entre outros.
	"""
	def __init__(self, string):
		self.capitalized = capitalize_words(string)
		self.stripped = remove_punctuation(remove_accents(string))


class Duration(int):
	"""Um objeto representando a duração de um audiobook."""
	def __init__(self, seconds):
		self.human = str(datetime.timedelta(seconds=seconds))


class Size(int):
	"""Um objeto representando informações sobre o tamanho de um arquivo."""
	def __init__(self, size):
		self.human = bytes_to_human(size)


class Document:
	"""Objeto representando informações sobre um documento."""
	def __init__(self, document):
		self.file_id = document["file_id"]


class Photo:
	"""Objeto representando informações sobre uma imagem."""
	def __init__(self, photo):
		self.file_id = photo["file_id"]


class Book:
	"""Objeto representando informações sobre um livro."""
	def __init__(self, book: dict) -> None:
		
		self.message = book["message"]
		self.title = Title(book["title"]) if book["title"] else None
		self.type = Title(book["type"]) if book["type"] else None
		self.category = Title(book["category"]) if book["category"] else None
		self.author = Title(book["author"]) if book["author"] else None
		self.narrator = Title(book["narrator"]) if book["narrator"] else None
		self.publisher = Title(book["publisher"]) if book["publisher"] else None
		self.duration = Duration(book["duration"]) if book["duration"] else None
		self.year = book["year"]
		self.chapters = book["chapters"]
		self.genre = book["genre"]
		self.size = Size(book["size"]) if book["size"] else None
		self.photo = Photo(book["photo"]) if book["photo"] else None
		self.documents = []
		
		for document in book["documents"]:
			self.documents.append(
				Document(document)
			)


class Library:
	"""Objeto representando informações sobre vários livros."""
	def __init__(self, categories: list, authors: list, narrators: list, publishers: list, types: list) -> None:
		self.books = []
		self.categories = categories
		self.authors = authors
		self.narrators = narrators
		self.publishers = publishers
		self.types = types
		
		# Ordenar todos os itens das listas em ordem alfabética.
		self.categories.sort()
		self.authors.sort()
		self.narrators.sort()
		self.publishers.sort()
		self.types.sort()
	
	
	# Este método é usado para obter uma lista de todas as categorias disponíveis.
	def get_categories(self):
		return self.create_pagination(list(enumerate(self.categories)), fillvalue=(None, None))
	
	
	# Este método é usado para obter uma lista de todas os autores disponíveis.
	def get_authors(self):
		return self.create_pagination(list(enumerate(self.authors)), fillvalue=(None, None))
	
	
	# Este método é usado para obter uma lista de todas os narradores disponíveis.
	def get_narrators(self):
		return self.create_pagination(list(enumerate(self.narrators)), fillvalue=(None, None))
	
	
	# Este método é usado para obter uma lista de todas as editoras disponíveis.
	def get_publishers(self):
		return self.create_pagination(list(enumerate(self.publishers)), fillvalue=(None, None))
	
	
	# Este método é usado para obter uma lista de todas os tipos disponíveis.
	def get_types(self):
		return self.create_pagination(list(enumerate(self.types)), fillvalue=(None, None))
	
	
	# Este método é usado para obter uma lista de todos os anos de publicação disponíveis.
	def get_years(self):
		return self.create_pagination(list(enumerate(self.years)), fillvalue=(None, None))
	
	
	# Este método é usado para obter um livro aleatório da lista.
	def get_random(self) -> Book:
		return random.choice(self.books)
	
	
	# Este método é usado para adicionar livros a lista.
	def append(self, book: Book) -> None:
		self.books.append(book)
	
	
	# Este método é usado para obter um livro específico da lista.
	# Os livros são distinguidos usando o ID númerico da mensagem
	# correspondente enviada no canal Telegram.
	def get(self, message_id: int) -> Union[None, Book]:
		
		for book in self.books:
			if book.message == message_id:
				return book
	
	
	# Este método é usado para obter livros de um determinado tipo, autor, editora e entre outros.
	def get_books(self, category: str = int, author: str = int, narrator: str = int, publisher: str = int, book_type: str = int) -> List[Book]:
		
		results = []
		
		if isinstance(category, int):
			category_name = self.categories[category]
			for book in self.books:
				if book.category and book.category == category_name:
					results.append(book)
			return self.create_pagination(results)
		
		if isinstance(author, int):
			author_name = self.authors[author]
			for book in self.books:
				if book.author and book.author == author_name:
					results.append(book)
			return self.create_pagination(results)
		
		if isinstance(narrator, int):
			narrator_name = self.narrators[narrator]
			for book in self.books:
				if book.narrator and book.narrator == narrator_name:
					results.append(book)
			return self.create_pagination(results)
		
		if isinstance(publisher, int):
			publisher_name = self.publishers[publisher]
			for book in self.books:
				if book.publisher and book.publisher == publisher_name:
					results.append(book)
			return self.create_pagination(results)
		
		if isinstance(book_type, int):
			type_name = self.types[book_type]
			for book in self.books:
				if book.type and book.type == type_name:
					results.append(book)
			return self.create_pagination(results)
	
	
	# Este método é usado para pesquisar por livros.
	def search(self, query: str) -> Union[None, List[Union[Book, None]]]:
		search_results = []
		
		# Aqui convertemos todos os caracteres para minúsculo e também removemos os acentos e as
		# pontuações.
		query = remove_punctuation(remove_accents(query.lower()))
		
		# Aqui separamos cada palavra com mais de 2 caracteres em uma lista.
		splited_query = tuple(
			word for word in query.split() if len(word) > 2
		)
		
		for book in self.books:
			if book.title:
				if (query in book.title.stripped or
					all(word in book.title.stripped for word in splited_query)):
					search_results.append(book)
					continue
			
			if book.type:
				if (query in book.type.stripped or
					all(word in book.type.stripped for word in splited_query)):
					search_results.append(book)
					continue
			
			if book.category:
				if (query in book.category.stripped or
					all(word in book.category.stripped for word in splited_query)):
					search_results.append(book)
					continue
			
			if book.author:
				if (query in book.author.stripped or
					all(word in book.author.stripped for word in splited_query)):
					search_results.append(book)
					continue
			
			if book.narrator:
				if (query in book.narrator.stripped or
					all(word in book.narrator.stripped for word in splited_query)):
					search_results.append(book)
					continue
			
			if book.publisher:
				if (query in book.publisher.stripped or
					all(word in book.publisher.stripped for word in splited_query)):
					search_results.append(book)
					continue
		
		if search_results:
			return self.create_pagination(search_results)
	
	
	# Este método é usado para criar uma lista contendo tuples de até 10 livros.
	def create_pagination(self, items: list, fillvalue: Any = None) -> List[Union[Book, None]]:
		return list(zip_longest(*[iter(items)] * 10, fillvalue=fillvalue))


class UserLibrary:
	"""Um objeto representando uma listas contendo livros de um usuário."""
	def __init__(self, index: int, conn: Connection, user_id: int, read: list, reading: list, dropped: list, favorites: list) -> None:
		self.index = index
		self.conn = conn
		self.user_id = user_id
		self.read = read
		self.reading = reading
		self.dropped = dropped
		self.favorites= favorites
	
	
	# Este método é usado para obter uma lista de livros específica do usuário.
	def get_list(self, category: Union[str, int]) -> Union[List[int], None]:
		
		if category in (1, "read"):
			return self.read if self.read else None
		
		if category in (2, "reading"):
			return self.reading if self.reading else None
		
		if category in (3, "dropped"):
			return self.dropped if self.dropped else None
		
		if category in (4, "favorites"):
			return self.favorites if self.favorites else None
	
	
	# Este método é usado para verificar se o usuário possui um determinado
	# livro em uma de suas listas.
	def has(self, book: Book, category: Union[str, int] = None) -> bool:
		if category is None:
			return (
				book.message in self.read or
				book.message in self.reading or
				book.message in self.dropped or
				book.message in self.favorites
			)
		
		if category in (1, "read"):
			return (book.message in self.read)
		
		if category in (2, "reading"):
			return (book.message in self.reading)
		
		if category in (3, "dropped"):
			return (book.message in self.dropped)
		
		if category in (4, "favorites"):
			return (book.message in self.favorites)
	
	
	# Este método é usado para adicionar um livro a uma das listas
	# do usuário.
	def add(self, book: Book, category: Union[str, int]) -> None:
		if self.has(book, category):
			return
		
		if category in (1, "read"):
			self.read.append(book.message)
		elif category in (2, "reading"):
			self.reading.append(book.message)
		elif category in (3, "dropped"):
			self.dropped.append(book.message)
		elif category in (4, "favorites"):
			self.favorites.append(book.message)
	
	
	# Este método é usado para remover um livro de uma das listas
	# do usuário.
	def remove(self, book: Book, category: Union[str, int] = None) -> None:
		if not self.has(book, category):
			return
			
		if category is None:
			if book.message in self.read:
				self.read.remove(book.message)
			elif book.message in self.reading:
				self.reading.remove(book.message)
			elif book.message in self.dropped:
				self.dropped.remove(book.message)
			return
		
		if category in (1, "read"):
			if book.message in self.read:
				self.read.remove(book.message)
		elif category in (2, "reading"):
			if book.message in self.reading:
				self.reading.remove(book.message)
		elif category in (3, "dropped"):
			if book.message in self.dropped:
				self.dropped.remove(book.message)
		elif category in (4, "favorites"):
			if book.message in self.favorites:
				self.favorites.remove(book.message)
	
	
	# Este método é usado para atualizar a row do usuário.
	# Deve ser chamado sempre que uma das listas sofrer modificações.
	async def refresh(self) -> None:
		command = """
			UPDATE users
			SET read = $1,
					reading = $2,
					dropped = $3,
					favorites = $4
			WHERE user_id = $5
		"""
		
		async with self.conn.transaction() as transaction:
			await self.conn.execute(
				command,
				self.read,
				self.reading,
				self.dropped,
				self.favorites,
				self.user_id
			)
	
	
	# Este método é usado para deletar a row do usuário.
	async def delete(self) -> None:
		command = """
			DELETE FROM users
			WHERE user_id = $1
		"""
		
		async with self.conn.transaction() as transaction:
			await self.conn.execute(command, self.user_id)
	
		