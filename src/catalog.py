class Product:
    """The class that represents a product"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity) -> None:
        """Initializing method"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """The class that represents a category"""

    name: str
    description: str
    products: list
    category_count: int = 0
    product_count: int

    def __init__(self, name, description, products) -> None:
        """Initializing method"""
        self.name = name
        self.description = description
        self.products = products
        Category.product_count = len(products)
        Category.category_count += 1
