import csv
from urllib.parse import urljoin
from urllib.request import urlretrieve

import requests
from bs4 import BeautifulSoup

from scraping_app.models.category import Category


class Scraper:
    def __init__(self, base_url):
        self.base_url = base_url

    def scrape(self):
        self.categories = []
        response = requests.get(self.base_url)
        if response.ok:
            soup = BeautifulSoup(response.content, "html.parser")
            menu = soup.find(class_="side_categories")
            links = menu.find_all("a")
            for link in links:
                category = Category(urljoin(self.base_url, link["href"]))
                self.categories.append(category)

    def save_book_info_to_csv(self):
        """
        Cette partie s'occupe de sauvegarder les données récupérées,
        dans une boucle jusqu'à la fin de la liste.
        """
        for category in self.categories:
            for book in category.books:
                first_book_info = book
                category_name = first_book_info.category.strip()
                with open(f"Scraping/{category_name}.csv", "w", encoding="utf-8-sig") as csvfile:
                    writer = csv.DictWriter(csvfile, first_book_info.__dict__, dialect="excel")
                    writer.writeheader()
                    for book in category.books:
                        writer.writerow(book.__dict__)
                        urlretrieve(book.image_url, filename=book.image_name)
