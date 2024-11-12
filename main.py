from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))


def render_index():
    founding_year = 1920
    current_year = datetime.now().year
    winery_age = current_year - founding_year

    template = env.get_template('template.html')
    rendered_html = template.render(winery_age=winery_age)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(rendered_html)


render_index()

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)

server.serve_forever()
