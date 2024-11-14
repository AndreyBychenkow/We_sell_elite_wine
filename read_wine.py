from collections import defaultdict

import pandas


def get_wines_from_excel():
    excel_data_df = pandas.read_excel('wine2.xlsx')
    excel_data_df.columns = ['category', 'name', 'variety', 'price', 'image_url']
    excel_data_df = excel_data_df.where(pandas.notnull(excel_data_df), None)

    grouped_wines = defaultdict(list)

    for _, wine in excel_data_df.iterrows():
        wine_data = {
            "Картинка": wine['image_url'] or "",
            "Категория": wine['category'] or "",
            "Название": wine['name'] or "",
            "Сорт": wine['variety'] or "",
            "Цена": wine['price'] or ""
        }

        category = wine['category'] or "Напитки"
        grouped_wines[category].append(wine_data)

    grouped_wines = dict(grouped_wines)

    categories = ['Белые вина', 'Красные вина', 'Напитки']
    categorized_wines = {category: grouped_wines.get(category, []) for category in categories}

    return categorized_wines
