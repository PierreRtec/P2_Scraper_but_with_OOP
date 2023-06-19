from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from scraping_app.models.book import Book


class Category:
    def __init__(self, url):
        self.url = url
        self.scrape()

    def scrape(self):
        self.books = []
        link_urls = []
        print(link_urls)
        response = requests.get(self.url)
        if response.ok:
            soup = BeautifulSoup(response.content, "html.parser")
            all_urls_book = soup.select("h3 a")
            for link in all_urls_book:
                book = Book(urljoin(self.url, link["href"]))
                self.books.append(book)

            # Y a-t-il une page suivante ?
            next_button = soup.select_one(".next a")
            if next_button is not None:
                # Oui, il y a un bouton next -> on répète la même fonction sur la page
                self.books += Category(urljoin(self.url, next_button["href"])).books
