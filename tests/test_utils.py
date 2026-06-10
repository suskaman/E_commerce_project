from src.utils import get_data_from_json


def test_get_data_from_json():
    assert type(get_data_from_json("../E_commerce_project/data/products.json")) == tuple
    assert get_data_from_json("../E_commerce_project/data/products.json") != ()
