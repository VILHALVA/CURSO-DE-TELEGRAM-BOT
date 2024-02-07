import json

from pyrogram.types import (
	InlineKeyboardButton, InlineKeyboardMarkup
)


def create_welcome(strings):
	
	inline_keyboard = []
	
	callback_data = dict(action="lists")
	inline_keyboard.append([InlineKeyboardButton(text=strings.button_my_library, callback_data=json.dumps(callback_data))])
	
	callback_data = dict(action="browse")
	inline_keyboard.append([InlineKeyboardButton(text=strings.button_browse, callback_data=json.dumps(callback_data))])
	
	callback_data = dict(action="commands")
	inline_keyboard.append([InlineKeyboardButton(text=strings.button_commands, callback_data=json.dumps(callback_data))])
	
	return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def create_browse(strings):
	
	inline_keyboard = []
	
	callback_data = dict(action="browse_categories")
	inline_keyboard.append([InlineKeyboardButton(text=strings.button_browse_categories, callback_data=json.dumps(callback_data))])
	
	callback_data = dict(action="browse_types")
	inline_keyboard.append([InlineKeyboardButton(text=strings.button_browse_types, callback_data=json.dumps(callback_data))])
	
	callback_data = dict(action="browse_authors")
	inline_keyboard.append([InlineKeyboardButton(text=strings.button_browse_authors, callback_data=json.dumps(callback_data))])
	
	callback_data = dict(action="browse_narrators")
	inline_keyboard.append([InlineKeyboardButton(text=strings.button_browse_narrators, callback_data=json.dumps(callback_data))])
	
	callback_data = dict(action="browse_publishers")
	inline_keyboard.append([InlineKeyboardButton(text=strings.button_browse_publishers, callback_data=json.dumps(callback_data))])
	
	callback_data = dict(action="back_welcome")
	inline_keyboard.append([InlineKeyboardButton(text=strings.button_go_back, callback_data=json.dumps(callback_data))])
	
	return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def create_my_library(strings):
	
	inline_keyboard = []
	
	callback_data = dict(action="my_favorites")
	inline_keyboard.append([InlineKeyboardButton(text=strings.button_my_favorites, callback_data=json.dumps(callback_data))])
	
	callback_data = dict(action="my_read")
	inline_keyboard.append([InlineKeyboardButton(text=strings.button_my_read, callback_data=json.dumps(callback_data))])
	
	callback_data = dict(action="my_reading")
	inline_keyboard.append([InlineKeyboardButton(text=strings.button_my_reading, callback_data=json.dumps(callback_data))])
	
	callback_data = dict(action="my_dropped")
	inline_keyboard.append([InlineKeyboardButton(text=strings.button_my_dropped, callback_data=json.dumps(callback_data))])
	
	return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def create_results(
	strings,
	results,
	single_id,
	page,
	prev_button=False,
	next_button=False
):
	
	inline_keyboard = []
	
	for book in results:
		if book is None:
			break
		
		callback_data = dict(action="book", id=book.message)
		inline_keyboard.append([InlineKeyboardButton(text=book.title, callback_data=json.dumps(callback_data))])
	
	pagination_keyboards = []
	
	if prev_button:
		callback_data = dict(action="prev_resuts", id=single_id, page=page)
		pagination_keyboards.append(InlineKeyboardButton(text=strings.previous_page_button, callback_data=json.dumps(callback_data)))
	
	if next_button:
		callback_data = dict(action="next_resuts", id=single_id, page=page)
		pagination_keyboards.append(InlineKeyboardButton(text=strings.next_page_button, callback_data=json.dumps(callback_data)))
	
	inline_keyboard.append(pagination_keyboards)
	
	return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def create_book_page(strings, book, is_favorited=False):
	
	inline_keyboard = []
	
	callback_data = dict(action="get_document", id=book.message)
	
	if book.type == "Audiobook":
		inline_keyboard.append([InlineKeyboardButton(text=strings.button_listen_book, callback_data=json.dumps(callback_data))])
	else:
		inline_keyboard.append([InlineKeyboardButton(text=strings.button_read_book, callback_data=json.dumps(callback_data))])
	
	callback_data = dict(action="list_add", id=book.message)
	inline_keyboard.append([InlineKeyboardButton(text=strings.button_add_library, callback_data=json.dumps(callback_data))])
	
	if is_favorited:
		callback_data = dict(action="unfavorite", id=book.message)
		inline_keyboard.append([InlineKeyboardButton(text=strings.button_unfavorite, callback_data=json.dumps(callback_data))])
	else:
		callback_data = dict(action="favorite", id=book.message)
		inline_keyboard.append([InlineKeyboardButton(text=strings.button_favorite, callback_data=json.dumps(callback_data))])
	
	callback_data = dict(action="book_remove", id=book.message)
	inline_keyboard.append([InlineKeyboardButton(text=strings.button_remove, callback_data=json.dumps(callback_data))])
	
	callback_data = dict(action="delete_message")
	inline_keyboard.append([InlineKeyboardButton(text=strings.button_quit, callback_data=json.dumps(callback_data))])
	
	return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def create_lists_add(strings, book, read=False, reading=False, dropped=False):
	
	inline_keyboard = []
	
	callback_data = dict(action="add_read", id=book.message)
	
	if read:
		inline_keyboard.append([InlineKeyboardButton(text=strings.button_my_read_added, callback_data=json.dumps(callback_data))])
	else:
		inline_keyboard.append([InlineKeyboardButton(text=strings.button_my_read, callback_data=json.dumps(callback_data))])
	
	callback_data = dict(action="add_reading", id=book.message)
	
	if reading:
		inline_keyboard.append([InlineKeyboardButton(text=strings.button_my_reading_added, callback_data=json.dumps(callback_data))])
	else:
		inline_keyboard.append([InlineKeyboardButton(text=strings.button_my_reading, callback_data=json.dumps(callback_data))])
	
	callback_data = dict(action="add_dropped", id=book.message)
	
	if dropped:
		inline_keyboard.append([InlineKeyboardButton(text=strings.button_my_dropped_added, callback_data=json.dumps(callback_data))])
	else:
		inline_keyboard.append([InlineKeyboardButton(text=strings.button_my_dropped, callback_data=json.dumps(callback_data))])
	
	callback_data = dict(action="back_book", id=book.message)
	
	inline_keyboard.append([InlineKeyboardButton(text=strings.button_go_back, callback_data=json.dumps(callback_data))])
	
	return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def create_lists(strings):
	
	inline_keyboard = []
	
	callback_data = dict(action="read_list")
	inline_keyboard.append([InlineKeyboardButton(text=strings.button_my_read, callback_data=json.dumps(callback_data))])
	
	callback_data = dict(action="reading_list")
	inline_keyboard.append([InlineKeyboardButton(text=strings.button_my_reading, callback_data=json.dumps(callback_data))])
	
	callback_data = dict(action="dropped_list")
	inline_keyboard.append([InlineKeyboardButton(text=strings.button_my_dropped, callback_data=json.dumps(callback_data))])
	
	callback_data = dict(action="favorite_list")
	inline_keyboard.append([InlineKeyboardButton(text=strings.button_my_favorites, callback_data=json.dumps(callback_data))])
	
	callback_data = dict(action="back_welcome")
	inline_keyboard.append([InlineKeyboardButton(text=strings.button_go_back, callback_data=json.dumps(callback_data))])
	
	return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def create_read_list(strings, page, books, prev_button=False, next_button=False):
	
	inline_keyboard = []
	
	for book in books:
		if book is None:
			break
		
		callback_data = dict(action="book", id=book.message)
		inline_keyboard.append([InlineKeyboardButton(text=book.title, callback_data=json.dumps(callback_data))])
	
	pagination_keyboards = []
	
	if prev_button:
		callback_data = dict(action="prev_read", page=page)
		pagination_keyboards.append(InlineKeyboardButton(text=strings.previous_page_button, callback_data=json.dumps(callback_data)))
	
	if next_button:
		callback_data = dict(action="next_read", page=page)
		pagination_keyboards.append(InlineKeyboardButton(text=strings.next_page_button, callback_data=json.dumps(callback_data)))
	
	inline_keyboard.append(pagination_keyboards)
	
	return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def create_reading_list(strings, page, books, prev_button=False, next_button=False):
	
	inline_keyboard = []
	
	for book in books:
		if book is None:
			break
		
		callback_data = dict(action="book", id=book.message)
		inline_keyboard.append([InlineKeyboardButton(text=book.title, callback_data=json.dumps(callback_data))])
	
	pagination_keyboards = []
	
	if prev_button:
		callback_data = dict(action="prev_reading", page=page)
		pagination_keyboards.append(InlineKeyboardButton(text=strings.previous_page_button, callback_data=json.dumps(callback_data)))
	
	if next_button:
		callback_data = dict(action="next_reading", page=page)
		pagination_keyboards.append(InlineKeyboardButton(text=strings.next_page_button, callback_data=json.dumps(callback_data)))
	
	inline_keyboard.append(pagination_keyboards)
	
	return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def create_dropped_list(strings, page, books, prev_button=False, next_button=False):
	
	inline_keyboard = []
	
	for book in books:
		if book is None:
			break
		
		callback_data = dict(action="book", id=book.message)
		inline_keyboard.append([InlineKeyboardButton(text=book.title, callback_data=json.dumps(callback_data))])
	
	pagination_keyboards = []
	
	if prev_button:
		callback_data = dict(action="prev_dropped", page=page)
		pagination_keyboards.append(InlineKeyboardButton(text=strings.previous_page_button, callback_data=json.dumps(callback_data)))
	
	if next_button:
		callback_data = dict(action="next_dropped", page=page)
		pagination_keyboards.append(InlineKeyboardButton(text=strings.next_page_button, callback_data=json.dumps(callback_data)))
	
	inline_keyboard.append(pagination_keyboards)
	
	return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def create_favorite_list(strings, page, books, prev_button=False, next_button=False):
	
	inline_keyboard = []
	
	for book in books:
		if book is None:
			break
		
		callback_data = dict(action="book", id=book.message)
		inline_keyboard.append([InlineKeyboardButton(text=book.title, callback_data=json.dumps(callback_data))])
	
	pagination_keyboards = []
	
	if prev_button:
		callback_data = dict(action="prev_favorite", page=page)
		pagination_keyboards.append(InlineKeyboardButton(text=strings.previous_page_button, callback_data=json.dumps(callback_data)))
	
	if next_button:
		callback_data = dict(action="next_favorite", page=page)
		pagination_keyboards.append(InlineKeyboardButton(text=strings.next_page_button, callback_data=json.dumps(callback_data)))
	
	inline_keyboard.append(pagination_keyboards)
	
	return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def create_browse_categories(
	strings,
	page,
	categories,
	prev_button=False,
	next_button=False
):
	
	inline_keyboard = []
	
	for index, name in categories:
		if index is None:
			break
		
		callback_data = dict(action="category", id=index)
		inline_keyboard.append([InlineKeyboardButton(text=name, callback_data=json.dumps(callback_data))])
	
	pagination_keyboards = []
	
	if prev_button:
		callback_data = dict(action="prev_categories", page=page)
		pagination_keyboards.append(InlineKeyboardButton(text=strings.previous_page_button, callback_data=json.dumps(callback_data)))
	
	if next_button:
		callback_data = dict(action="next_categories", page=page)
		pagination_keyboards.append(InlineKeyboardButton(text=strings.next_page_button, callback_data=json.dumps(callback_data)))
	
	inline_keyboard.append(pagination_keyboards)
	
	return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def create_books_category(
	strings,
	category,
	page,
	books,
	prev_button=False,
	next_button=False
):
	
	inline_keyboard = []
	
	for book in books:
		if book is None:
			break
		
		callback_data = dict(action="book", id=book.message)
		inline_keyboard.append([InlineKeyboardButton(text=book.title, callback_data=json.dumps(callback_data))])
	
	pagination_keyboards = []
	
	if prev_button:
		callback_data = dict(action="prev_books_category", page=page, id=category)
		pagination_keyboards.append(InlineKeyboardButton(text=strings.previous_page_button, callback_data=json.dumps(callback_data)))
	
	if next_button:
		callback_data = dict(action="next_books_category", page=page, id=category)
		pagination_keyboards.append(InlineKeyboardButton(text=strings.next_page_button, callback_data=json.dumps(callback_data)))
	
	inline_keyboard.append(pagination_keyboards)
	
	return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def create_browse_authors(
	strings,
	page,
	authors,
	prev_button=False,
	next_button=False
):
	
	inline_keyboard = []
	
	for index, name in authors:
		if index is None:
			break
		
		callback_data = dict(action="author", id=index)
		inline_keyboard.append([InlineKeyboardButton(text=name, callback_data=json.dumps(callback_data))])
	
	pagination_keyboards = []
	
	if prev_button:
		callback_data = dict(action="prev_authors", page=page)
		pagination_keyboards.append(InlineKeyboardButton(text=strings.previous_page_button, callback_data=json.dumps(callback_data)))
	
	if next_button:
		callback_data = dict(action="next_authors", page=page)
		pagination_keyboards.append(InlineKeyboardButton(text=strings.next_page_button, callback_data=json.dumps(callback_data)))
	
	inline_keyboard.append(pagination_keyboards)
	
	return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def create_books_author(
	strings,
	author,
	page,
	books,
	prev_button=False,
	next_button=False
):
	
	inline_keyboard = []
	
	for book in books:
		if book is None:
			break
		
		callback_data = dict(action="book", id=book.message)
		inline_keyboard.append([InlineKeyboardButton(text=book.title, callback_data=json.dumps(callback_data))])
	
	pagination_keyboards = []
	
	if prev_button:
		callback_data = dict(action="prev_books_author", page=page, id=author)
		pagination_keyboards.append(InlineKeyboardButton(text=strings.previous_page_button, callback_data=json.dumps(callback_data)))
	
	if next_button:
		callback_data = dict(action="next_books_author", page=page, id=author)
		pagination_keyboards.append(InlineKeyboardButton(text=strings.next_page_button, callback_data=json.dumps(callback_data)))
	
	inline_keyboard.append(pagination_keyboards)
	
	return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def create_browse_narrators(
	strings,
	page,
	narrators,
	prev_button=False,
	next_button=False
):
	
	inline_keyboard = []
	
	for index, name in narrators:
		if index is None:
			break
		
		callback_data = dict(action="narrator", id=index)
		inline_keyboard.append([InlineKeyboardButton(text=name, callback_data=json.dumps(callback_data))])
	
	pagination_keyboards = []
	
	if prev_button:
		callback_data = dict(action="prev_narrators", page=page)
		pagination_keyboards.append(InlineKeyboardButton(text=strings.previous_page_button, callback_data=json.dumps(callback_data)))
	
	if next_button:
		callback_data = dict(action="next_narrators", page=page)
		pagination_keyboards.append(InlineKeyboardButton(text=strings.next_page_button, callback_data=json.dumps(callback_data)))
	
	inline_keyboard.append(pagination_keyboards)
	
	return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def create_books_narrator(
	strings,
	narrator,
	page,
	books,
	prev_button=False,
	next_button=False
):
	
	inline_keyboard = []
	
	for book in books:
		if book is None:
			break
		
		callback_data = dict(action="book", id=book.message)
		inline_keyboard.append([InlineKeyboardButton(text=book.title, callback_data=json.dumps(callback_data))])
	
	pagination_keyboards = []
	
	if prev_button:
		callback_data = dict(action="prev_books_narrator", page=page, id=narrator)
		pagination_keyboards.append(InlineKeyboardButton(text=strings.previous_page_button, callback_data=json.dumps(callback_data)))
	
	if next_button:
		callback_data = dict(action="next_books_narrator", page=page, id=narrator)
		pagination_keyboards.append(InlineKeyboardButton(text=strings.next_page_button, callback_data=json.dumps(callback_data)))
	
	inline_keyboard.append(pagination_keyboards)
	
	return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def create_browse_publishers(
	strings,
	page,
	publishers,
	prev_button=False,
	next_button=False
):
	
	inline_keyboard = []
	
	for index, name in publishers:
		if index is None:
			break
		
		callback_data = dict(action="publisher", id=index)
		inline_keyboard.append([InlineKeyboardButton(text=name, callback_data=json.dumps(callback_data))])
	
	pagination_keyboards = []
	
	if prev_button:
		callback_data = dict(action="prev_publishers", page=page)
		pagination_keyboards.append(InlineKeyboardButton(text=strings.previous_page_button, callback_data=json.dumps(callback_data)))
	
	if next_button:
		callback_data = dict(action="next_publishers", page=page)
		pagination_keyboards.append(InlineKeyboardButton(text=strings.next_page_button, callback_data=json.dumps(callback_data)))
	
	inline_keyboard.append(pagination_keyboards)
	
	return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def create_books_publisher(
	strings,
	publisher,
	page,
	books,
	prev_button=False,
	next_button=False
):
	
	inline_keyboard = []
	
	for book in books:
		if book is None:
			break
		
		callback_data = dict(action="book", id=book.message)
		inline_keyboard.append([InlineKeyboardButton(text=book.title, callback_data=json.dumps(callback_data))])
	
	pagination_keyboards = []
	
	if prev_button:
		callback_data = dict(action="prev_books_publisher", page=page, id=publisher)
		pagination_keyboards.append(InlineKeyboardButton(text=strings.previous_page_button, callback_data=json.dumps(callback_data)))
	
	if next_button:
		callback_data = dict(action="next_books_publisher", page=page, id=publisher)
		pagination_keyboards.append(InlineKeyboardButton(text=strings.next_page_button, callback_data=json.dumps(callback_data)))
	
	inline_keyboard.append(pagination_keyboards)
	
	return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def create_browse_types(
	strings,
	page,
	types,
	prev_button=False,
	next_button=False
):
	
	inline_keyboard = []
	
	for index, name in types:
		if index is None:
			break
		
		callback_data = dict(action="type", id=index)
		inline_keyboard.append([InlineKeyboardButton(text=name, callback_data=json.dumps(callback_data))])
	
	pagination_keyboards = []
	
	if prev_button:
		callback_data = dict(action="prev_types", page=page)
		pagination_keyboards.append(InlineKeyboardButton(text=strings.previous_page_button, callback_data=json.dumps(callback_data)))
	
	if next_button:
		callback_data = dict(action="next_types", page=page)
		pagination_keyboards.append(InlineKeyboardButton(text=strings.next_page_button, callback_data=json.dumps(callback_data)))
	
	inline_keyboard.append(pagination_keyboards)
	
	return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def create_books_type(
	strings,
	type,
	page,
	books,
	prev_button=False,
	next_button=False
):
	
	inline_keyboard = []
	
	for book in books:
		if book is None:
			break
		
		callback_data = dict(action="book", id=book.message)
		inline_keyboard.append([InlineKeyboardButton(text=book.title, callback_data=json.dumps(callback_data))])
	
	pagination_keyboards = []
	
	if prev_button:
		callback_data = dict(action="prev_books_type", page=page, id=type)
		pagination_keyboards.append(InlineKeyboardButton(text=strings.previous_page_button, callback_data=json.dumps(callback_data)))
	
	if next_button:
		callback_data = dict(action="next_books_type", page=page, id=type)
		pagination_keyboards.append(InlineKeyboardButton(text=strings.next_page_button, callback_data=json.dumps(callback_data)))
	
	inline_keyboard.append(pagination_keyboards)
	
	return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def create_random(strings, book):
	
	inline_keyboard = []
	
	callback_data = dict(action="book", id=book.message)
	inline_keyboard.append([InlineKeyboardButton(text=strings.button_go_book, callback_data=json.dumps(callback_data))])
	
	callback_data = dict(action="new_random")
	inline_keyboard.append([InlineKeyboardButton(text=strings.button_new_random, callback_data=json.dumps(callback_data))])
	
	callback_data = dict(action="delete_message")
	inline_keyboard.append([InlineKeyboardButton(text=strings.button_quit, callback_data=json.dumps(callback_data))])
	
	return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def create_commands(strings):
	
	inline_keyboard = []
	
	callback_data = dict(action="back_welcome")
	inline_keyboard.append([InlineKeyboardButton(text=strings.button_go_back, callback_data=json.dumps(callback_data))])
	
	return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def create_delete(strings):
	
	inline_keyboard = []
	
	callback_data = dict(action="delete_account")
	inline_keyboard.append([InlineKeyboardButton(text=strings.button_delete_data, callback_data=json.dumps(callback_data))])
	
	return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)

