import masks


def mask_account_card(user_data: str) -> str:


    response_str = []
    for item in user_data.split(" "):
        if item.isalpha():
            response_str.append(item)
        elif len(item) == 16:
            response_str.append(masks.get_mask_card_number(item))
        elif len(item) == 20:
            response_str.append(masks.get_mask_account(item))

    return " ".join(response_str)