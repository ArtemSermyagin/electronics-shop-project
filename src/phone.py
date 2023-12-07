from src.item import Item


class Phone(Item):
    # number_of_sim = 0
    def __init__(
        self, name: str, price: float, quantity: int, number_of_sim: int
    ) -> None:
        super().__init__(name, price, quantity)
        if not isinstance(number_of_sim, int) or number_of_sim <= 0:
            raise ValueError(
                "Количество физических SIM-карт должно быть целым числом больше нуля."
            )
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return (
            f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
        )

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        elif isinstance(other, Phone):
            return self.quantity + other.quantity
        else:
            raise TypeError("Невозможно сложить Phone и объект другого класса")


phone1 = Phone("iPhone 14", 120_000, 5, 2)

print(repr(phone1))
print(str(phone1))
print(phone1.number_of_sim)
item1 = Item("Смартфон", 10000, 20)
print(item1 + phone1)
print(phone1 + phone1)
