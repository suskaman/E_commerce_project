from src.utils import get_data_from_json


def test_get_data_from_json():
    assert type(get_data_from_json("../E_commerce_project/data/products.json")) == tuple
    assert get_data_from_json("../E_commerce_project/data/products.json") != ()


def test_get_data_from_json_type_error():
    result = get_data_from_json(123)
    assert result == ()


def test_get_data_from_json_empty_string():
    result = get_data_from_json("")

    assert result == ()
