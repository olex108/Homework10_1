import os

from src.data_formatter import get_data_from_csv, get_data_from_excel
from src.generators import filter_by_currency
from src.processing import filter_by_state, process_bank_search, sort_by_date
from src.utils import get_transactions_data
from src.widget import get_date, mask_account_card


def main() -> None:
    """
    Функция main отвечает за основную логику проекта и связывает функциональности между собой.
    Программа состоит из следующих блоков:

    1. Выбор пункта меню

    2. Выбор статус фильтрации

    3. Выбор параметров сортировки

    - Сортировка по дате
    - Сортировка по возрастанию или убыванию
    - Выводить только рублевые транзакции
    - Отфильтровать список транзакций по определенному слову в описании

    4. Вызов необходимых функций:
    Вызов функции определяется по вводимым параметров пользователем

    - Вызов функции для получения списка транзакций:
    Одна из троих функций get_transactions_data, get_data_from_csv, get_data_from_excel

    - Вызов функции для фильтрации списка: filter_by_state

    - Вызов функции фильтрации по дате: sort_by_date

    - Вызов функции для вывода только рублевые транзакции: filter_by_currency

    - Вызов функции поиска по ключевому слову: process_bank_search

    5. Вывод результатов
    """

    ###################
    # Выбор пункта меню
    ###################

    dict_of_source_type_file = {"1": "JSON", "2": "CSV", "3": "XLSX"}
    file_type = None

    print(
        f"""
            Привет! Добро пожаловать в программу работы с банковскими транзакциями.
            Выберите необходимый пункт меню:
            1. Получит информацию о транзакциях из {dict_of_source_type_file["1"]}-файла
            2. Получит информацию о транзакциях из {dict_of_source_type_file["2"]}-файла
            3. Получит информацию о транзакциях из {dict_of_source_type_file["3"]}-файла
        """
    )

    while file_type not in dict_of_source_type_file.keys():

        file_type = input("Пункт меню: ")

        if file_type not in dict_of_source_type_file.keys():
            print(
                """
            Вы ввели неверный пункт меню!
            """
            )

    print(
        f"""
            Для обработки выбран {dict_of_source_type_file[file_type]}-файл.
        """
    )

    #########################
    # Выбор статус фильтрации
    #########################

    states_list = ["EXECUTED", "CANCELED", "PENDING"]
    state = None

    print(
        """
            Введите статус, по которому необходимо выполнить фильтрацию.
            Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING
        """
    )

    while state not in states_list:
        state = input("Статус: ").upper()

        if state not in states_list:
            print(
                f"""
            Статус операции "{state}" недоступен!
            """
            )

    print(
        f"""
            Операции отфильтрованы по статусу \"{state}\"
        """
    )

    #############################
    # Выбор параметров сортировки
    #############################

    # Сортировка по дате
    is_sort_by_date = input(
        """
            Отсортировать операции по дате? 
            \nДа/Нет: """
    )

    # Сортировка по возрастанию или убыванию
    if is_sort_by_date.lower() == "да":
        sort_reverse = input(
            """
            Направление сортировки:
            \nпо возрастанию/по убыванию: """
        )
        if sort_reverse.lower() == "по убыванию":
            is_sort_reverse = True
        else:
            is_sort_reverse = False

    # Выводить только рублевые транзакции
    is_sort_only_rub = input(
        """
            Выводить только рублевые транзакции? 
            \nДа/Нет: """
    )

    # Отфильтровать список транзакций по определенному слову в описании
    is_sort_by_word = input(
        """
            Отфильтровать список транзакций по определенному слову в описании? 
            \nДа/Нет: """
    )
    if is_sort_by_word.lower() == "да":
        search_word = input("""\nВведите ключевое слово: """)

    ###########################
    # Вызов необходимых функций
    ###########################

    list_of_transactions = []

    # Вызов функции для получения списка транзакций
    if file_type == "1":
        path_to_file = os.path.join("data", "operations.json")
        list_of_transactions = get_transactions_data(path_to_file)

    elif file_type == "2":
        path_to_file = os.path.join("data", "transactions.csv")
        list_of_transactions_csv = get_data_from_csv(path_to_file)
        # Меняем структуру словарей в списке
        for transaction in list_of_transactions_csv:
            transaction_dict = {
                "id": transaction.get("id"),
                "state": transaction.get("state"),
                "date": transaction.get("date"),
                "operationAmount": {
                    "amount": transaction.get("amount"),
                    "currency": {"name": transaction.get("currency_name"), "code": transaction.get("currency_code")},
                },
                "description": transaction.get("description"),
                # Так как не заполненные поля в CSV-файлах заполнены как "nan" переписываем их как None
                # Не нашел корректного способа выявить "nan" и использовал это сравнение
                "from": None if not isinstance(transaction.get("from"), str) else transaction.get("from"),
                "to": transaction.get("to"),
            }
            list_of_transactions.append(transaction_dict)

    else:
        path_to_file = os.path.join("data", "transactions_excel.xlsx")
        list_of_transactions_excel = get_data_from_excel(path_to_file)
        # Меняем структуру словарей в списке
        for transaction in list_of_transactions_excel:
            transaction_dict = {
                "id": transaction.get("id"),
                "state": transaction.get("state"),
                "date": transaction.get("date"),
                "operationAmount": {
                    "amount": transaction.get("amount"),
                    "currency": {"name": transaction.get("currency_name"), "code": transaction.get("currency_code")},
                },
                "description": transaction.get("description"),
                # Так как не заполненные поля в CSV-файлах заполнены как "nan" переписываем их как None
                # Не нашел корректного способа выявить "nan" и использовал это сравнение
                "from": None if not isinstance(transaction.get("from"), str) else transaction.get("from"),
                "to": transaction.get("to"),
            }
            list_of_transactions.append(transaction_dict)

    # Вызов функции для фильтрации списка
    list_of_transactions = filter_by_state(list_of_transactions, state)

    # Вызов функции фильтрации по дате:
    if is_sort_by_date.lower() == "да":
        list_of_transactions = sort_by_date(list_of_transactions, is_sort_reverse)

    # Вызов функции для вывода только рублевые транзакции:
    if is_sort_only_rub.lower() == "да":
        list_of_transactions = list(filter_by_currency(list_of_transactions, "RUB"))

    # Вызов функции поиска по ключевому слову:
    if is_sort_by_word.lower() == "да":
        list_of_transactions = process_bank_search(list_of_transactions, search_word)

    ###################
    # Вывод результатов
    ###################

    if len(list_of_transactions) == 0:
        print(
            """
            Не найдено ни одной транзакции, подходящей под ваши условия фильтрации
            """
        )
    else:

        print(
            """
            Распечатываю итоговый список транзакций...
            """
        )

        print(
            f"""
            Всего банковских операций в выборке: {len(list_of_transactions)}
            """
        )

        for transaction in list_of_transactions:
            print(
                f"""
            {get_date(transaction.get("date"))} {transaction.get("description")}
            {(lambda x: "" if x is None else x + " -> ")(mask_account_card(transaction.get("from")))}{mask_account_card(transaction.get("to"))}
            Сумма {transaction["operationAmount"]["amount"]} {transaction["operationAmount"]["currency"]["name"]}
            """
            )


if __name__ == "__main__":
    main()
