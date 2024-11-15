from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

from read_wine import get_wines_from_excel, env

FOUNDING_YEAR = 1920


def get_year_word(years):
    if years % 10 == 1 and years % 100 != 11:
        return "год"
    elif 2 <= years % 10 <= 4 and not (12 <= years % 100 <= 14):
        return "года"
    else:
        return "лет"


def render_index():
    current_year = datetime.now().year
    winery_age = current_year - FOUNDING_YEAR
    year_word = get_year_word(winery_age)
    wines = get_wines_from_excel()
    template = env.get_template('template.html')
    rendered_html = template.render(wines=wines, winery_age=winery_age, year_word=year_word)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(rendered_html)


def main():
    render_index()
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
