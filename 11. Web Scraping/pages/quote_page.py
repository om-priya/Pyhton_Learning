from selenium.webdriver.common.by import By
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
