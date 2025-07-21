import json
from json import JSONDecodeError
import os

# def load_json(data_list):
#     """
#     Функция для записи данных в JSON файл operations.json
#     """
#
#     path = os.path.join(os.pardir, "data", "operations.json")
#     with open(path, "w") as file:
#         json.dump(data_list, file, indent=4)


def get_transactions_data(path_to_file: str) ->list:
    """
    Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список
    """

    try:
        with open(path_to_file, "r") as file:
            data = json.load(file)

        if type(data) != list:
            return []
        else:
            return data

    except JSONDecodeError:
        return []

    except FileNotFoundError:
        return []


