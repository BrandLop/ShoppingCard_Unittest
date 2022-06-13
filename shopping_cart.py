from product import Product

class ShoppingCart:
    def __init__(self) -> None:
        self.__products: list[Product] = []

    def is_empty(self) -> bool:
        return len(self.__products) == 0

    def has_products(self) -> bool:
        return not self.is_empty()

