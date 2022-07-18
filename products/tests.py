from django.test import TestCase
from .models import Products
from django.contrib.auth import get_user_model


class ProductsModel(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user('usertest', 'usertest@gmail.com', '1234')

    def test_products(self):
        products = Products(
            index = 1,
            categories = 'phones',
            titles = 'nokia',
            price = '22.50',
            description = 'is a new phone',
            images = 'www.somepage.com/img.jpg',
            reviews = '7 reviews',
            ratings = '2'
        )
        self.assertIs(products.categories, 'phones') 
    
    def test_products_views(self):        
        self.client.login(username='usertest', password='1234')
        response = self.client.get('/products/', follow=True)
        self.assertEqual(response.status_code, 200)