def test_init_product(samsung_product):
    assert samsung_product.name == "Samsung Galaxy S23 Ultra"
    assert samsung_product.description == "256GB, Серый цвет, 200MP камера"
    assert samsung_product.price == 180000.0
    assert samsung_product.quantity == 5


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
