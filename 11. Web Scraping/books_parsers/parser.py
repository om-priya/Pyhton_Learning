import re

from books_locators.books_locators import BookLocators


class BookParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f"hello {self.get_title} {self.get_price}"

    @property
    def get_title(self):
        locator = BookLocators.TITLE_LOCATOR
        single_title = self.parent.select_one(locator)
        return single_title.string

    @property
    def get_price(self):
        locator = BookLocators.PRICE_LOCATOR
        price = self.parent.select_one(locator).string

        pattern = "£([0-9]+\.[0-9]+)"
        matcher = re.search(pattern, price)
        return float(matcher.group(1))
