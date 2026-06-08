import json
import logging

from config.logging_config import setup_logging
from src.catalog import Category, Product

utils_logger = logging.getLogger("utils")


def get_data_from_json(file_name: str) -> tuple:
    """get lists of categories and products from json file and create a class object"""

    utils_logger.info("START getting list of products from json file")

    try:
        if not isinstance(file_name, str):
            raise TypeError("file_name must be a string")
        if file_name == "":
            raise ValueError("file_name must be a string")

        with open(file_name, "r", encoding="utf-8") as json_file:
            utils_logger.info(f"open file: {file_name}")
            data = json.load(json_file)

        list_of_product = []
        list_of_category = []
        for category in data:
            cat = Category(
                category["name"],
                category["description"],
                []
            )

            for product in category["products"]:
                prod = Product(
                                product["name"],
                                product["description"],
                                product["price"],
                                product["quantity"],
                                cat
                )

                list_of_product.append(prod)
                cat.add_product(prod)

            list_of_category.append(cat)

        return list_of_category, list_of_product

    except TypeError as e:
        utils_logger.error(f"ERROR {e}")
        return ()
    except ValueError as e:
        utils_logger.error(f"ERROR {e}")
        return ()

    finally:
        utils_logger.info("START getting list of products from json file")


if __name__ == "__main__":
    setup_logging()

    categories, products = get_product_from_json(
        "C:/Users/suska/PycharmProjects/E_commerce_project/data/products.json"
    )

    print(categories[1].name)
    print(products)
