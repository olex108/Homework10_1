from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция принимает на вход номер карты в виде числа и
    возвращает маску номера по правилу XXXX XX** **** XXXX"""

    return f"{str(card_number)[:4]} {str(card_number)[4:6]} ** **** {str(card_number)[12:]}"


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функция принимает на вход номер счета в виде числа и
    возвращает маску номера по правилу **XXXX"""

    return f"**{str(account_number)[-4:]}"
