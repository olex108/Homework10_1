import pandas as pd

import csv

import os

def get_data_from_csv(path_to_file):
    """
    Функция для считывания финансовых операций из CSV принимает путь к файлу CSV в качестве аргумента
    Функция для считывания финансовых операций из CSV выдает список словарей с транзакциями
    """

    with open(path_to_file, encoding="utf-8") as file:
        file_data = csv.DictReader(file)
        data_list = [raw for raw in file_data]

    return data_list

# print(get_data_from_csv(os.path.join(os.pardir, "data", "transactions.csv")))


def get_data_from_excel(path_to_file):
    """
    Функция для считывания финансовых операций из Excel принимает путь к файлу Excel в качестве аргумента
    Функция для считывания финансовых операций из Excel выдает список словарей с транзакциями
    """

    file_data = pd.read_excel(path_to_file)
    data_list = file_data.to_dict(orient="records")

    return data_list

# print(get_data_from_excel(os.path.join(os.pardir, "data", "transactions_excel.xlsx")))

