import pytest

from src.processing import filter_by_state, process_bank_search, sort_by_date


# Test for function filter_by_state
# Параметризация тестов для различных возможных значений статуса state
@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        ("INVALID", []),
        ("", []),
    ],
)
# Тестирование фильтрации списка словарей по заданному статусу state
# Проверка работы функции при отсутствии словарей с указанным статусом state в списке.
def test_filter_by_state(list_of_dictionaries_with_state: list, state: str, expected: list) -> None:
    assert filter_by_state(list_of_dictionaries_with_state, state) == expected


# Проверка работы функции без указания статуса state.
def test_filter_by_state_without_state(list_of_dictionaries_with_state: list) -> None:
    assert filter_by_state(list_of_dictionaries_with_state) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


# Test for function sort_by_date
# Тестирование сортировки списка словарей по датам в порядке убывания и возрастания.
# Проверка корректности сортировки при одинаковых датах.
@pytest.mark.parametrize(
    "reverse_parameter, expected",
    [
        (
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064519, "state": "CANCEL", "date": "2018-10-14T08:21:33.419440"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064519, "state": "CANCEL", "date": "2018-10-14T08:21:33.419440"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date(list_of_dictionaries_with_state: list, reverse_parameter: bool, expected: list) -> None:
    assert sort_by_date(list_of_dictionaries_with_state, reverse_parameter) == expected


# Тесты на работу функции с некорректными или нестандартными форматами дат.
@pytest.mark.parametrize(
    "reverse_parameter, expected",
    [
        (
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03"},
                {"id": 615064519, "state": "CANCEL", "date": "2018-10-14 08:21:33.419440"},
            ],
        ),
        (
            False,
            [
                {"id": 615064519, "state": "CANCEL", "date": "2018-10-14 08:21:33.419440"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03"},
            ],
        ),
    ],
)
def test_sort_by_date_different_date(
    list_of_dictionaries_with_different_date: list, reverse_parameter: bool, expected: list
) -> None:
    assert sort_by_date(list_of_dictionaries_with_different_date, reverse_parameter) == expected


# Проверка работы функции при вводе пустого списка
def test_sort_by_date_empty() -> None:
    assert sort_by_date([]) == []


# Test for function process_bank_search
@pytest.mark.parametrize(
    "transactions_list, search, expected",
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
            "вклад",
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
            ],
        ),
    ],
)
def test_process_bank_search(transactions_list: list, search: str, expected: list) -> None:
    assert process_bank_search(transactions_list, search) == expected
