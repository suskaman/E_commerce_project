from abc import ABC, abstractmethod


class BaseProduct(ABC):
    name: str
    description: str
    quantity: int

    @abstractmethod
    def __init__(self, name, description, price, quantity) -> None:
        pass

    @abstractmethod
    def new_product(self, n_product) -> Product:
        pass

    @property
    @abstractmethod
    def price(self) -> float | int:
        pass

    @price.setter
    @abstractmethod
    def price(self, price) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class MixinLog:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"Создан объект: {self!r}")


class Product(MixinLog, BaseProduct):

    list_of_products: list = []
    category: Category

    def __init__(self, name, description, price, quantity, category=None) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.category = category
        Product.list_of_products.append(self)
        super().__init__(name, description, price, quantity)

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
        if type(self) == type(other):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError

    def __repr__(self):
        return (
            f"{self.__class__.__name__}('{self.name}', '{self.description}', "
            f"{self.price}, {self.quantity})"
        )


class EvenProduct:

    def __init__(self, category):
        self.category = category

    def __iter__(self):
        self.id = -1
        return self

    def __next__(self):
        list_of_products = self.category.products.split("\n")

        if self.id + 1 < len(list_of_products):
            self.id += 1
            return list_of_products[self.id]
        else:
            raise StopIteration


class Smartphone(Product):
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    germination_period: str
    color: str

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class BaseEntity(ABC):
    def __init__(self, *args, **kwargs) -> None:
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass


class Category(MixinLog, BaseEntity):
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
        super().__init__(name, description, products)

        for product in self.__products:
            product.category = self

    def add_product(self, product) -> None:
        if isinstance(product, Product):
            self.__products.append(product)
            product.category = self
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self) -> str:
        return "\n".join(str(product) for product in self.__products)

    def __str__(self):
        count = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {count} шт"

    def __repr__(self):
        products = [product.name for product in self.__products]
        return f"{self.__class__.__name__}('{self.name}', {products})"


class Order(MixinLog, BaseEntity):
    product: Product
    quantity: int
    total_price: float

    def __init__(self, product, quantity) -> None:
        self.product = product
        self.quantity = quantity
        self.total_price = quantity * product.price
        super().__init__(product, quantity)

    def __str__(self):
        return (f"Заказ на {self.product.name} в количестве {self.quantity}шт."
                f" общей стоимостью в {self.total_price}руб.")

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.product.name}', '{self.quantity}', '{self.total_price}')"


if __name__ == "__main__":
    pass
