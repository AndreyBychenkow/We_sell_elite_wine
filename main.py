import os
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader

from read_wine import get_wines_from_excel

FOUNDING_YEAR = 1920
env = Environment(loader=FileSystemLoader('.'))


def get_year_word(years):
    if years % 10 == 1 and years % 100 != 11:
        return "год"
    elif 2 <= years % 10 <= 4 and not (12 <= years % 100 <= 14):
        return "года"
    else:
        return "лет"


def calculate_winery_age():
    current_year = datetime.now().year
    return current_year - FOUNDING_YEAR


def get_winery_age_description():
    winery_age = calculate_winery_age()
    year_word = get_year_word(winery_age)
    return winery_age, year_word


def render_template(wines, winery_age, year_word):
    template = env.get_template('template.html')
    return template.render(
        wines=wines,
        winery_age=winery_age,
        year_word=year_word
    )


def save_rendered_html(rendered_html):
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(rendered_html)


def render_index(file_path):
    wines = get_wines_from_excel(file_path)
    winery_age, year_word = get_winery_age_description()
    rendered_html = render_template(wines, winery_age, year_word)
    save_rendered_html(rendered_html)


def main():
    load_dotenv()
    file_path = os.environ.get('WINE_FILE_PATH')
    if not file_path:
        raise EnvironmentError("Переменная окружения 'WINE_FILE_PATH' не установлена.")

    render_index(file_path)
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
