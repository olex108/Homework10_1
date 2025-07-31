import pytest

from src.statistics import get_count_by_descriptions


@pytest.mark.parametrize(
    "transactions_list, descriptions_list, expected",
    [
        (
            [
                {
                    "state": "EXECUTED",
                    "date": "2018-02-03T07:16:28.366141",
                    "operationAmount": {"amount": "90297.21", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Открытие вклада",
                    "to": "Счет 37653295304860108767",
                },
                {
                    "id": 587085106,
                    "state": "EXECUTED",
                    "date": "2018-03-23T10:45:06.972075",
                    "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Открытие вклада",
                    "to": "Счет 41421565395219882431",
                },
                {
                    "id": 596171168,
                    "state": "EXECUTED",
                    "date": "2018-07-11T02:26:18.671407",
                    "operationAmount": {"amount": "79931.03", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод",
                    "to": "Счет 72082042523231456215",
                },
            ],
            ["Открытие вклада", "Перевод"],
            {"Открытие вклада": 2, "Перевод": 1},
        ),
    ],
)
def test_get_count_by_descriptions(transactions_list: list, descriptions_list: list, expected: dict) -> None:
    assert get_count_by_descriptions(transactions_list, descriptions_list) == expected
