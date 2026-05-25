class Product:
    name: str
    description:str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity



class Category:
    name: str
    description: str
    products: list
    category_count: int=0
    product_count: int

    def __init__(self, name, description, products) -> None:
        self.name = name
        self.description = description
        self.products = products
        Category.product_count = len(products)
        Category.category_count += 1