from product import Product

class ShoppingCart:
    def __init__(self) -> None:
        self.__products: list[Product] = []

    @property
    def products(self) -> None:
        return self.__products.copy()

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        
    def is_empty(self) -> bool:
        return len(self.__products) == 0

    def has_products(self) -> bool:
        return not self.is_empty()

