import re
from datetime import datetime

from src.widget import get_date


def filter_by_state(data_list: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и опционально значение для ключа state
    возвращает новый список словарей, содержащий только те словари, у которых ключ соответствует указанному значению"""

    return [data for data in data_list if data.get("state") == state]


def sort_by_date(data_list: list, reverse_parameter: bool = True) -> list:
    """Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание)
    возвращает новый список, отсортированный по дате (date)"""

    data_list_with_correct_date = []

    # Заполняем список элементами с корректной датой
    for item in data_list:
        try:
            if get_date(item["date"]):
                data_list_with_correct_date.append(item)
        except ValueError:
            continue

    return sorted(
        data_list_with_correct_date,
        key=lambda data: datetime.fromisoformat(data["date"]).strftime("%Y.%m.%d"),
        reverse=reverse_parameter,
    )


def process_bank_search(data: list, search: str) -> list:
    """
    Функция, принимает список словарей с данными о банковских операциях и строку поиска,
    возвращает список словарей, у которых в описании есть данная строка.
    """

    sorted_list = []
    for transaction in data:
        match = re.search(search.lower(), transaction.get("description").lower())
        if match:
            sorted_list.append(transaction)

    return sorted_list
