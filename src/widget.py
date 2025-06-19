import masks


def mask_account_card(full_account_card: str) -> str:
    """ Функция принимает один аргумент — строку, содержащую тип и номер карты или счета,
    возвращает строку с замаскированным номером """

    mask_response = ""
    for item in full_account_card.split(" "):
        if item.isalpha():
            mask_response += item
        elif len(item) == 16:
            mask_response += masks.get_mask_card_number(item)
        elif len(item) == 20:
            mask_response += masks.get_mask_account(item)

    return mask_response


def get_date(date_in_full_formate: str) -> str:
    """ Функция принимает дату в формате 'YYYY-MM-DDTHH:MM:SS.mmmmmm' и возвращает в формате 'DD.ММ.YYYY' """

    date_part = date_in_full_formate.split("T")[0]
    date_in_list = date_part.split("-")[::-1]

    return ".".join(date_in_list)
