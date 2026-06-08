from src.catalog import Product

#
# product
#


def test_init_product(samsung_product):
    assert samsung_product.name == "Samsung Galaxy S23 Ultra"
    assert samsung_product.description == "256GB, Серый цвет, 200MP камера"
    assert samsung_product.price == 180000.0
    assert samsung_product.quantity == 5


def test_product_added_to_list(samsung_product):
    assert samsung_product in Product.list_of_products


#
# category
#


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
    assert samsung_category.category_count == 1


def test_add_product(samsung_category, iphone_product):
    samsung_category.add_product(iphone_product)

    assert iphone_product.category == samsung_category
    assert "Iphone 15" in samsung_category.products


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
