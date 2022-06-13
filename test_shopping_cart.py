import unittest
from product import Product
from shopping_cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self) -> None:
        self.name = 'Samsung'
        self.price = 500.0
        self.smart_phone = Product(self.name, self.price)
        self.shopping_cart = ShoppingCart()
        self.shopping_cart_2 = ShoppingCart()
        self.shopping_cart_2.add_product(self.smart_phone)

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

    def test_shopping_cart_is_empty(self):
        self.assertTrue(self.shopping_cart.is_empty(), 'Shopping cart is not empty')

    def test_shopping_cart_has_product(self):
        self.assertTrue(self.shopping_cart_2.has_products(), 'Shopping cart has no products')
        self.assertFalse(self.shopping_cart_2.is_empty(), 'Shopping cart is empty')

if __name__ == '__main__':
    unittest.main()