from idlelib.rpc import response_queue
from unittest.mock import Mock, patch
import pytest
import requests

import json

from src.external_api import get_transaction_amount

@patch("requests.request")
def test_get_transaction_amount(mock_get):
    # Тест функции при получении транзакции в рублях
    assert get_transaction_amount(
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "\u0440\u0443\u0431.",
                    "code": "RUB"
                }
            },
            "description": "\u041f\u0435\u0440\u0435\u0432\u043e\u0434 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438",
            "from": "Maestro 1596837868705199",
            "to": "\u0421\u0447\u0435\u0442 64686473678894779589"
        }
    ) == 31957.58

    # Тест функции при транзакции в USD
    mock_get.return_value.json.return_value = {
        "result": 2499073.96,
    }
    mock_get.return_value.status_code = 200

    assert get_transaction_amount(
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "\u0440\u0443\u0431.",
                    "code": "USD"
                }
            },
            "description": "\u041f\u0435\u0440\u0435\u0432\u043e\u0434 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438",
            "from": "Maestro 1596837868705199",
            "to": "\u0421\u0447\u0435\u0442 64686473678894779589"
        }
    ) == 2499073.96

    # Тест возникновения ошибки при отсутствии страницы
    with pytest.raises(ValueError):
        mock_get.return_value.status_code = 404
        get_transaction_amount(
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                    "amount": "31957.58",
                    "currency": {
                        "name": "\u0440\u0443\u0431.",
                        "code": "USD"
                    }
                },
                "description": "\u041f\u0435\u0440\u0435\u0432\u043e\u0434 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438",
                "from": "Maestro 1596837868705199",
                "to": "\u0421\u0447\u0435\u0442 64686473678894779589"
            }
        )

