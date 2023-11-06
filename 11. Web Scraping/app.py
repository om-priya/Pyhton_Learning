from selenium import webdriver
from pages.quote_page import QuotesPage

browser = webdriver.Firefox()
browser.get("https://quotes.toscrape.com/")

new_page = QuotesPage(browser)

for quote in new_page.quotes:
    print(quote)
