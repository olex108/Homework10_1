import random


def filter_by_currency(transactions: list[dict], currency: str) -> GeneratorExit[list]:
    """
    Функция принимает на вход список словарей, представляющих транзакции.
    Функция должна возвращать итератор, который поочередно выдает транзакции, где валюта операции соответствует
    заданной (например, USD)
    """
    return (transaction for transaction in transactions if transaction["operationAmount"]["currency"]["code"] == currency)


def transaction_descriptions(transactions: list[dict]):
    """
    Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
    """

    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start_number: int, stop_number: int):
    """
    Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор должен принимать начальное и конечное значения для генерации диапазона номеров.
    """

    for number in range(start_number, stop_number + 1):
        # number = str(random.randint(start_number, stop_number))
        number = f"{'0' * (16-len(str(number)))}{str(number)}"
        yield f"{str(number)[0:4]} {str(number)[4:8]} {str(number)[8:12]} {str(number)[12:16]}"
