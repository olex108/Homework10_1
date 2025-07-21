import os
from dotenv import load_dotenv

import requests

load_dotenv()

def get_transaction_amount(transaction):
    """
    Функцию принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют
    и конвертации суммы операции в рубли.
    Для конвертации валюты воспользуется Exchange Rates Data API: https://apilayer.com/exchangerates_data-api.
    """

    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    else:
        convert_from = transaction["operationAmount"]["currency"]["code"]
        convert_to = "RUB"
        amount = transaction["operationAmount"]["amount"]
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={convert_to}&from={convert_from}&amount={amount}"
        payload = {}
        headers = {
            "apikey": f"{os.getenv('API_KEY')}"
        }
        response = requests.request("GET", url, headers=headers, data=payload)

        if response.status_code == 200:
            return round(response.json()["result"], 2)
        else:
            raise ValueError("Некорректный ответ с сайта")


