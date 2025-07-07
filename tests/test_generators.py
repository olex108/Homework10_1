from unittest import expectedFailure

import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


# Test for function filter_by_currency
def test_filter_by_currency(list_of_transactions: list) -> None:
    expected_result = [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'},
        {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
         'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
         'to': 'Счет 75651667383060284188'},
        {'id': 895315941, 'state': 'EXECUTED', 'date': '2018-08-19T04:27:37.904916',
         'operationAmount': {'amount': '56883.54', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод с карты на карту', 'from': 'Visa Classic 6831982476737658',
         'to': 'Visa Platinum 8990922113665229'}
    ]

    # Тестирование, проверяющее, что функция фильтрует транзакции по заданной валюте
    test_iterator = filter_by_currency(list_of_transactions, "USD")
    result = list(test_iterator)
    assert result == expected_result

    # Тестирование, правильности обработки случаев, когда транзакции в заданной валюте отсутствуют
    test_iterator_invalid_currency = filter_by_currency(list_of_transactions, "EUR")
    result = list(test_iterator_invalid_currency)
    assert result == []

    # Проверка, что генератор не завершается ошибкой при обработке пустого списка
    test_iterator_empty_list = filter_by_currency([], "USD")
    result = list(test_iterator_empty_list)
    assert result == []



# Test for function transaction_descriptions
def test_transaction_descriptions(list_of_transactions: list) -> None:
    test_generator = transaction_descriptions(list_of_transactions)
    assert next(test_generator) == "Перевод организации"
    assert next(test_generator) == "Перевод со счета на счет"
    assert next(test_generator) == "Перевод со счета на счет"

# Тестирование работы функции при задании пустого списка
def test_transaction_descriptions_empty_list() -> None:
    test_generator = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(test_generator)



# Test for function card_number_generator
def test_card_number_generator() -> None:
    test_generator = card_number_generator(1, 3)
    # Проверка, что генератор выдает правильные номера карт в заданном диапазоне
    # Проверка корректности форматирования номеров карт
    assert next(test_generator) == "0000 0000 0000 0001"
    assert next(test_generator) == "0000 0000 0000 0002"
    assert next(test_generator) == "0000 0000 0000 0003"
    # Проверка на правильность завершения генерации
    with pytest.raises(StopIteration):
        next(test_generator)

