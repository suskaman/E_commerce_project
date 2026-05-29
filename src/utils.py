import json
import logging

from config.logging_config import setup_logging
from src.catalog import Category, Product

utils_logger = logging.getLogger("utils")


def get_product_from_json(file_name: str) -> list:
    """get list of products from json file and create a class object"""

    utils_logger.info("START getting list of products from json file")

    try:
        if not isinstance(file_name, str):
            raise TypeError("file_name must be a string")

        with open(file_name, "r", encoding="utf-8") as json_file:
            utils_logger.info(f"open file: {file_name}")
            data = json.load(json_file)

        list_of_products = []

        for category in data:
            for product in category["products"]:
                list_of_products.append(
                    Product(
                        product["name"],
                        product["description"],
                        product["price"],
                        product["quantity"],
                    )
                )

        return list_of_products

    except TypeError as e:
        utils_logger.error(f"ERROR {e}")
        return []

    finally:
        utils_logger.info("START getting list of products from json file")


def get_category_from_json(file_name: str) -> list:
    """get list of categories from json file and create a class object"""

    utils_logger.info("START getting list of categories from json file")

    try:

        if not isinstance(file_name, str):
            raise TypeError("file_name must be a string")

        list_of_product = get_product_from_json(file_name)

        with open(file_name, "r", encoding="utf-8") as json_file:
            utils_logger.info(f"open file: {file_name}")
            data = json.load(json_file)

        list_of_category = []

        for category in data:
            for product in list_of_product:
                if product.category:
                    list_of_category.append(
                        Category(
                            category["name"],
                            category["description"],
                            category["products"],
                        )
                    )

        return list_of_category

    except TypeError as e:
        utils_logger.error(f"ERROR {e}")
        return []

    finally:
        utils_logger.info("END getting list of categories from json file")


if __name__ == "__main__":
    setup_logging()

    cat = get_category_from_json(
        "C:/Users/suska/PycharmProjects/E_commerce_project/data/products.json"
    )

    print(cat)
