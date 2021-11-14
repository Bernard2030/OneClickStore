from django.contrib.auth.models import User
from django.test import TestCase
from .models import Product, UserProfile, UserRating


# Create your tests here.
class ProductTests(TestCase):
    """
    Here we'll define the tests that we'll run against our Product models
    """

    @classmethod
    def setUpTestData(cls):
        Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=10.00
        )
        Product.objects.create(name='A product', description='sample description', price=1000.00)
        Product.objects.create(name='Another product', description='description', price=30000.00)
        Product.objects.create(name='A really really long product name', description='description', price=10000.00)

    def test_product_count(self):
        self.assertEqual(Product.objects.count(), 4)

    def test_product_name_length(self):
        test_name = Product(name='A really really long product name')
        self.assertEqual(len(test_name.name), 33)

    def test_product_name_length_short(self):
        test_name = Product(name='A product')
        self.assertEqual(len(test_name.name), 9)

    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')

    def test_product_price_length(self):
        test_price = Product(price=10000.00)
        self.assertEqual(len(str(test_price.price)), 7)

    def test_product_price_length_short(self):
        test_price = Product(price=10.00)
        self.assertEqual(len(str(test_price.price)), 4)

