from .models.scraper import Scraper


class AppController:
    def __init__(self, directory):
        self.directory = directory
        self.scraper = Scraper()

    def run(self):
        # Ici, vous utilisez self.scraper pour démarrer le processus de scraping
        # et enregistrez les résultats dans self.directory.
        pass
