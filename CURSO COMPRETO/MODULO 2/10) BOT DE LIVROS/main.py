import asyncio

from pyrogram import Client
from pyrogram.types import CallbackQuery, InputMediaPhoto

from bot.config import ASYNCPG_OPTIONS, PYROGRAM_OPTIONS
from bot.files import (
	books, strings, categories, authors, narrators, publishers, types
)
from bot import filters
from bot.types.books_and_documents import Book, Library
from bot.types.callback import CallbackQueryData
from bot.types.database import Database
from bot.types.strings import Strings
from bot.reply_markup import *
from bot.utils import (
	create_caption, create_media_group
)

# Criamos o cliente usado para acessar a API do Telegram.
app = Client(**PYROGRAM_OPTIONS)

# Este handler é usado para enviar a mensagem de vindas.
@app.on_message(filters.command(commands=["start"]))
async def handle_welcome(client, message):
	
	user = await database.get_user(message.from_user.id)
	
	if not user:
		await database.create_user(message.from_user.id)
	
	reply_markup = create_welcome(strings)
	
	await client.send_message(
		chat_id=message.from_user.id,
		text=strings.welcome_message,
		reply_markup=reply_markup
	)
	
	await message.stop_propagation()
	
	return


# Esse è o ovo de páscoa que você não recebeu em abril.
@app.on_message(filters.command(commands=["help"]))
async def handle_help(client, message):
	
	await client.send_message(
		chat_id=message.from_user.id,
		text=strings.not_help_you_message
	)
	
	await message.stop_propagation()
	
	return


# Este handler é usado para enviar um livro aleatório para o usuário.
@app.on_message(filters.command(commands=["random"]))
async def handle_random(client, message):
	
	book = library.get_random()
	
	reply_markup = create_random(strings, book)
	
	await client.send_photo(
		chat_id=message.from_user.id,
		photo=book.photo.file_id,
		caption=create_caption(book),
		reply_markup=reply_markup
	)
	
	return


# Este retornará um menu onde será possível que o usuário exclua seus dados.
@app.on_message(filters.command(commands=["delete"]))
async def handle_delete(client, message):
	
	reply_markup = create_delete(strings)
	
	await client.send_message(
		chat_id=message.from_user.id,
		text=strings.delete.format(strings.button_delete_data),
		reply_markup=reply_markup
	)
	
	return


# Este handler excluirá todos os dados que o bot possui sobre o usuário.
@app.on_callback_query(filters=filters.delete_account)
async def handle_delete_account(client: Client, callback: CallbackQuery) -> None:
	
	user_library = await database.get_library(callback.from_user.id)
	await user_library.delete()
	
	await callback.message.delete()
	
	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_who_are_you
	)
	
	await callback.stop_propagation()
	
	return


# Este handler retornará um novo livro aleatório.
@app.on_callback_query(filters=filters.new_random)
async def handle_new_random(client: Client, callback: CallbackQuery) -> None:
	
	book = library.get_random()
	
	media = InputMediaPhoto(media=book.photo.file_id, caption=create_caption(book))
	
	reply_markup = create_random(strings, book)
	
	await client.edit_message_media(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		media=media,
		reply_markup=reply_markup
	)
	
	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_new_random
	)

	await callback.stop_propagation()
	
	return


# Usado para gerenciar a pesquisa de livros via mensagem privada.
@app.on_message(filters.private)
async def handle_search(client, message):
	
	single_id = await database.create_query(message.text)
	results = library.search(message.text)
	
	if not results:
		await client.send_message(
			chat_id=message.from_user.id,
			text=strings.no_results_found
		)
		return
	
	if len(results) > 1:
		reply_markup = create_results(strings, results[0], single_id, 0, next_button=True)
	else:
		reply_markup = create_results(strings, results[0], single_id, 0)
	
	await client.send_message(
		chat_id=message.from_user.id,
		text=strings.search_results,
		reply_markup=reply_markup
	)
	
	await message.stop_propagation()
	
	return


