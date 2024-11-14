import pandas


def get_wines_from_excel():
    excel_data_df = pandas.read_excel('wine.xlsx')
    excel_data_df.columns = ['name', 'variety', 'price', 'image_url']
    wines = excel_data_df.to_dict(orient='records')
    return wines
