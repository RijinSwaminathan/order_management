from django.test import TestCase

from product.models import Product


class TestProduct(TestCase):
    def setUp(self):
        self.product = Product(product_name='Product Name', product_type='Product type', product_price=10.0)

    def test_product(self):
        old_count = Product.objects.count()
        self.product.save()
        new_count = Product.objects.count()
        self.assertNotEqual(old_count, new_count)
