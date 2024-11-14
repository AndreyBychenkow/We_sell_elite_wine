from pprint import pprint

import pandas


def get_wines_from_excel():
    excel_data_df = pandas.read_excel('wine2.xlsx')

    excel_data_df.columns = ['category', 'name', 'variety', 'price', 'image_url']

    excel_data_df = excel_data_df.where(pandas.notnull(excel_data_df), None)

    grouped_wines = {
        "Белые вина": [],
        "Красные вина": [],
        "Напитки": []
    }

    for _, wine in excel_data_df.iterrows():
        wine_data = {
            "Картинка": wine['image_url'] or "",
            "Категория": wine['category'] or "",
            "Название": wine['name'] or "",
            "Сорт": wine['variety'] or "",
            "Цена": wine['price'] or ""
        }

        category = (wine['category'] or "").lower()
        if "белые вина" in category or "белое" in category:
            grouped_wines["Белые вина"].append(wine_data)
        elif "красные вина" in category or "красное" in category:
            grouped_wines["Красные вина"].append(wine_data)
        else:
            grouped_wines["Напитки"].append(wine_data)

    pprint(grouped_wines)
    return grouped_wines


if __name__ == "__main__":
    get_wines_from_excel()
