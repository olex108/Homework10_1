from typing import Any, Union
from datetime import datetime


def log(filename: Union[None, str] = None) -> Any:
    """
    Декоратор автоматически логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки.
    Декоратор принимает необязательный аргумент filename, который определяет, куда будут записываться логи
    (в файл или в консоль):
    - Если filename задан, логи записываются в указанный файл.
    - Если filename не задан, логи выводятся в консоль.
    Логирование включает:
    - Имя функции и результат выполнения при успешной операции.
    - Имя функции, тип возникшей ошибки и входные параметры, если выполнение функции привело к ошибке.
    """

    def log_decorator(function: Any) -> Any:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = 0
            try:
                start_time = f"{function.__name__} start - {datetime.now()}"
                result = function(*args, **kwargs)
                stop_time = f"{function.__name__} stop - {datetime.now()}"
                result_message = f"{function.__name__} ok"
                if filename is None:
                    print(f"{start_time}\n{stop_time}\n{result_message}")
                else:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{start_time}\n{stop_time}\n{result_message}")
                return result
            except Exception as e:
                stop_time = f"{function.__name__} stop - {datetime.now()}"
                result_message = f"{function.__name__} error: {type(e).__name__}. Inputs: {args}, {{}}"
                if filename is None:
                    print(f"{start_time}\n{stop_time}\n{result_message}")
                else:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{start_time}\n{stop_time}\n{result_message}")
                raise e

        return wrapper

    return log_decorator