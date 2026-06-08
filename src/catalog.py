class Product:
    name: str
    description: str
    quantity: int
    list_of_products: list = []
    category: Category

    def __init__(self, name, description, price, quantity, category=None) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.category = category
        Product.list_of_products.append(self)

    @classmethod
    def new_product(cls, n_product) -> Product:

        for product in cls.list_of_products:
            if product.name == n_product["name"]:
                product.quantity += n_product["quantity"]

                if product.__price != n_product["price"]:
                    product.__price = max(product.__price, n_product["price"])
            return product

        new_product = cls(
            n_product["name"],
            n_product["description"],
            n_product["price"],
            n_product["quantity"],
        )
        Product.list_of_products.append(new_product)
        return new_product

    @property
    def price(self) -> float | int:
        return self.__price

    @price.setter
    def price(self, price) -> None:
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif price <= self.__price:
            print("Вы действительно хотите установить более низкую цену? y/n")
            if input().lower() == "y":
                self.__price = price


class Category:
    name: str
    description: str
    category_count: int = 0
    product_count: int

    def __init__(self, name, description, products) -> None:
        self.name = name
        self.description = description
        self.__products = products
        Category.product_count = len(self.__products)
        Category.category_count += 1

        for product in self.__products:
            product.category = self

    def add_product(self, product) -> None:
        self.__products.append(product)
        product.category = self
        Category.category_count += 1

    @property
    def products(self) -> str:
        list_products = []

        for product in self.__products:
            list_products.append(
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            )

        return "\n".join(list_products)


if __name__ == "__main__":

    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)

    # print(category1.products)

    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 18000.0,
            "quantity": 5,
        }
    )

    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    # print(new_product.price)
    # new_product.price = 800
    # print(new_product.price)
    # new_product.price = -100
    # print(new_product.price)
    # new_product.price = 0
    # print(new_product.price)
