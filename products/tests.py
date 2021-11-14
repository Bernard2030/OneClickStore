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

    def test_product_price_length_long(self):
        test_price = Product(price=100000.00)
        self.assertEqual(len(str(test_price.price)), 8)


class UserProfileTests(TestCase):
    """
    Here we'll define the tests that we'll run against our UserProfile models
    """

    def setUp(self):
        self.user = User(id=1, username='zoo', password='testpwsd123')
        self.user.save()
        self.user_2 = User(id=2, username='zoo2', password='testpwsd123')
        self.user_2.save()

    """
        @classmethod
        def setUpTestData(cls):
            UserProfile.objects.create(user=User.objects.get(id=1))
            UserProfile.objects.create(user=User.objects.get(id=2))
    """

    def tearDown(self):
        self.user = None
        self.user_2 = None

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()

    def test_update_user(self):
        self.user.username = 'zken'
        self.user.save()

    def test_get_user(self):
        self.user.username = 'zken'
        self.user.save()
        user = User.objects.get(id=1)
        self.assertEquals(user.username, 'zken')

    def test_get_all_users(self):
        self.user.username = 'zken'
        self.user_2.username = 'zken2'
        self.user.save()
        self.user_2.save()
        users = User.objects.all()
        self.assertEquals(len(users), 2)

    def test_get_all_users_by_id(self):
        self.user.username = 'zken'
        self.user.save()
        users = User.objects.all()
        self.assertEquals(users[0].id, 2)

    def test_get_all_users_by_username(self):
        self.user.username = 'zken'
        self.user.save()
        users = User.objects.all()
        self.assertEquals(users[1].username, 'zken')

    def test_get_user_profile(self):
        self.user.username = 'zken'
        self.user.save()
        user_profile = UserProfile.objects.get(user=self.user)
        self.assertEquals(user_profile.user, self.user)

