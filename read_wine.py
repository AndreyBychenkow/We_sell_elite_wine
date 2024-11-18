import os
from collections import defaultdict

import pandas


def check_file_exists(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл не найден: {file_path}. Проверьте, что файл существует.")


def load_excel_data(file_path):
    excel_data_df = pandas.read_excel(file_path)
    excel_data_df.columns = ['category', 'name', 'variety', 'price', 'image_url', 'is_profitable']
    return excel_data_df.where(pandas.notnull(excel_data_df), None)


def group_wines_by_category(excel_data_df):
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

    return dict(grouped_wines)


def mark_cheapest_wines(grouped_wines):
    for category, wines in grouped_wines.items():
        if wines:
            cheapest_wine = min(wines, key=lambda x: x['Цена'])
            cheapest_wine['is_cheapest'] = True
    return grouped_wines


def get_wines_from_excel(file_path):
    check_file_exists(file_path)
    excel_data_df = load_excel_data(file_path)
    grouped_wines = group_wines_by_category(excel_data_df)
    return mark_cheapest_wines(grouped_wines)
