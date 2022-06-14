import unittest
from product import Product
from product import ProductDiscountError
from shopping_cart import ShoppingCart

def is_avilable_to_skip():
    return True
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

    def test_product_in_shopping_cart(self):
        self.assertIn(self.smart_phone, self.shopping_cart_2.products, 'Product is not in shopping cart')

        product = Product('Glasses', 15.0)
        self.shopping_cart_2.add_product(product)
        self.assertIn(product, self.shopping_cart_2.products, 'Product is not in shopping cart')

    def test_product_not_in_shopping_cart(self):
        self.shopping_cart_2.remove_product(self.smart_phone)

        self.assertNotIn(self.smart_phone, self.shopping_cart_2.products, 'Product is still in shopping cart')

    def test_discount_error(self):
        with self.assertRaises(ProductDiscountError):
            Product(name = 'Glasses', price = 15.0, discount = 20.0)      

    def test_total_shopping_cart(self):
        self.shopping_cart.add_product(Product(name='Book', price=15.0))
        self.shopping_cart.add_product(Product(name='Camera', price=700.0, discount=70.0))
        self.shopping_cart.add_product(Product(name='PC', price=1000.0, discount=0.0))

        self.assertGreater(self.shopping_cart.total, 0, 'Total is not greater than 0')
        self.assertLess(self.shopping_cart.total, 2000.0, 'Total is not less than 2000.0')
        self.assertEqual(self.shopping_cart.total, 1645.0, 'Total is not correct')

    def test_total_empty_shoping_cart(self):
        self.assertEqual(self.shopping_cart.total, 0, 'Total is not 0')

    @unittest.skip('Not implemented')
    def test_skip_example(self):
        self.assertEqual(1, 1)

    @unittest.skipIf(is_avilable_to_skip(), 'Not needed')
    def test_skip_example_2(self):
        self.assertEqual(10, 10)

if __name__ == '__main__':
    unittest.main()