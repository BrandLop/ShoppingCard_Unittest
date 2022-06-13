import unittest
from product import Product

class TestShoppingCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('The setUpClass called once before all tests')
    
    @classmethod
    def tearDownClass(cls):
        print('The tearDownClass called once after all tests')

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
    
    def test_product_name(self):
        self.assertEqual(self.smart_phone.name, self.name)
    
    def test_product_price(self):
        self.assertEqual(self.smart_phone.price, self.price)

if __name__ == '__main__':
    unittest.main()