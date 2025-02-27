from abc import ABC, abstractmethod
from colorama import Fore, Style
from typing import List
from logger_config import logger


class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def get_books(self) -> List[Book]:
        pass


class Library(LibraryInterface):
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        if not book.title.strip():
            logger.error("Book title cannot be empty.")
            return
        if any(b.title == book.title for b in self.books):
            logger.error(
                f"Book with title '{book.title}' already exists. Please add another title."
            )
            return
        self.books.append(book)
        logger.info(f"Book added: {book}")

    def remove_book(self, title: str) -> None:
        if not title.strip():
            logger.error("Book title cannot be empty.")
            return
        if not any(book.title == title for book in self.books):
            logger.error(f"Book with title '{title}' not found. Cannot remove.")
            return
        self.books = [book for book in self.books if book.title != title]
        logger.info(f"Book removed: {title}")

    def get_books(self) -> List[Book]:
        return self.books


class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: int) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        books = self.library.get_books()
        if books:
            for book in books:
                logger.info(book)
        else:
            logger.info("No books in the library.")


def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = (
            input(
                Fore.CYAN
                + "Enter command (add, remove, show, exit): "
                + Style.RESET_ALL
            )
            .strip()
            .lower()
        )

        if command not in {"add", "remove", "show", "exit"}:
            logger.warning("Invalid command. Please try again.")
            continue

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input(
                    Fore.CYAN + "Enter book title to remove: " + Style.RESET_ALL
                ).strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break


if __name__ == "__main__":
    main()
