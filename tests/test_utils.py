import json
from unittest.mock import Mock

from src.utils import get_transactions_data


def test_get_transactions_data() -> None:

    # Тестирование по заданным данным в файле
    mock_data = Mock(return_value=[{"key": "value"}])
    json.load = mock_data
    assert get_transactions_data("data/operations.json") == [{"key": "value"}]

    # Тестирование по некорректных данных в файле
    mock_data_dict = Mock(return_value={"key": "value"})
    json.load = mock_data_dict
    assert get_transactions_data("data/operations.json") == []

    mock_data_empty = Mock(return_value=None)
    json.load = mock_data_empty
    assert get_transactions_data("data/operations.json") == []

    # Тестирование функции при вызове несуществующего файла
    assert get_transactions_data("data/operation.json") == []
