from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from slugify import slugify


class Book:
    def __init__(self, url):
        self.url = url
        self.scrape()

    def scrape(self):
        response = requests.get(self.url)
        if response.ok:
            soup = BeautifulSoup(response.content, "html.parser")
            self.title = soup.select_one(".product_main h1").text.strip()
            print(self.title)
            self.description = self.product_description(soup)
            self.category = self.product_category(soup)
            self.upc = self.universal_product_code(soup)
            self.image_url = urljoin(self.url, self.product_image_url(soup))
            self.number = self.product_number_available(soup)
            self.including = self.product_price_including(soup)
            self.excluding = self.product_price_excluding(soup)
            self.review_rating = self.product_review_rating(soup)
            self.image_name = f"Images/{slugify(self.title[:100])}.jpg"

    # Les méthodes spécifiques à chaque livre, comme product_description, product_category, etc.
    # restent à peu près les mêmes mais deviennent des méthodes d'instance de la classe Book.
    def product_description(self, soup):
        return "hello", soup

    def product_category(self, soup):
        pass

    def universal_product_code(self, soup):
        pass

    def product_image_url(self, soup):
        pass

    def product_number_available(self, soup):
        pass

    def product_price_including(self, soup):
        pass

    def product_price_excluding(self, soup):
        pass

    def product_review_rating(self, soup):
        pass
