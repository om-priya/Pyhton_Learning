from locators.quote_locator import QuoteLocator
from selenium.webdriver.common.by import By


class QuoteParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f"{self.get_quote} || {self.get_author}"

    @property
    def get_quote(self):
        locator = QuoteLocator.QUOTE
        single_quote = self.parent.find_elements(By.CSS_SELECTOR, locator)
        # print(single_quote)
        for quote in single_quote:
            return quote.text

    @property
    def get_author(self):
        locator = QuoteLocator.AUTHOR
        author = self.parent.find_elements(By.CSS_SELECTOR, locator)
        for auth in author:
            return auth.text
