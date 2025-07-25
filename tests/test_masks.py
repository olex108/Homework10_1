from typing import Union

import pytest

from src.masks import get_mask_account, get_mask_card_number


# Test for function get_mask_card_number
# Тестирование правильности маскирования номера карты.
@pytest.mark.parametrize(
    "values, expected", [("1234123412341234", "1234 12** **** 1234"), (1234123412341234, "1234 12** **** 1234")]
)
# Проверка работы функции на различных входных форматах номеров карт
def test_get_mask_card_number(values: Union[int, str], expected: str) -> None:
    assert get_mask_card_number(values) == expected


# Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты
def test_get_mask_card_number_empty(empty_string: str) -> None:

    with pytest.raises(ValueError):
        get_mask_card_number(empty_string)


# Проверка работы функции на различных входных форматах (вызов ошибке при неверном типе входных данных)
def test_get_mask_card_number_error(list_of_card_numbers: int | str) -> None:

    with pytest.raises(TypeError):
        get_mask_card_number(list_of_card_numbers)


# Test for function get_mask_account
# Тестирование правильности маскирования номера счета
@pytest.mark.parametrize("values, expected", [("12341234123412341234", "**1234")])
# Проверка работы функции с различными форматами и длинами номеров счетов.
# Проверка, что функция корректно обрабатывает входные данные, где номер счета меньше ожидаемой длины
def test_get_mask_account(values: Union[int, str], expected: str) -> None:
    assert get_mask_account(values) == expected
