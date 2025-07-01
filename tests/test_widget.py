import pytest

from src.widget import get_date, mask_account_card


# Test for function mask_account_card
# Проверка что функция корректно распознает и применяет нужный тип маскировки в зависимости от типа входных данных
# Параметризованные тесты с разными типами карт и счетов для проверки универсальности функции.
@pytest.mark.parametrize(
    "name, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Visa 70007922896063611234", "Visa **1234"),
        ("Visa Platinum 7000 7922 8960 6361", "Visa Platinum 7000 79** **** 6361"),
        ("MasterCard   7000 7922 8960 6361", "MasterCard 7000 79** **** 6361"),
    ],
)
def test_mask_account_card(name: str, expected: str) -> None:
    assert mask_account_card(name) == expected


# Тестирование функции на обработку некорректных входных данных и проверка ее устойчивости к ошибкам.
def test_mask_account_card_invalid_number(invalid_card_number: str) -> None:
    with pytest.raises(ValueError):
        mask_account_card(invalid_card_number)


# Test for function get_date
# Тестирование правильности преобразования даты.
# Проверка работы функции на различных входных форматах даты, включая граничные случаи и нестандартные строки с датами.
@pytest.mark.parametrize(
    "date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-03-01T02:26:18.671407", "01.03.2024"),
        ("02:26:18.671407", ""),
        ("2024-03-01", "01.03.2024"),
        ("", ""),
    ],
)
def test_get_date(date: str, expected: str) -> None:
    assert get_date(date) == expected
