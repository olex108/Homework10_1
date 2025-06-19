from typing import Any

from _datetime import datetime

import masks


def mask_account_card(full_account_card: str) -> str:
    """Функция принимает один аргумент — строку, содержащую тип и номер карты или счета,
    возвращает строку с замаскированным номером"""

    mask_response = ""
    for item in full_account_card.split(" "):
        if item.isalpha():
            mask_response += item
        elif len(item) == 16:
            mask_response += masks.get_mask_card_number(item)
        elif len(item) == 20:
            mask_response += masks.get_mask_account(item)

    return mask_response


def get_date(date_in_full_formate: str) -> Any:
    """Функция принимает дату в формате 'YYYY-MM-DDTHH:MM:SS.mmmmmm' и возвращает в формате 'DD.ММ.YYYY'"""

    return datetime.fromisoformat(date_in_full_formate).strftime("%d.%m.%Y")
