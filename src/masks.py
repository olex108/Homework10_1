from typing import Union
import logging
import os


logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

path_to_file = os.path.join(os.path.abspath(__file__), os.pardir, os.pardir, "logs", "masks.log")
file_handler = logging.FileHandler(path_to_file, mode="w", encoding="'utf-8")
file_formatter = logging.Formatter(f"%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция принимает на вход номер карты в виде числа и
    возвращает маску номера по правилу XXXX XX** **** XXXX"""

    logger.info(f"Вызов функции {get_mask_card_number.__name__}")
    if not isinstance(card_number, int) and not isinstance(card_number, str):
        logger.error(f"Неверный формат входного значения. Ошибка {TypeError}")
        raise TypeError("Неверный формат входного значения")

    if len(str(card_number)) != 16:
        logger.error(f"Неверная длина номера карты. Ошибка {ValueError}")
        raise ValueError("Неверная длина номера карты")

    logger.info("Функция возвращает маску номера карты")
    return f"{str(card_number)[:4]} {str(card_number)[4:6]}** **** {str(card_number)[12:]}"


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функция принимает на вход номер счета в виде числа и
    возвращает маску номера по правилу **XXXX"""

    logger.info(f"Вызов функции {get_mask_account.__name__}")
    if not isinstance(account_number, int) and not isinstance(account_number, str):
        logger.error(f"Неверный формат входного значения. Ошибка {TypeError}")
        raise TypeError("Неверный формат входного значения")

    if len(str(account_number)) != 20:
        logger.error(f"Неверная длина счета. Ошибка {ValueError}")
        raise ValueError("Неверная длина счета")

    logger.info(f"Функция {get_mask_account.__name__} возвращает маску счета")
    return f"**{str(account_number)[-4:]}"


get_mask_card_number(1234123412341234)