# Este handler retornará a próxima lista de livros dos resultados da busca.
@app.on_callback_query(filters=filters.next_resuts)
async def handle_next_resuts(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	query = await database.get_query(data.id)
	
	results = library.search(query)
	
	next_page = (data.page + 1)
	next_results = results[next_page]

	if (next_page + 1) < len(results):
		reply_markup = create_results(strings, next_results, data.id, next_page, prev_button=True, next_button=True)
	else:
		reply_markup = create_results(strings, next_results, data.id, next_page, prev_button=True)
	
	await client.edit_message_text(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		text=strings.search_results,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_next_books
	)

	await callback.stop_propagation()

	return


# Este handler retornará a lista de livros anterior dos resultados da busca.
@app.on_callback_query(filters=filters.prev_resuts)
async def handle_prev_resuts(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	query = await database.get_query(data.id)
	
	results = library.search(query)
	
	prev_page = (data.page - 1)
	prev_results = results[prev_page]

	if prev_page != 0:
		reply_markup = create_results(strings, prev_results, data.id, prev_page, prev_button=True, next_button=True)
	else:
		reply_markup = create_results(strings, prev_results, data.id, prev_page, next_button=True)
	
	await client.edit_message_text(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		text=strings.search_results,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_prev_books
	)

	await callback.stop_propagation()

	return


# Este handler exclui a mensagem solicitada pelo usuário.
@app.on_callback_query(filters=filters.delete_message)
async def handle_delete_message(client: Client, callback: CallbackQuery) -> None:
	
	await callback.message.delete()
	
	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_handes_free
	)
	
	await callback.stop_propagation()
	
	return


# Este handler retornará uma "página" contendo informações sobre um livro.
@app.on_callback_query(filters=filters.book_page)
async def handle_book_page(client: Client, callback: CallbackQuery) -> None:
	
	user_library = await database.get_library(callback.from_user.id)
	
	data = CallbackQueryData(callback.data)
	book = library.get(data.id)
	
	if user_library.has(book, 4):
		reply_markup = create_book_page(strings, book, is_favorited=True)
	else:
		reply_markup = create_book_page(strings, book)

	await client.send_photo(
		chat_id=callback.from_user.id,
		photo=book.photo.file_id,
		caption=create_caption(book),
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_book_sent
	)

	await callback.stop_propagation()

	return


# Este handler adicionará o livro selecionado a sua lista pessoal de favoritos.
@app.on_callback_query(filters=filters.favorite)
async def handle_favorite(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	book = library.get(data.id)
	
	# Adicionar o livro a lista de favoritos.
	user_library = await database.get_library(callback.from_user.id)
	user_library.add(book, 4)
	await user_library.refresh()
	
	reply_markup = create_book_page(strings, book, is_favorited=True)
	
	await client.edit_message_reply_markup(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_list_updated
	)

	await callback.stop_propagation()
	
	return


# Este handler removerá o livro selecionado da lista pessoal de favoritos do usuário.
@app.on_callback_query(filters=filters.unfavorite)
async def handle_unfavorite(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	book = library.get(data.id)
	
	# Remover o livro da lista de favoritos.
	user_library = await database.get_library(callback.from_user.id)
	user_library.remove(book, 4)
	await user_library.refresh()
	
	reply_markup = create_book_page(strings, book)
	
	await client.edit_message_reply_markup(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		reply_markup=reply_markup
	)
	
	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_list_updated
	)

	await callback.stop_propagation()
	
	return


# Este handler todos os documentos relacionados ao livro solicitado pelo usuário.
@app.on_callback_query(filters=filters.get_document)
async def handle_get_document(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	book = library.get(data.id)
	
	media_group = create_media_group(book)
	
	await client.send_media_group(
		chat_id=callback.from_user.id,
		media=media_group
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_book_sent
	)

	await callback.stop_propagation()
	
	return


# Este handler retornará um menu com opções que possibilitam ao usuário adicionar o
# livro em questão a uma de suasy listas pessoais.
@app.on_callback_query(filters=filters.list_add)
async def handle_list_add(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	book = library.get(data.id)
	
	reply_markup = create_lists_add(strings, book)
	
	await client.edit_message_caption(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		caption=strings.which_to_add.format(book.title),
		reply_markup=reply_markup
	)
	
	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_lists_sent
	)

	await callback.stop_propagation()
	
	return


# Este handler adicionará o livro selecionado a lista de "📚 Lidos" do usuário.
@app.on_callback_query(filters=filters.add_read)
async def handle_add_read(client: Client, callback: CallbackQuery) -> None:
	
	user_library = await database.get_library(callback.from_user.id)
	
	data = CallbackQueryData(callback.data)
	book = library.get(data.id)
	
	# Adicionar o livro a lista de lidos.
	user_library = await database.get_library(callback.from_user.id)
	user_library.remove(book)
	user_library.add(book, 1)
	await user_library.refresh()
	
	reply_markup = create_lists_add(strings, book, read=True)
	
	await client.edit_message_reply_markup(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		reply_markup=reply_markup
	)
	
	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_list_updated
	)

	await callback.stop_propagation()
	
	return


# Este handler adicionará o livro selecionado a lista de "📖 Lendo" do usuário.
@app.on_callback_query(filters=filters.add_reading)
async def handle_add_reading(client: Client, callback: CallbackQuery) -> None:
	
	user_library = await database.get_library(callback.from_user.id)
	
	data = CallbackQueryData(callback.data)
	book = library.get(data.id)
	
	# Adicionar o livro a lista de lendo..
	user_library = await database.get_library(callback.from_user.id)
	user_library.remove(book)
	user_library.add(book, 2)
	await user_library.refresh()
	
	reply_markup = create_lists_add(strings, book, reading=True)
	
	await client.edit_message_reply_markup(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		reply_markup=reply_markup
	)
	
	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_list_updated
	)

	await callback.stop_propagation()
	
	return


# Este handler adicionará o livro selecionado a lista de "🗑 Abandonado" do usuário.
@app.on_callback_query(filters=filters.add_dropped)
async def handle_add_dropped(client: Client, callback: CallbackQuery) -> None:
	
	user_library = await database.get_library(callback.from_user.id)
	
	data = CallbackQueryData(callback.data)
	book = library.get(data.id)
	
	# Adicionar o livro a lista de abandonados..
	user_library = await database.get_library(callback.from_user.id)
	user_library.remove(book)
	user_library.add(book, 3)
	await user_library.refresh()
	
	reply_markup = create_lists_add(strings, book, dropped=True)
	
	await client.edit_message_reply_markup(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		reply_markup=reply_markup
	)
	
	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_list_updated
	)

	await callback.stop_propagation()
	
	return


