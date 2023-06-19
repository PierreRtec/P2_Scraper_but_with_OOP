from scraping_app.controller.app_controller import AppController
from scraping_app.views.command_line_view import ask_for_directory


def main():
    directory = ask_for_directory()
    app = AppController(directory)
    app.run()


if __name__ == "__main__":
    main()
