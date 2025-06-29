import pytest

from src.masks import get_mask_card_number, get_mask_account

# Test for function get_mask_card_number
# Тестирование правильности маскирования номера карты.
@pytest.mark.parametrize("values, expected", [
    ("1234123412341234", "1234 12** **** 1234"),
    (1234123412341234, "1234 12** **** 1234")
])

# Проверка работы функции на различных входных форматах номеров карт
def test_get_mask_card_number(values, expected):
    assert get_mask_card_number(values) == expected

# Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты
def test_get_mask_card_number_empty(empty_string):

    with pytest.raises(ValueError):
        get_mask_card_number(empty_string)

# Проверка работы функции на различных входных форматах (вызов ошибке при неверном типе входных данных)
def test_get_mask_card_number_error(list_of_card_numbers):

    with pytest.raises(TypeError):
        get_mask_card_number(list_of_card_numbers)


# Test for function get_mask_account
# Тестирование правильности маскирования номера счета
@pytest.mark.parametrize("values, expected", [
    ("12341234123412341234", "**1234"),
    (1234123412341234, "**1234"),
    (123412341234, "**1234")
])

# Проверка работы функции с различными форматами и длинами номеров счетов.
# Проверка, что функция корректно обрабатывает входные данные, где номер счета меньше ожидаемой длины
def test_get_mask_account(values, expected):
    assert get_mask_account(values) == expected
