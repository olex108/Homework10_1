from typing import Any

from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(full_account_card: str) -> str:
    """Функция принимает один аргумент — строку, содержащую тип и номер карты или счета,
    возвращает строку с замаскированным номером"""

    number_account_card = []
    mask_response = []

    for item in full_account_card.split(" "):
        if item.isalpha():
            mask_response.append(item)
        elif item.isdigit():
            number_account_card.append(item)

    if len("".join(number_account_card)) == 16:
        mask_response.append(get_mask_card_number("".join(number_account_card)))
    elif len("".join(number_account_card)) == 20:
        mask_response.append(get_mask_account("".join(number_account_card)))
    else:
        raise ValueError("Неверная длина номера")

    return " ".join(mask_response)


def get_date(date_in_full_formate: str) -> Any:
    """Функция принимает дату в формате 'YYYY-MM-DDTHH:MM:SS.mmmmmm' и возвращает в формате 'DD.ММ.YYYY'"""

    try:
        return datetime.fromisoformat(date_in_full_formate).strftime("%d.%m.%Y")
    except ValueError:
        return ""