# Este handler retornará o usuário para a página de informações anterior do livro. 
@app.on_callback_query(filters=filters.back_book)
async def handle_back_book(client: Client, callback: CallbackQuery) -> None:
	
	user_library = await database.get_library(callback.from_user.id)
	
	data = CallbackQueryData(callback.data)
	book = library.get(data.id)
	
	if user_library.has(book, 4):
		reply_markup = create_book_page(strings, book, is_favorited=True)
	else:
		reply_markup = create_book_page(strings, book)
	
	await client.edit_message_caption(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		caption=create_caption(book),
		reply_markup=reply_markup
	)
	
	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_previous_menu
	)

	await callback.stop_propagation()

	return


# Este handler removerá o livro de todas as listas do usuário.
@app.on_callback_query(filters=filters.book_remove)
async def handle_book_remove(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	book = library.get(data.id)
	
	# Remover o livro de todas as listas.
	user_library = await database.get_library(callback.from_user.id)
	user_library.remove(book)
	await user_library.refresh()
	
	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_list_updated
	)

	await callback.stop_propagation()

	return


# Este handler retornará um menu contendo todas as 4 listas do usuário.
@app.on_callback_query(filters=filters.lists)
async def handle_lists(client: Client, callback: CallbackQuery) -> None:
	
	reply_markup = create_lists(strings)
	
	await client.edit_message_text(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		text=strings.your_lists,
		reply_markup=reply_markup
	)
	
	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_your_lists
	)
	
	await callback.stop_propagation()
	
	return


# Este handler retornará o usuário para o menu de boas vindas.
@app.on_callback_query(filters=filters.back_welcome)
async def handle_back_welcome(client: Client, callback: CallbackQuery) -> None:
	
	reply_markup = create_welcome(strings)
	
	await client.edit_message_text(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		text=strings.welcome_message,
		reply_markup=reply_markup
	)
	
	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_previous_menu
	)
	
	await callback.stop_propagation()
	
	return


# Este handler retornará uma lista contendo todos os livros do usuário marcados
# como "📚 Lidos".
@app.on_callback_query(filters=filters.read_list)
async def handle_read_list(client: Client, callback: CallbackQuery) -> None:
	
	user_library = await database.get_library(callback.from_user.id)
	user_books = user_library.get_list(1)

	if not user_books:
		await client.answer_callback_query(
			callback_query_id=callback.id,
			text=strings.dialog_no_books_here
		)
		return

	books = []
	
	for bid in user_books:
		books.append(library.get(bid))
	
	books = library.create_pagination(books)

	if len(books) > 1:
		reply_markup = create_read_list(strings, 0, books[0], next_button=True)
	else:
		reply_markup = create_read_list(strings, 0, books[0])

	await client.send_message(
		chat_id=callback.from_user.id,
		text=strings.your_read_books,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_books_sent
	)
	
	await callback.stop_propagation()
	
	return


