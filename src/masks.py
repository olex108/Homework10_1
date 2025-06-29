from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция принимает на вход номер карты в виде числа и
    возвращает маску номера по правилу XXXX XX** **** XXXX"""
    if type(card_number) != int and type(card_number) != str:
        raise TypeError("Неверный формат входного значения")

    if len(str(card_number)) != 16:
        raise ValueError("Неверная длина номера карты")

    return f"{str(card_number)[:4]} {str(card_number)[4:6]}** **** {str(card_number)[12:]}"


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функция принимает на вход номер счета в виде числа и
    возвращает маску номера по правилу **XXXX"""

    return f"**{str(account_number)[-4:]}"
