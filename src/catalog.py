from pygments.formatters import other


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

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return self.price*self.quantity + other.price*other.quantity


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
            list_products.append(str(product) + '\n')

        return "\n".join(list_products)

    def __str__(self):
        count = 0
        for product in self.__products:
            count += product.quantity

        return f"{self.name}, количество продуктов: {count} шт"

if __name__ == "__main__":
    pass
