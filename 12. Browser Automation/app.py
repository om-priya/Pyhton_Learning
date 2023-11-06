from selenium import webdriver
from pages.quote_page import QuotesPage

browser = webdriver.Firefox()
browser.get("https://quotes.toscrape.com/search.aspx")
new_page = QuotesPage(browser)

my_author = input("Enter the name of author: ")
new_page.select_author(my_author)

my_tag = input("Enter the tag: ")
new_page.select_tag(my_tag)
