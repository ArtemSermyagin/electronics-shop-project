import csv
from abc import ABC


class Item:
    """
    Класс для представления товара в магазине.
    """

    pay_rate = 1.0
    all = []

    def __repr__(self) -> str:
        return f"Item('{self.__name}', {self.price }, {self.quantity})"  # noqa

    def __str__(self):
        return f"{self.__name}"

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __add__(self, other):
        return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(self.__name) <= 10:
            self.__name = new_name
        else:
            self.__name = new_name[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """

        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file_name):
        """
        Создает объекты Item из данных CSV-файла.

        :param filename: Имя CSV-файла.
        """
        cls.all.clear()
        try:
            with open(file_name, encoding="windows-1251") as csvfile:
                items = csv.DictReader(csvfile, delimiter=",")
                header = next(items)
                if 'name' not in header or 'price' not in header or 'quantity' not in header:
                    raise csv.Error('Файл item.csv поврежден')
                else:
                    for item in items:
                        name = item["name"]
                        price = float(item["price"])
                        quantity = cls.string_to_number(item["quantity"])
                        cls(name, price, quantity)
                        print(name, price, quantity)
        except FileNotFoundError:
            print("Отсутствует файл item.csv")
        except csv.Error:
            print('Файл item.csv поврежден')



    @staticmethod
    def string_to_number(
        value: str, default: int = 0, raise_error: bool = False
    ) -> int:
        """
        Преобразует строку в число.

        :param value: Строковое представление числа.
        :param default: Значение по умолчанию, возвращаемое при ошибке преобразования.
        :param raise_error: Флаг, указывающий, следует ли выбрасывать исключение при ошибке.
        :return: Преобразованное число.
        """
        try:
            return int(float(value))
        except ValueError("выбросить исключение при неудачном преобразовании"):
            print("Ошибка")


# print(Item.instantiate_from_csv("../tests/item.csv"))