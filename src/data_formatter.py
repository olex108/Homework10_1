from typing import Any

import pandas as pd


def get_data_from_csv(path_to_file: str) -> list[Any]:
    """
    Функция для считывания финансовых операций из CSV.
    Принимает путь к файлу CSV в качестве аргумента.
    Функция выдает список словарей с транзакциями
    """

    file_data = pd.read_csv(path_to_file)
    data_list = file_data.to_dict(orient="records")

    return data_list


def get_data_from_excel(path_to_file: str) -> list:
    """
    Функция для считывания финансовых операций из Excel.
    Принимает путь к файлу Excel в качестве аргумента.
    Функция выдает список словарей с транзакциями.
    """

    file_data = pd.read_excel(path_to_file)
    data_list = file_data.to_dict(orient="records")

    return data_list
