def filter_by_state(data_list: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и опционально значение для ключа state
    возвращает новый список словарей, содержащий только те словари, у которых ключ соответствует указанному значению"""

    return [data for data in data_list if data["state"] == state]


def sort_by_date(data_list: list, reverse_parameter: bool = True) -> list:
    """Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание)
    возвращает новый список, отсортированный по дате (date)"""

    return sorted(data_list, key=lambda data: data["date"], reverse=reverse_parameter)
