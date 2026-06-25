import pytest

from src.catalog import Category, LawnGrass, Order, Product, Smartphone


@pytest.fixture()
def samsung_product():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture()
def iphone_product():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture()
def new_product():
    return Product.new_product()


@pytest.fixture()
def samsung_category(samsung_product):
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [samsung_product],
    )


@pytest.fixture()
def lawngrass_grass(samsung_product):
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )


@pytest.fixture()
def smartphone_xiaomi(samsung_product):
    return Smartphone(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14,
        90.3,
        "Note 11",
        1024,
        "Синий",
    )


@pytest.fixture()
def smartphone_samsung():
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )


@pytest.fixture()
def order_on_smartphone(samsung_product):
    return Order(samsung_product, 3)
