from django.contrib.auth.models import User
from django.test import TestCase
from .models import Product, UserProfile, UserRating, ProductSale, UserReview, Category


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


class UserRatingTests(TestCase):
    """
    Tests of user rating model
    """

    def setUp(self):
        self.user = User(id=1, username='zoo', password='testpwsd123')
        self.user.save()
        self.user_2 = User(id=2, username='zoo2', password='testpwsd123')
        self.user_2.save()
        self.rating = UserRating(id=1, rating=5, user=self.user)
        self.rating.save()
        self.rating_2 = UserRating(id=2, rating=4, user=self.user_2)
        self.rating_2.save()

    def tearDown(self):
        self.user = None
        self.user_2 = None
        self.rating = None
        self.rating_2 = None

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, UserRating))

    def test_save_rating(self):
        self.rating.save()

    def test_delete_rating(self):
        self.rating.delete()

    def test_update_rating(self):
        self.rating.rating = 3
        self.rating.save()
        self.assertEquals(self.rating.rating, 3)

    def test_get_rating(self):
        self.rating.rating = 5
        self.rating.save()
        rating = UserRating.objects.get(id=1)
        self.assertEquals(rating.rating, 5)

    def test_get_all_ratings(self):
        self.rating.rating = 5
        self.rating_2.rating = 2
        self.rating.save()
        self.rating_2.save()
        ratings = UserRating.objects.all()
        self.assertEquals(len(ratings), 2)

    def test_get_all_ratings_by_id(self):
        self.rating.rating = 5
        self.rating.save()
        ratings = UserRating.objects.all()
        self.assertEquals(ratings[0].id, 2)

    def test_get_all_ratings_by_rating(self):
        self.rating.rating = 5
        self.rating.save()
        ratings = UserRating.objects.all()
        self.assertEquals(ratings[1].rating, 5)

    def test_get_all_ratings_by_user(self):
        self.rating.rating = 3
        self.rating.save()
        ratings = UserRating.objects.all()
        self.assertEquals(ratings[1].user, self.user)

    def test_get_user_rating(self):
        self.rating.rating = 3
        self.rating.save()
        user_rating = UserRating.objects.get(user=self.user)
        self.assertEquals(user_rating.rating, 3)


class ProductSaleTests(TestCase):
    """

    """

    def setUp(self):
        self.user = User(id=1, username='zoo', password='testpwsd123')
        self.user.save()
        self.user_2 = User(id=2, username='zoo2', password='testpwsd123')
        self.user_2.save()
        self.product = Product(id=1, name='test', price=3110, description='sample test', image='test')
        self.product.save()
        self.product_2 = Product(id=2, name='test2', price=1000, description='test', image='test')
        self.product_2.save()
        self.sale = ProductSale(id=1, sale_price=1000, product=self.product)
        self.sale.save()
        self.sale_2 = ProductSale(id=2, sale_price=1000, product=self.product_2)
        self.sale_2.save()

    def tearDown(self):
        self.user = None
        self.user_2 = None
        self.product = None
        self.product_2 = None
        self.sale = None
        self.sale_2 = None

    def test_instance(self):
        self.assertTrue(isinstance(self.sale, ProductSale))

    def test_save_sale(self):
        self.sale.save()

    def test_delete_sale(self):
        self.sale.delete()

    def test_update_sale(self):
        self.sale.sale_price = 1000
        self.sale.save()
        self.assertEquals(self.sale.sale_price, 1000)

    def test_get_sale(self):
        self.sale.sale_price = 1000
        self.sale.save()
        sale = ProductSale.objects.get(id=1)
        self.assertEquals(sale.sale_price, 1000)

    def test_get_all_sales(self):
        self.sale.sale_price = 3000
        self.sale_2.sale_price = 10220
        self.sale.save()
        self.sale_2.save()
        sales = ProductSale.objects.all()
        self.assertEquals(len(sales), 2)

    def test_get_all_sales_by_id(self):
        self.sale.sale_price = 3000
        self.sale.save()
        sales = ProductSale.objects.all()
        self.assertEquals(sales[0].id, 2)

    def test_get_all_sales_by_sale_price(self):
        self.sale.sale_price = 3000
        self.sale.save()
        sales = ProductSale.objects.all()
        self.assertEquals(sales[1].sale_price, 3000)

    def test_get_all_sales_by_product(self):
        self.sale.sale_price = 3000
        self.sale.save()
        sales = ProductSale.objects.all()
        self.assertEquals(sales[1].product, self.product)

    def test_get_product_sale(self):
        self.sale.sale_price = 3000
        self.sale.save()
        sale = ProductSale.objects.get(product=self.product)
        self.assertEquals(sale.sale_price, 3000)

    def test_get_product_sale_by_id(self):
        self.sale.sale_price = 8000
        self.sale.save()
        sale = ProductSale.objects.get(id=1)
        self.assertEquals(sale.sale_price, 8000)

    def test_get_product_sale_by_sale_price(self):
        self.sale.sale_price = 7070
        self.sale.save()
        sale = ProductSale.objects.get(sale_price=7070)
        self.assertEquals(sale.sale_price, 7070)

    def test_get_product_sale_by_product(self):
        self.sale.sale_price = 7070
        self.sale.save()
        sale = ProductSale.objects.get(product=self.product)
        self.assertEquals(sale.sale_price, 7070)

    def test_get_product_sale_by_product_id(self):
        self.sale.sale_price = 9038
        self.sale.save()
        sale = ProductSale.objects.get(product=self.product.id)
        self.assertEquals(sale.sale_price, 9038)


class CategoryTests(TestCase):

    def setUp(self):
        self.user = User(id=1, username='zoo', password='testpwsd123')
        self.user.save()
        self.user_2 = User(id=2, username='zoo2', password='testpwsd123')
        self.user_2.save()
        self.category = Category(id=1, name='test')
        self.category.save()
        self.category_2 = Category(id=2, name='test2')
        self.category_2.save()

    def tearDown(self):
        self.user = None
        self.user_2 = None
        self.category = None
        self.category_2 = None

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save()

    def test_delete_category(self):
        self.category.delete()

    def test_update_category(self):
        self.category.name = 'test'
        self.category.save()
        self.assertEquals(self.category.name, 'test')

    def test_get_category(self):
        self.category.name = 'test'
        self.category.save()
        category = Category.objects.get(id=1)
        self.assertEquals(category.name, 'test')

    def test_get_all_categories(self):
        self.category.name = 'test'
        self.category_2.name = 'test2'
        self.category.save()
        self.category_2.save()
        categories = Category.objects.all()
        self.assertEquals(len(categories), 2)

    def test_get_all_categories_by_id(self):
        self.category.name = 'test'
        self.category.save()
        categories = Category.objects.all()
        self.assertEquals(categories[0].id, 2)

    def test_get_all_categories_by_name(self):
        self.category.name = 'test'
        self.category.save()
        categories = Category.objects.all()
        self.assertEquals(categories[1].name, 'test')

    def test_get_category_by_name(self):
        self.category.name = 'test'
        self.category.save()
        category = Category.objects.get(name='test')
        self.assertEquals(category.name, 'test')

    def test_get_category_by_id(self):
        self.category.name = 'test'
        self.category.save()
        category = Category.objects.get(id=1)
        self.assertEquals(category.name, 'test')

    def test_get_category_by_name_and_id(self):
        self.category.name = 'test'
        self.category.save()
        category = Category.objects.get(name='test', id=1)
        self.assertEquals(category.name, 'test')



