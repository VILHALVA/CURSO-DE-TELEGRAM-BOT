from pyrogram import Client
from pyrogram.filters import command, private
from pyrogram.types import CallbackQuery

from .types.callback import CallbackQueryData


def book_page(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "book")


def next_resuts(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "next_resuts")


def prev_resuts(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "prev_resuts")


def delete_message(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "delete_message")


def favorite(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "favorite")


def unfavorite(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "unfavorite")


def get_document(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "get_document")


def list_add(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "list_add")


def add_read(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "add_read")


def add_reading(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "add_reading")


def add_dropped(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "add_dropped")


def back_book(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "back_book")


def book_remove(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "book_remove")


def lists(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "lists")


def read_list(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "read_list")


def reading_list(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "reading_list")


def dropped_list(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "dropped_list")


def favorite_list(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "favorite_list")


def next_read(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "next_read")


def prev_read(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "prev_read")


def next_reading(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "next_reading")


def prev_reading(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "prev_reading")


def next_dropped(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "next_dropped")


def prev_dropped(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "prev_dropped")


def next_favorite(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "next_favorite")


def prev_favorite(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "prev_favorite")


def back_welcome(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "back_welcome")


def browse(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "browse")


def browse_categories(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "browse_categories")


def next_categories(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "next_categories")


def prev_categories(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "prev_categories")


def category(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "category")


def prev_books_category(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "prev_books_category")


def next_books_category(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "next_books_category")


def browse_authors(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "browse_authors")


def next_authors(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "next_authors")


def prev_authors(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "prev_authors")


def author(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "author")


def prev_books_author(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "prev_books_author")


def next_books_author(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "next_books_author")


def browse_narrators(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "browse_narrators")


def next_narrators(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "next_narrators")


def prev_narrators(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "prev_narrators")


def narrator(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "narrator")


def prev_books_narrator(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "prev_books_narrator")


def next_books_narrator(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "next_books_narrator")


def browse_publishers(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "browse_publishers")


def next_publishers(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "next_publishers")


def prev_publishers(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "prev_publishers")


def publisher(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "publisher")


def prev_books_publisher(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "prev_books_publisher")


def next_books_publisher(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "next_books_publisher")


def browse_types(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "browse_types")


def next_types(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "next_types")


def prev_types(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "prev_types")


def type(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "type")


def next_books_type(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == 'next_books_type')


def prev_books_type(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == 'prev_books_type')


def publisher(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "publisher")


def prev_books_publisher(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "prev_books_publisher")


def next_books_publisher(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "next_books_publisher")


def new_random(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "new_random")


def commands(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "commands")


def delete(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "delete")


def delete_account(client: Client, callback: CallbackQuery) -> bool:
	data = CallbackQueryData(callback.data)
	return (data.action == "delete_account")


