import os
from collections import defaultdict

import pandas
from dotenv import load_dotenv

load_dotenv()


def get_wines_from_excel(file_path=None):
    try:

        file_path = file_path or os.environ['WINE_FILE_PATH']

        if not os.path.exists(file_path):
            raise FileNotFoundError

    except (KeyError, FileNotFoundError):
        raise FileNotFoundError(
            "Файл не найден. Проверьте, что переменная окружения 'WINE_FILE_PATH' "
            "установлена и файл существует."
        )

    excel_data_df = pandas.read_excel(file_path)
    excel_data_df.columns = ['category', 'name', 'variety', 'price', 'image_url', 'is_profitable']
    excel_data_df = excel_data_df.where(pandas.notnull(excel_data_df), None)

    grouped_wines = defaultdict(list)

    for _, wine in excel_data_df.iterrows():
        wine_data = {
            "Картинка": wine['image_url'] or "",
            "Категория": wine['category'] or "",
            "Название": wine['name'] or "",
            "Сорт": wine['variety'] or "",
            "Цена": wine['price'] or "",
            "Выгодное предложение": wine['is_profitable'] or False
        }

        category = wine['category'] or "Напитки"
        grouped_wines[category].append(wine_data)

    grouped_wines = dict(grouped_wines)

    for category, wines in grouped_wines.items():
        if wines:
            cheapest_wine = min(wines, key=lambda x: x['Цена'])
            cheapest_wine['is_cheapest'] = True

    return grouped_wines
