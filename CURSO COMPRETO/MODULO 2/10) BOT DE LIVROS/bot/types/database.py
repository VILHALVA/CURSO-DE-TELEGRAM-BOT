from typing import Union
import random
import string

import asyncpg
from asyncpg.exceptions import DuplicateTableError
from asyncpg import Record

from .books_and_documents import UserLibrary


class Database:
	"""Objeto usado para gerenciar informações gerais sobre os usuários."""
	def __init__(self, options: dict) -> None:
		self.options = options
		
	
	# Está método cria a conexão para o servidor do
	# bsnco de dados e adiciona a table "users".
	async def initialize(self) -> None:
		commands = (
			"""
				CREATE TABLE users (
					id serial PRIMARY KEY,
					user_id int,
					read int[],
					reading int[],
					dropped int[],
					favorites int[]
				)
			""",
			"""
				CREATE TABLE queries (
					id serial PRIMARY KEY,
					query_id text,
					query_text text
				)
			"""
		)
		
		self.conn = await asyncpg.connect(**self.options)
		
		for command in commands:
			try:
				async with self.conn.transaction() as transaction:
					await self.conn.execute(command)
			except DuplicateTableError:
				pass
	
	
	# Este método é usado para criar um nova row para o usuário.
	async def create_user(self, user_id: int) -> None:
		command = """
			INSERT INTO users (
				user_id, read, reading, dropped, favorites
			)
			VALUES (
				$1, $2, $3, $4, $5
			)
		"""
		
		async with self.conn.transaction() as transaction:
			await self.conn.execute(command, user_id, [], [], [], [])
	
	
	# Este método é usado para obter a row do usuário.
	async def get_user(self, user_id: int) -> Union[None, Record]:
		command = """
			SELECT *
			FROM users
			WHERE user_id = $1
		"""
	
		return await self.conn.fetchrow(command, user_id)
	
	
	# Este método é usado para obter a "biblioteca" de livros do usuário.
	async def get_library(self, user_id: int) -> UserLibrary:
		user_row = await self.get_user(user_id)
		if not user_row:
			return
		values = user_row.values()
		
		index, user_id, read, reading, dropped, favorites = list(values)
		
		library = dict(
			index=index,
			conn=self.conn,
			user_id=user_id,
			read=read,
			reading=reading,
			dropped=dropped,
			favorites=favorites
		)
		
		return UserLibrary(**library)
	
	
	# Este método associa o termo pesquisado pelo usuário a
	# um ID único de até 9 caracteres compostos por letras.
	async def create_query(self, query: str) -> str:
		command = """
			INSERT INTO queries (
				query_id, query_text
			)
			VALUES (
				$1, $2
			)
		"""
		
		query_id = "".join(random.choices(string.ascii_uppercase, k=9))
		
		async with self.conn.transaction() as transaction:
			await self.conn.execute(command, query_id, query)
		
		return query_id
	
	
	# Este método retorna um termo com base no ID gerado pelo "create_query".
	async def get_query(self, query_id: str) -> str:
		command = """
			SELECT query_text
			FROM queries
			WHERE query_id = $1
		"""
		
		row = await self.conn.fetchrow(command, query_id)
		return row.get("query_text")

