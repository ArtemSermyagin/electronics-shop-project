import pytest

from src.item import Item


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_instantiate_from_csv():
    csv_data = "Phone,199.99,3\nLaptop,899.99,1\n"
    with open("test_items.csv", "w", encoding="utf-8") as csv_file:
        csv_file.write(csv_data)


def test_apply_discount():
    item = Item("Товар", 10.0, 5)
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8.0


def test_instantiate_from_csv_():
    Item.instantiate_from_csv("../src/items.csv")
    assert len(Item.all) == 5
    assert Item.all[0].name == "Смартфон"
    assert Item.all[1].price == 1000
    assert Item.all[2].quantity == 5

@pytest.fixture
def sample_item():
    return Item("Смартфон", 50.99, 1)


def test_str_method(sample_item):
    assert str(sample_item) == "Смартфон"


def test_repr_method(sample_item):
    assert repr(sample_item) == "Item('Смартфон', 50.99, 1)"