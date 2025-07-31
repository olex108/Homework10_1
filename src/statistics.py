from collections import Counter


def get_count_by_descriptions(data_list: list, descriptions_list: list) -> dict:
    """
    Функция, принимает список словарей с данными о банковских операциях и список категорий операций,
    возвращает словарь, где ключи — это названия категорий, а значения — это количество операций в каждой категории.
    """

    sorted_descriptions_list = [
        transaction.get("description")
        for transaction in data_list
        if transaction.get("description") in descriptions_list
    ]

    return dict(Counter(sorted_descriptions_list))
