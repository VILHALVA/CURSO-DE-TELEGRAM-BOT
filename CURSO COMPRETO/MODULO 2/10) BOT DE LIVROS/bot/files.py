import asyncio
import json

import aiofiles

from .config import (
	BOOKS_FILE, STRINGS_FILE, CATEGORIES_FILE, AUTHORS_FILE,
	NARRATORS_FILE, PUBLISHERS_FILE, TYPES_FILE
)

# Este método abre um arquivo retorna seu conteúdo como uma string.
async def read_file(filename: str) -> str:
	
	async with aiofiles.open(file=filename, mode="r") as file:
		content = await file.read()
	
	return content

# Este método converte o conteúdo de um arquivo json para um dict.
async def file_to_dict(filename: str) -> dict:
	
	content = await read_file(filename)
	return json.loads(content)

future = asyncio.gather(
	file_to_dict(BOOKS_FILE),
	file_to_dict(STRINGS_FILE),
	file_to_dict(CATEGORIES_FILE),
	file_to_dict(AUTHORS_FILE),
	file_to_dict(NARRATORS_FILE),
	file_to_dict(PUBLISHERS_FILE),
	file_to_dict(TYPES_FILE)
)

loop = asyncio.get_event_loop()
books, strings, categories, authors, narrators, publishers, types = loop.run_until_complete(future)
