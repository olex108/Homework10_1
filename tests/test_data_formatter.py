from unittest.mock import Mock, patch

import pandas

from src.data_formatter import get_data_from_csv, get_data_from_excel


# Тесты для функции считывания финансовых операций из CSV используют Mock и patch
@patch("pandas.read_csv")
def test_get_data_from_csv(mock_get: Mock) -> None:
    mock_get.return_value = pandas.DataFrame({"col1": [1, 2], "col2": [3, 4]})
    assert get_data_from_csv("aaaa") == [{"col1": 1, "col2": 3}, {"col1": 2, "col2": 4}]


# Тесты для функции считывания финансовых операций из Excel используют Mock и patch
@patch("pandas.read_excel")
def test_get_data_from_excel(mock_get: Mock) -> None:
    mock_get.return_value = pandas.DataFrame({"col1": [1, 2], "col2": [3, 4]})
    assert get_data_from_excel("test.xlsx") == [{"col1": 1, "col2": 3}, {"col1": 2, "col2": 4}]
