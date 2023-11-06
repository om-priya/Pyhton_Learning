from bs4 import BeautifulSoup

from books_locators.all_books_page import AllBooksPageLocators
from books_parsers.parser import BookParser


class AllBooksPage:
    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, "html.parser")

    @property
    def books_result(self):
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)]
