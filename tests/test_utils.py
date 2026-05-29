from src.utils import get_category_from_json, get_product_from_json


def test_get_product_from_json():
    assert (
        type(get_product_from_json("../E_commerce_project/data/products.json")) == list
    )
    assert get_product_from_json("../E_commerce_project/data/products.json") != []


def test_get_category_from_json():
    assert (
        type(get_category_from_json("../E_commerce_project/data/products.json")) == list
    )
    assert get_category_from_json("../E_commerce_project/data/products.json") != []
