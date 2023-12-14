import csv

import pytest

from src.item import Item
from src.phone import Phone


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_instantiate_from_csv():
    csv_data = "Phone,199.99,3\nLaptop,899.99,1\n"
    with open("test_items.csv", "w", encoding="utf-8") as csv_file:
        csv_file.write(csv_data)


def test_instantiate_from_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        with open("ite.csv", encoding="windows-1251") as csvfile:
            items = csv.DictReader(csvfile, delimiter=",")


def test_instantiate_from_csv_corrupted_file():
    with pytest.raises(csv.Error):
        Item.instantiate_from_csv()


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


def test_srt():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert str(phone1) == "iPhone 14"
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2

    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10


def test_invalid_number_of_sim():
    with pytest.raises(ValueError) as exception:
        Phone("Phone 1", 1000.0, 1, 0)
    assert (
            str(exception.value)
            == "Количество физических SIM-карт должно быть целым числом больше нуля."
    )


def test_valid_number_of_sim():
    phone = Phone("Phone 2", 1500.0, 2, 1)
    assert phone.number_of_sim == 1
