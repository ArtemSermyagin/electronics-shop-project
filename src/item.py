import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

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
        # self.all.clear()

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

        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, filename: str) -> None:
        """
        Создает объекты Item из данных CSV-файла.

        :param filename: Имя CSV-файла.
        """
        cls.all.clear()
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            skip_first = True
            for row in reader:
                if skip_first:
                    skip_first = False
                    continue
                name = row[0]
                price = cls.string_to_number(row[1])
                quantity = cls.string_to_number(row[2])
                item = Item(name, price, quantity)

                # cls.all.append(item)

    @staticmethod
    def string_to_number(value: str, default: float = 0.0, raise_error: bool = False) -> float:
        """
        Преобразует строку в число.

        :param value: Строковое представление числа.
        :param default: Значение по умолчанию, возвращаемое при ошибке преобразования.
        :param raise_error: Флаг, указывающий, следует ли выбрасывать исключение при ошибке.
        :return: Преобразованное число.
        """
        try:
            return float(value)
        except ValueError:
            if raise_error:
                raise  # выбросить исключение при неудачном преобразовании
            # return default
