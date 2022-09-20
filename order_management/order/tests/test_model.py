from datetime import datetime

from django.test import TestCase

from order.models import Order, OrderProducts
from product.models import Product


class TestOrder(TestCase):
    def setUp(self):
        self.order = Order(order_date=datetime.now(), is_delete=False,
                           is_delivered=False)

    def test_order(self):
        old_count = Order.objects.count()
        self.order.save()
        new_count = Order.objects.count()
        self.assertNotEqual(old_count, new_count)


class TestProductsOrder(TestCase):
    def setUp(self):
        self.order = Order.objects.create(order_date=datetime.now(), is_delete=False,
                                          is_delivered=False)
        self.product = Product.objects.create(product_name='Product Name', product_type='Product type',
                                              product_price=10.0)
        self.order_product = OrderProducts(order_id=self.order, product_id=self.product, quantity=2)

    def test_order_product(self):
        old_count = OrderProducts.objects.count()
        self.order_product.save()
        new_count = OrderProducts.objects.count()
        self.assertNotEqual(old_count, new_count)
