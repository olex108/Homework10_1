from unittest import expectedFailure

import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


# Test for function filter_by_currency
def test_filter_by_currency(list_of_transactions) -> None:
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
    iterator = filter_by_currency(list_of_transactions, "USD")
    result = list(iterator)
    assert result == expected_result


# Test for function transaction_descriptions
def test_transaction_descriptions(list_of_transactions) -> None:
    generator = transaction_descriptions(list_of_transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"



# Test for function card_number_generator
def test_card_number_generator() -> None:
    generator = card_number_generator(1, 5)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"

