import pytest

from src.decorators import log
from src.masks import get_mask_card_number
from typing import Union


# Test for function log
def test_log(capsys):
    @log()
    def test_function(card_number: Union[int, str]) -> str:
        """Функция принимает на вход номер карты в виде числа и
        возвращает маску номера по правилу XXXX XX** **** XXXX"""
        if not isinstance(card_number, int) and not isinstance(card_number, str):
            raise TypeError("Неверный формат входного значения")

        if len(str(card_number)) != 16:
            raise ValueError("Неверная длина номера карты")

        return f"{str(card_number)[:4]} {str(card_number)[4:6]}** **** {str(card_number)[12:]}"

    # тестирования вывода в консоль.
    test_function(1234123412341234)
    capture = capsys.readouterr()
    assert capture.out == "test_function ok\n"


    with pytest.raises(ValueError):
        test_function(12341234123412)

    capture = capsys.readouterr()
    assert capture.out == "test_function error: ValueError. Inputs: (12341234123412,), {}\n"

    # Тесты выполнение функций с декоратором и обработки исключений
def test_function_with_decorator():
    @log()
    def test_function(card_number: Union[int, str]) -> str:
        """Функция принимает на вход номер карты в виде числа и
        возвращает маску номера по правилу XXXX XX** **** XXXX"""
        if not isinstance(card_number, int) and not isinstance(card_number, str):
            raise TypeError("Неверный формат входного значения")

        if len(str(card_number)) != 16:
            raise ValueError("Неверная длина номера карты")

        return f"{str(card_number)[:4]} {str(card_number)[4:6]}** **** {str(card_number)[12:]}"

    result = test_function(1234123412341234)
    assert result == "1234 12** **** 1234"

    with pytest.raises(ValueError):
        test_function(12341234123412)
