import json
import logging
import os
from json import JSONDecodeError

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
path_to_file = os.path.join(os.path.abspath(__file__), os.pardir, os.pardir, "logs", "utils.log")
file_handler = logging.FileHandler(path_to_file, mode="w", encoding="'utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

# def load_json(data_list):
#     """
#     Функция для записи данных в JSON файл operations.json
#     """
#
#     path = os.path.join(os.pardir, "data", "operations.json")
#     with open(path, "w") as file:
#         json.dump(data_list, file, indent=4)


def get_transactions_data(path_to_file: str) -> list:
    """
    Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список
    """

    logger.info(f"вызов функции {get_transactions_data.__name__}, путь до файла {path_to_file}")
    try:
        with open(path_to_file, "r") as file:
            data = json.load(file)

        if not isinstance(data, list):
            logger.warning("Данные в файле не соответствуют ожидаемому формату")
            return []
        else:
            logger.info("Функция возвращает данные из файла")
            return data

    except JSONDecodeError as ex:
        logger.error(f"Данные в файле не соответствуют ожидаемому формату. Ошибка {ex}")
        return []

    except FileNotFoundError as ex:
        logger.error(f"Файл по заданному пути отсутствует {ex}")
        return []
