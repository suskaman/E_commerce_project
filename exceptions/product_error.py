class ProductError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Неизвестная ошибка при работе с товарами."

    def __str__(self):
        return self.message


class ProductEmptyError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "товар с нулевым количеством"
