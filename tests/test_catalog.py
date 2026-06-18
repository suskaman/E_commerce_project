import pytest

from src.catalog import Category, EvenProduct, Product

# -----------------
# EvenProduct
# -----------------


def test_EvenProduct(samsung_product, iphone_product):
    category = Category("смартфоны", "смартфоны", [samsung_product, iphone_product])
    list_of_products = []
    for product in EvenProduct(category):
        list_of_products.append(product)
    assert list_of_products == [
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.",
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.",
    ]


# -----------------
# product
# -----------------


def test_init_product(samsung_product):
    assert samsung_product.name == "Samsung Galaxy S23 Ultra"
    assert samsung_product.description == "256GB, Серый цвет, 200MP камера"
    assert samsung_product.price == 180000.0
    assert samsung_product.quantity == 5


def test_product_added_to_list(samsung_product):
    assert samsung_product in Product.list_of_products


#
# new_product
#


def test_product_new_product():
    new_product = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
    product = Product.new_product(new_product)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.price == 180000.0
    # количество увеличилось, так как такой товар уже есть
    assert product.quantity == 10

    assert product in Product.list_of_products


#
# price setter
#


def test_price_setter_lower_price(mocker, samsung_product):
    mocker.patch("src.catalog.input", return_value="y")
    samsung_product.price = 70000

    assert samsung_product.price == 70000


def test_price_setter_negative_price(samsung_product, capsys):
    samsung_product.price = -100

    captured = capsys.readouterr()

    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert samsung_product.price == 180000.0


def test_price_setter_reject_lower_price(mocker, samsung_product):
    mocker.patch("src.catalog.input", return_value="n")
    samsung_product.price = 70000

    assert samsung_product.price == 180000.0


#
# str(product)
#


def test_str_representation_of_product(samsung_product):
    assert (
        str(samsung_product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    )


#
# str(product)
#


def test_str_representation_of_category(samsung_category):
    assert str(samsung_category) == "Смартфоны, количество продуктов: 5 шт"


#
# __add__ product
#


def test_add_products(smartphone_samsung, smartphone_xiaomi, lawngrass_grass):
    assert smartphone_samsung + smartphone_xiaomi == 180000.0 * 5 + 31000.0 * 14

    with pytest.raises(TypeError):
        smartphone_xiaomi + lawngrass_grass


# -----------------
# category
# -----------------


def test_init_category(samsung_category, samsung_product):
    assert samsung_category.name == "Смартфоны"
    assert (
        samsung_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert (
        samsung_category.products
        == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    )
    assert samsung_category.product_count == 1
    assert samsung_category.category_count == 3


#
# add_product in category
#


def test_add_product_to_category(samsung_category, smartphone_xiaomi, lawngrass_grass):
    samsung_category.add_product(smartphone_xiaomi)
    assert smartphone_xiaomi.category == samsung_category
    assert "Xiaomi Redmi Note 11" in samsung_category.products

    samsung_category.add_product(lawngrass_grass)
    assert lawngrass_grass.category == samsung_category
    assert "Газонная трава" in samsung_category.products

    with pytest.raises(TypeError):
        samsung_category.add_product("Not a product")


# -----------------
# Smartphone
# -----------------


def test_init_smartphone(smartphone_xiaomi):
    assert smartphone_xiaomi.name == "Xiaomi Redmi Note 11"
    assert smartphone_xiaomi.description == "1024GB, Синий"
    assert smartphone_xiaomi.price == 31000.0
    assert smartphone_xiaomi.quantity == 14
    assert smartphone_xiaomi.efficiency == 90.3
    assert smartphone_xiaomi.model == "Note 11"
    assert smartphone_xiaomi.memory == 1024
    assert smartphone_xiaomi.color == "Синий"


# -----------------
# LawnGrass
# -----------------


def test_init_lawngrass(lawngrass_grass):
    assert lawngrass_grass.name == "Газонная трава"
    assert lawngrass_grass.description == "Элитная трава для газона"
    assert lawngrass_grass.price == 500.0
    assert lawngrass_grass.quantity == 20
    assert lawngrass_grass.country == "Россия"
    assert lawngrass_grass.germination_period == "7 дней"
    assert lawngrass_grass.color == "Зеленый"
