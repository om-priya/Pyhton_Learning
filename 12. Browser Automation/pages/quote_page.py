from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from parser.quote import QuoteParser
from locators.quote_page_locator import QuotePageLocator


class QuotesPage:
    def __init__(self, browser) -> None:
        self.browser = browser

    @property
    def quotes(self):
        return [
            QuoteParser(e)
            for e in self.browser.find_elements(
                By.CSS_SELECTOR, QuotePageLocator.QUOTE_PAGE_LOCATOR
            )
        ]

    @property
    def author_dropdown(self):
        element = self.browser.find_element(
            By.CSS_SELECTOR, QuotePageLocator.AUTHOR_TAG_LOCATOR
        )
        return Select(element)

    @property
    def tag_dropdown(self):
        element = self.browser.find_element(
            By.CSS_SELECTOR, QuotePageLocator.TAG_LOCATOR
        )
        return Select(element)

    def select_author(self, author_name):
        self.tag_dropdown.select_by_visible_text(author_name)

    def select_tag(self, tag_name):
        self.tag_dropdown.options(tag_name)
