import requests


from books_pages.all_books_page import AllBooksPage

HTML_PAGE = requests.get("https://books.toscrape.com/").content

page = AllBooksPage(HTML_PAGE)

print(page.books_result)
