import pytest

from src.catalog import Category, Product


@pytest.fixture()
def samsung_product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture()
def iphone_product():
    return Product(
        "Iphone 15", "512GB, Gray space", 210000.0, 8
    )

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