# Este handler retornará a página seguinte da lista de livros lidos do usuário.
@app.on_callback_query(filters=filters.next_read)
async def handle_next_read(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	user_library = await database.get_library(callback.from_user.id)
	user_books = user_library.get_list(1)
	
	books = []
	
	for bid in user_books:
		books.append(library.get(bid))
	
	books = library.create_pagination(books)

	next_page = (data.page + 1)
	next_results = books[next_page]
	
	if (next_page + 1) < len(books):
		reply_markup = create_read_list(strings, next_page, next_results, prev_button=True, next_button=True)
	else:
		reply_markup = create_read_list(strings, next_page, next_results, prev_button=True)

	await client.edit_message_reply_markup(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_next_books
	)

	callback.stop_propagation()

	return


# Este handler retornará a página anterior da lista de livros lidos do usuário.
@app.on_callback_query(filters=filters.prev_read)
async def handle_prev_read(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	user_library = await database.get_library(callback.from_user.id)
	user_books = user_library.get_list(1)
	
	books = []
	
	for bid in user_books:
		books.append(library.get(bid))
	
	books = library.create_pagination(books)
	
	prev_page = (data.page - 1)
	prev_results = books[prev_page]

	if prev_page != 0:
		reply_markup = create_read_list(strings, prev_page, prev_results, prev_button=True, next_button=True)
	else:
		reply_markup = create_read_list(strings, prev_page, prev_results, next_button=True)
	
	await client.edit_message_reply_markup(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_prev_books
	)

	await callback.stop_propagation()

	return


# Este handler retornará uma lista contendo todos os livros do usuário marcados
# como "📖 Lendo".
@app.on_callback_query(filters=filters.reading_list)
async def handle_reading_list(client: Client, callback: CallbackQuery) -> None:
	
	user_library = await database.get_library(callback.from_user.id)
	user_books = user_library.get_list(2)

	if not user_books:
		await client.answer_callback_query(
			callback_query_id=callback.id,
			text=strings.dialog_no_books_here
		)
		return

	books = []
	
	for bid in user_books:
		books.append(library.get(bid))
	
	books = library.create_pagination(books)

	if len(books) > 1:
		reply_markup = create_reading_list(strings, 0, books[0], next_button=True)
	else:
		reply_markup = create_reading_list(strings, 0, books[0])

	await client.send_message(
		chat_id=callback.from_user.id,
		text=strings.your_reading_books,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_books_sent
	)
	
	await callback.stop_propagation()
	
	return


# Este handler retornará a página seguinte da lista de livros lendo do usuário.
@app.on_callback_query(filters=filters.next_reading)
async def handle_next_reading(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	user_library = await database.get_library(callback.from_user.id)
	user_books = user_library.get_list(2)
	
	books = []
	
	for bid in user_books:
		books.append(library.get(bid))
	
	books = library.create_pagination(books)

	next_page = (data.page + 1)
	next_results = books[next_page]
	
	if (next_page + 1) < len(books):
		reply_markup = create_reading_list(strings, next_page, next_results, prev_button=True, next_button=True)
	else:
		reply_markup = create_reading_list(strings, next_page, next_results, prev_button=True)

	await client.edit_message_reply_markup(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_next_books
	)

	callback.stop_propagation()

	return


# Este handler retornará a página anterior da lista de livros lendo do usuário.
@app.on_callback_query(filters=filters.prev_reading)
async def handle_prev_reading(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	user_library = await database.get_library(callback.from_user.id)
	user_books = user_library.get_list(2)
	
	books = []
	
	for bid in user_books:
		books.append(library.get(bid))
	
	books = library.create_pagination(books)
	
	prev_page = (data.page - 1)
	prev_results = books[prev_page]

	if prev_page != 0:
		reply_markup = create_reading_list(strings, prev_page, prev_results, prev_button=True, next_button=True)
	else:
		reply_markup = create_reading_list(strings, prev_page, prev_results, next_button=True)
	
	await client.edit_message_reply_markup(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_prev_books
	)

	await callback.stop_propagation()

	return


# Este handler retornará uma lista contendo todos os livros do usuário marcados
# como "🗑 Abandonados".
@app.on_callback_query(filters=filters.dropped_list)
async def handle_dropped_list(client: Client, callback: CallbackQuery) -> None:
	
	user_library = await database.get_library(callback.from_user.id)
	user_books = user_library.get_list(3)

	if not user_books:
		await client.answer_callback_query(
			callback_query_id=callback.id,
			text=strings.dialog_no_books_here
		)
		return

	books = []
	
	for bid in user_books:
		books.append(library.get(bid))
	
	books = library.create_pagination(books)

	if len(books) > 1:
		reply_markup = create_dropped_list(strings, 0, books[0], next_button=True)
	else:
		reply_markup = create_dropped_list(strings, 0, books[0])

	await client.send_message(
		chat_id=callback.from_user.id,
		text=strings.your_dropped_books,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_books_sent
	)
	
	await callback.stop_propagation()
	
	return


# Este handler retornará a página seguinte da lista de livros abandonado do usuário.
@app.on_callback_query(filters=filters.next_dropped)
async def handle_next_dropped(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	user_library = await database.get_library(callback.from_user.id)
	user_books = user_library.get_list(3)
	
	books = []
	
	for bid in user_books:
		books.append(library.get(bid))
	
	books = library.create_pagination(books)

	next_page = (data.page + 1)
	next_results = books[next_page]
	
	if (next_page + 1) < len(books):
		reply_markup = create_dropped_list(strings, next_page, next_results, prev_button=True, next_button=True)
	else:
		reply_markup = create_dropped_list(strings, next_page, next_results, prev_button=True)

	await client.edit_message_reply_markup(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_next_books
	)

	callback.stop_propagation()

	return


# Este handler retornará a página anterior da lista de livros abandonado do usuário.
@app.on_callback_query(filters=filters.prev_dropped)
async def handle_prev_dropped(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	user_library = await database.get_library(callback.from_user.id)
	user_books = user_library.get_list(3)
	
	books = []
	
	for bid in user_books:
		books.append(library.get(bid))
	
	books = library.create_pagination(books)
	
	prev_page = (data.page - 1)
	prev_results = books[prev_page]

	if prev_page != 0:
		reply_markup = create_dropped_list(strings, prev_page, prev_results, prev_button=True, next_button=True)
	else:
		reply_markup = create_dropped_list(strings, prev_page, prev_results, next_button=True)
	
	await client.edit_message_reply_markup(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_prev_books
	)

	await callback.stop_propagation()

	return


# Este handler retornará uma lista contendo todos os livros do usuário marcados
# como "❤️ Favoritos".
@app.on_callback_query(filters=filters.favorite_list)
async def handle_favorite_list(client: Client, callback: CallbackQuery) -> None:
	
	user_library = await database.get_library(callback.from_user.id)
	user_books = user_library.get_list(4)

	if not user_books:
		await client.answer_callback_query(
			callback_query_id=callback.id,
			text=strings.dialog_no_books_here
		)
		return

	books = []
	
	for bid in user_books:
		books.append(library.get(bid))
	
	books = library.create_pagination(books)

	if len(books) > 1:
		reply_markup = create_favorite_list(strings, 0, books[0], next_button=True)
	else:
		reply_markup = create_favorite_list(strings, 0, books[0])

	await client.send_message(
		chat_id=callback.from_user.id,
		text=strings.your_favorite_books,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_books_sent
	)
	
	await callback.stop_propagation()
	
	return


# Este handler retornará a página seguinte da lista de livros favoritos do usuário.
@app.on_callback_query(filters=filters.next_favorite)
async def handle_next_favorite(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	user_library = await database.get_library(callback.from_user.id)
	user_books = user_library.get_list(4)
	
	books = []
	
	for bid in user_books:
		books.append(library.get(bid))
	
	books = library.create_pagination(books)

	next_page = (data.page + 1)
	next_results = books[next_page]
	
	if (next_page + 1) < len(books):
		reply_markup = create_favorite_list(strings, next_page, next_results, prev_button=True, next_button=True)
	else:
		reply_markup = create_favorite_list(strings, next_page, next_results, prev_button=True)

	await client.edit_message_reply_markup(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_next_books
	)

	await callback.stop_propagation()

	return


# Este handler retornará a página anterior da lista de livros favoritos do usuário.
@app.on_callback_query(filters=filters.prev_favorite)
async def handle_prev_favorite(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	user_library = await database.get_library(callback.from_user.id)
	user_books = user_library.get_list(4)
	
	books = []
	
	for bid in user_books:
		books.append(library.get(bid))
	
	books = library.create_pagination(books)
	
	prev_page = (data.page - 1)
	prev_results = books[prev_page]

	if prev_page != 0:
		reply_markup = create_favorite_list(strings, prev_page, prev_results, prev_button=True, next_button=True)
	else:
		reply_markup = create_favorite_list(strings, prev_page, prev_results, next_button=True)
	
	await client.edit_message_reply_markup(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_prev_books
	)

	await callback.stop_propagation()

	return


# Este handler retornará um menu onde é possível navegar por categorias, autores, etc.
@app.on_callback_query(filters=filters.browse)
async def handle_browse(client: Client, callback: CallbackQuery) -> None:
	
	reply_markup = create_browse(strings)
	
	await client.edit_message_text(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		text=strings.browse_message,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_browse_sent
	)

	await callback.stop_propagation()

	return


# Este handler retornará uma lista contendo todas categorias disponíveis.
@app.on_callback_query(filters=filters.browse_categories)
async def handle_browse_categories(client: Client, callback: CallbackQuery) -> None:
	
	categories = library.get_categories()
	
	if len(categories) > 1:
		reply_markup = create_browse_categories(strings, 0, categories[0], next_button=True)
	else:
		reply_markup = create_browse_categories(strings, 0, categories[0])

	await client.send_message(
		chat_id=callback.from_user.id,
		text=strings.categories_list_message,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_categories_sent
	)
	
	await callback.stop_propagation()
	
	return


# Este handler retornará a página seguinte da lista de categorias.
@app.on_callback_query(filters=filters.next_categories)
async def handle_next_categories(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	categories = library.get_categories()

	next_page = (data.page + 1)
	next_categories = categories[next_page]
	
	if (next_page + 1) < len(categories):
		reply_markup = create_browse_categories(strings, next_page, next_categories, prev_button=True, next_button=True)
	else:
		reply_markup = create_browse_categories(strings, next_page, next_categories, prev_button=True)

	await client.edit_message_reply_markup(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_next_categories
	)

	await callback.stop_propagation()

	return


# Este handler retornará a página anterior da lista de categorias.
@app.on_callback_query(filters=filters.prev_categories)
async def handle_prev_categories(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	categories = library.get_categories()
	
	prev_page = (data.page - 1)
	prev_categories = categories[prev_page]

	if prev_page != 0:
		reply_markup = create_browse_categories(strings, prev_page, prev_categories, prev_button=True, next_button=True)
	else:
		reply_markup = create_browse_categories(strings, prev_page, prev_categories, next_button=True)
	
	await client.edit_message_reply_markup(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_prev_categories
	)

	await callback.stop_propagation()

	return


# Este handler retornará uma lista contendo todas is livros presentes na categoria em questão.
@app.on_callback_query(filters=filters.category)
async def handle_category(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	books = library.get_books(category=data.id)
	
	if len(books) > 1:
		reply_markup = create_books_category(strings, data.id, 0, books[0], next_button=True)
	else:
		reply_markup = create_books_category(strings, data.id, 0, books[0])

	await client.send_message(
		chat_id=callback.from_user.id,
		text=strings.books_by_category.format(books[0][0].category),
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_books_sent
	)
	
	await callback.stop_propagation()
	
	return


# Este handler retornará a página seguinte da lista de livros presentes na categoria em questão.
@app.on_callback_query(filters=filters.next_books_category)
async def handle_next_books_category(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	books = library.get_books(category=data.id)

	next_page = (data.page + 1)
	next_books = books[next_page]
	
	if (next_page + 1) < len(books):
		reply_markup = create_books_category(strings, data.id, next_page, next_books, prev_button=True, next_button=True)
	else:
		reply_markup = create_books_category(strings, data.id, next_page, next_books, prev_button=True)

	await client.edit_message_reply_markup(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_next_books
	)

	await callback.stop_propagation()

	return


# Este handler retornará a página anterior da lista de livros presentes na categoria em questão.
@app.on_callback_query(filters=filters.prev_books_category)
async def handle_prev_books_category(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	books = library.get_books(category=data.id)
	
	prev_page = (data.page - 1)
	prev_books = books[prev_page]

	if prev_page != 0:
		reply_markup = create_books_category(strings, data.id, prev_page, prev_books, prev_button=True, next_button=True)
	else:
		reply_markup = create_books_category(strings, data.id, prev_page, prev_books, next_button=True)
	
	await client.edit_message_reply_markup(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_prev_books
	)

	await callback.stop_propagation()

	return



# Este handler retornará uma lista contendo todas categorias disponíveis.
@app.on_callback_query(filters=filters.browse_authors)
async def handle_browse_authors(client: Client, callback: CallbackQuery) -> None:
	
	authors = library.get_authors()
	
	if len(authors) > 1:
		reply_markup = create_browse_authors(strings, 0, authors[0], next_button=True)
	else:
		reply_markup = create_browse_authors(strings, 0, authors[0])

	await client.send_message(
		chat_id=callback.from_user.id,
		text=strings.authors_list_message,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_authors_sent
	)
	
	await callback.stop_propagation()
	
	return


# Este handler retornará a página seguinte da lista de categorias.
@app.on_callback_query(filters=filters.next_authors)
async def handle_next_authors(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	authors = library.get_authors()

	next_page = (data.page + 1)
	next_authors = authors[next_page]
	
	if (next_page + 1) < len(authors):
		reply_markup = create_browse_authors(strings, next_page, next_authors, prev_button=True, next_button=True)
	else:
		reply_markup = create_browse_authors(strings, next_page, next_authors, prev_button=True)

	await client.edit_message_reply_markup(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_next_authors
	)

	await callback.stop_propagation()

	return


# Este handler retornará a página anterior da lista de categorias.
@app.on_callback_query(filters=filters.prev_authors)
async def handle_prev_authors(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	authors = library.get_authors()
	
	prev_page = (data.page - 1)
	prev_authors = authors[prev_page]

	if prev_page != 0:
		reply_markup = create_browse_authors(strings, prev_page, prev_authors, prev_button=True, next_button=True)
	else:
		reply_markup = create_browse_authors(strings, prev_page, prev_authors, next_button=True)
	
	await client.edit_message_reply_markup(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_prev_authors
	)

	await callback.stop_propagation()

	return


# Este handler retornará uma lista contendo todas is livros escritos pelo autor em questão.
@app.on_callback_query(filters=filters.author)
async def handle_author(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	books = library.get_books(author=data.id)
	
	if len(books) > 1:
		reply_markup = create_books_author(strings, data.id, 0, books[0], next_button=True)
	else:
		reply_markup = create_books_author(strings, data.id, 0, books[0])

	await client.send_message(
		chat_id=callback.from_user.id,
		text=strings.books_by_author.format(books[0][0].author),
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_books_sent
	)
	
	await callback.stop_propagation()
	
	return


# Este handler retornará a página seguinte da lista de livros escritos pelo autor em questão.
@app.on_callback_query(filters=filters.next_books_author)
async def handle_next_books_author(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	books = library.get_books(author=data.id)

	next_page = (data.page + 1)
	next_books = books[next_page]
	
	if (next_page + 1) < len(books):
		reply_markup = create_books_author(strings, data.id, next_page, next_books, prev_button=True, next_button=True)
	else:
		reply_markup = create_books_author(strings, data.id, next_page, next_books, prev_button=True)

	await client.edit_message_reply_markup(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_next_books
	)

	await callback.stop_propagation()

	return


# Este handler retornará a página anterior da lista de livros escritos pelo autor em questão.
@app.on_callback_query(filters=filters.prev_books_author)
async def handle_prev_books_author(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	books = library.get_books(author=data.id)
	
	prev_page = (data.page - 1)
	prev_books = books[prev_page]

	if prev_page != 0:
		reply_markup = create_books_author(strings, data.id, prev_page, prev_books, prev_button=True, next_button=True)
	else:
		reply_markup = create_books_author(strings, data.id, prev_page, prev_books, next_button=True)
	
	await client.edit_message_reply_markup(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_prev_books
	)

	await callback.stop_propagation()

	return


# Este handler retornará uma lista contendo todas os narradores disponíveis.
@app.on_callback_query(filters=filters.browse_narrators)
async def handle_browse_narrators(client: Client, callback: CallbackQuery) -> None:
	
	narrators = library.get_narrators()
	
	if len(narrators) > 1:
		reply_markup = create_browse_narrators(strings, 0, narrators[0], next_button=True)
	else:
		reply_markup = create_browse_narrators(strings, 0, narrators[0])

	await client.send_message(
		chat_id=callback.from_user.id,
		text=strings.narrators_list_message,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_narrators_sent
	)
	
	await callback.stop_propagation()
	
	return


# Este handler retornará a página seguinte da lista de narradores..
@app.on_callback_query(filters=filters.next_narrators)
async def handle_next_narrators(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	narrators = library.get_narrators()

	next_page = (data.page + 1)
	next_narrators = narrators[next_page]
	
	if (next_page + 1) < len(narrators):
		reply_markup = create_browse_narrators(strings, next_page, next_narrators, prev_button=True, next_button=True)
	else:
		reply_markup = create_browse_narrators(strings, next_page, next_narrators, prev_button=True)

	await client.edit_message_reply_markup(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_next_narrators
	)

	await callback.stop_propagation()

	return


# Este handler retornará a página anterior da lista de narradores.
@app.on_callback_query(filters=filters.prev_narrators)
async def handle_prev_narrators(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	narrators = library.get_narrators()
	
	prev_page = (data.page - 1)
	prev_narrators = narrators[prev_page]

	if prev_page != 0:
		reply_markup = create_browse_narrators(strings, prev_page, prev_narrators, prev_button=True, next_button=True)
	else:
		reply_markup = create_browse_narrators(strings, prev_page, prev_narrators, next_button=True)
	
	await client.edit_message_reply_markup(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_prev_narrators
	)

	await callback.stop_propagation()

	return


# Este handler retornará uma lista contendo todas is livros narrados pelo narrador em questão.
@app.on_callback_query(filters=filters.narrator)
async def handle_narrator(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	books = library.get_books(narrator=data.id)
	
	if len(books) > 1:
		reply_markup = create_books_narrator(strings, data.id, 0, books[0], next_button=True)
	else:
		reply_markup = create_books_narrator(strings, data.id, 0, books[0])

	await client.send_message(
		chat_id=callback.from_user.id,
		text=strings.books_by_narrator.format(books[0][0].narrator),
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_books_sent
	)
	
	await callback.stop_propagation()
	
	return


# Este handler retornará a página seguinte da lista de livros narrados pelo narrador em questão.
@app.on_callback_query(filters=filters.next_books_narrator)
async def handle_next_books_narrator(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	books = library.get_books(narrator=data.id)

	next_page = (data.page + 1)
	next_books = books[next_page]
	
	if (next_page + 1) < len(books):
		reply_markup = create_books_narrator(strings, data.id, next_page, next_books, prev_button=True, next_button=True)
	else:
		reply_markup = create_books_narrator(strings, data.id, next_page, next_books, prev_button=True)

	await client.edit_message_reply_markup(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_next_books
	)

	await callback.stop_propagation()

	return


# Este handler retornará a página anterior da lista de livros narrados pelo narrador em questão.
@app.on_callback_query(filters=filters.prev_books_narrator)
async def handle_prev_books_narrator(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	books = library.get_books(narrator=data.id)
	
	prev_page = (data.page - 1)
	prev_books = books[prev_page]

	if prev_page != 0:
		reply_markup = create_books_narrator(strings, data.id, prev_page, prev_books, prev_button=True, next_button=True)
	else:
		reply_markup = create_books_narrator(strings, data.id, prev_page, prev_books, next_button=True)
	
	await client.edit_message_reply_markup(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_prev_books
	)

	await callback.stop_propagation()

	return


# Este handler retornará uma lista contendo todas as editoras disponíveis.
@app.on_callback_query(filters=filters.browse_publishers)
async def handle_browse_publishers(client: Client, callback: CallbackQuery) -> None:
	
	publishers = library.get_publishers()
	
	if len(publishers) > 1:
		reply_markup = create_browse_publishers(strings, 0, publishers[0], next_button=True)
	else:
		reply_markup = create_browse_publishers(strings, 0, publishers[0])

	await client.send_message(
		chat_id=callback.from_user.id,
		text=strings.publishers_list_message,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_publishers_sent
	)
	
	await callback.stop_propagation()
	
	return


# Este handler retornará a página seguinte da lista de editoras..
@app.on_callback_query(filters=filters.next_publishers)
async def handle_next_publishers(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	publishers = library.get_publishers()

	next_page = (data.page + 1)
	next_publishers = publishers[next_page]
	
	if (next_page + 1) < len(publishers):
		reply_markup = create_browse_publishers(strings, next_page, next_publishers, prev_button=True, next_button=True)
	else:
		reply_markup = create_browse_publishers(strings, next_page, next_publishers, prev_button=True)

	await client.edit_message_reply_markup(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_next_publishers
	)

	await callback.stop_propagation()

	return


# Este handler retornará a página anterior da lista de editoras.
@app.on_callback_query(filters=filters.prev_publishers)
async def handle_prev_publishers(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	publishers = library.get_publishers()
	
	prev_page = (data.page - 1)
	prev_publishers = publishers[prev_page]

	if prev_page != 0:
		reply_markup = create_browse_publishers(strings, prev_page, prev_publishers, prev_button=True, next_button=True)
	else:
		reply_markup = create_browse_publishers(strings, prev_page, prev_publishers, next_button=True)
	
	await client.edit_message_reply_markup(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_prev_publishers
	)

	await callback.stop_propagation()

	return


# Este handler retornará uma lista contendo todas is livros publicados pela editora em questão.
@app.on_callback_query(filters=filters.publisher)
async def handle_publisher(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	books = library.get_books(publisher=data.id)
	
	if len(books) > 1:
		reply_markup = create_books_publisher(strings, data.id, 0, books[0], next_button=True)
	else:
		reply_markup = create_books_publisher(strings, data.id, 0, books[0])

	await client.send_message(
		chat_id=callback.from_user.id,
		text=strings.books_by_publisher.format(books[0][0].publisher),
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_books_sent
	)
	
	await callback.stop_propagation()
	
	return


# Este handler retornará a página seguinte da lista de livros publicados pela editora em questão.
@app.on_callback_query(filters=filters.next_books_publisher)
async def handle_next_books_publisher(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	books = library.get_books(publisher=data.id)

	next_page = (data.page + 1)
	next_books = books[next_page]
	
	if (next_page + 1) < len(books):
		reply_markup = create_books_publisher(strings, data.id, next_page, next_books, prev_button=True, next_button=True)
	else:
		reply_markup = create_books_publisher(strings, data.id, next_page, next_books, prev_button=True)

	await client.edit_message_reply_markup(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_next_books
	)

	await callback.stop_propagation()

	return


# Este handler retornará a página anterior da lista de livros publicados pela editora em questão.
@app.on_callback_query(filters=filters.prev_books_publisher)
async def handle_prev_books_publisher(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	books = library.get_books(publisher=data.id)
	
	prev_page = (data.page - 1)
	prev_books = books[prev_page]

	if prev_page != 0:
		reply_markup = create_books_publisher(strings, data.id, prev_page, prev_books, prev_button=True, next_button=True)
	else:
		reply_markup = create_books_publisher(strings, data.id, prev_page, prev_books, next_button=True)
	
	await client.edit_message_reply_markup(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_prev_books
	)

	await callback.stop_propagation()

	return


# Este handler retornará uma lista contendo todas os tipos disponíveis.
@app.on_callback_query(filters=filters.browse_types)
async def handle_browse_types(client: Client, callback: CallbackQuery) -> None:
	
	types = library.get_types()
	
	if len(types) > 1:
		reply_markup = create_browse_types(strings, 0, types[0], next_button=True)
	else:
		reply_markup = create_browse_types(strings, 0, types[0])

	await client.send_message(
		chat_id=callback.from_user.id,
		text=strings.types_list_message,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_types_sent
	)
	
	await callback.stop_propagation()
	
	return


# Este handler retornará a página seguinte da lista de tipos..
@app.on_callback_query(filters=filters.next_types)
async def handle_next_types(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	types = library.get_types()

	next_page = (data.page + 1)
	next_types = types[next_page]
	
	if (next_page + 1) < len(types):
		reply_markup = create_browse_types(strings, next_page, next_types, prev_button=True, next_button=True)
	else:
		reply_markup = create_browse_types(strings, next_page, next_types, prev_button=True)

	await client.edit_message_reply_markup(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_next_types
	)

	await callback.stop_propagation()

	return


# Este handler retornará a página anterior da lista de tipos.
@app.on_callback_query(filters=filters.prev_types)
async def handle_prev_types(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	types = library.get_types()
	
	prev_page = (data.page - 1)
	prev_types = types[prev_page]

	if prev_page != 0:
		reply_markup = create_browse_types(strings, prev_page, prev_types, prev_button=True, next_button=True)
	else:
		reply_markup = create_browse_types(strings, prev_page, prev_types, next_button=True)
	
	await client.edit_message_reply_markup(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_prev_types
	)

	await callback.stop_propagation()

	return


# Este handler retornará uma lista contendo todas is livros do tipo em questão.
@app.on_callback_query(filters=filters.type)
async def handle_type(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	books = library.get_books(book_type=data.id)
	
	if len(books) > 1:
		reply_markup = create_books_type(strings, data.id, 0, books[0], next_button=True)
	else:
		reply_markup = create_books_type(strings, data.id, 0, books[0])

	await client.send_message(
		chat_id=callback.from_user.id,
		text=strings.books_by_type.format(books[0][0].type),
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_books_sent
	)
	
	await callback.stop_propagation()
	
	return


# Este handler retornará a página seguinte da lista de livros do tipo em questão.
@app.on_callback_query(filters=filters.next_books_type)
async def handle_next_books_type(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	books = library.get_books(book_type=data.id)

	next_page = (data.page + 1)
	next_books = books[next_page]
	
	if (next_page + 1) < len(books):
		reply_markup = create_books_type(strings, data.id, next_page, next_books, prev_button=True, next_button=True)
	else:
		reply_markup = create_books_type(strings, data.id, next_page, next_books, prev_button=True)

	await client.edit_message_reply_markup(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_next_books
	)

	await callback.stop_propagation()

	return


# Este handler retornará a página anterior da lista de livros do tipo em questão.
@app.on_callback_query(filters=filters.prev_books_type)
async def handle_prev_books_type(client: Client, callback: CallbackQuery) -> None:
	
	data = CallbackQueryData(callback.data)
	
	books = library.get_books(book_type=data.id)
	
	prev_page = (data.page - 1)
	prev_books = books[prev_page]

	if prev_page != 0:
		reply_markup = create_books_type(strings, data.id, prev_page, prev_books, prev_button=True, next_button=True)
	else:
		reply_markup = create_books_type(strings, data.id, prev_page, prev_books, next_button=True)
	
	await client.edit_message_reply_markup(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_prev_books
	)

	await callback.stop_propagation()

	return


# Este handler retornará uma lista contendo todos os comandos do bot.
@app.on_callback_query(filters=filters.commands)
async def handle_commands(client: Client, callback: CallbackQuery) -> None:
	
	reply_markup = create_commands(strings)
	
	await client.edit_message_text(
		chat_id=callback.from_user.id,
		message_id=callback.message.message_id,
		text=strings.commands,
		reply_markup=reply_markup
	)

	await client.answer_callback_query(
		callback_query_id=callback.id,
		text=strings.dialog_commands_loaded
	)

	await callback.stop_propagation()

	return

	

# Criamos nossa biblioteca.
library = Library(
	categories,
	authors,
	narrators,
	publishers,
	types
)

# Adicionamos todos os livros catalogados a nossa biblioteca.
for book in books:
	library.append(Book(book))

# Strings para diálogos e textos de botões.
strings = Strings(strings)

# Usamos esse objeto criar ou excluir informações sobre os usuários.
database = Database(ASYNCPG_OPTIONS)

loop = asyncio.get_event_loop()
loop.run_until_complete(database.initialize())

app.run()