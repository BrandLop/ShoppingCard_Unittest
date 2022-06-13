import unittest
from product import Product

class TestShoppingCart(unittest.TestCase):

    def setUp(self) -> None:
        self.name = 'Samsung'
        self.price = 500.0
        self.smart_phone = Product(self.name, self.price)

    def tearDown(self) -> None:
        pass

    def test_product_object(self):
        name = 'Apple'
        price = 1.70

        product = Product(name, price)  
        self.assertEqual(product.name, name)
        self.assertEqual(product.price, price, 'Price is not correct')

if __name__ == '__main__':
    unittest.main()