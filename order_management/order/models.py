import uuid

from django.db import models


# Create your models here.
class Order(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    order_date = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)

    objects = models.Manager

    class Meta:
        """
            to set table name in database
        """
        db_table = "order"


class OrderProducts(models.Model):
    order_id = models.ForeignKey('order.Order', on_delete=models.CASCADE)
    product_id = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    objects = models.Manager

    class Meta:
        """
            to set table name in database
        """
        db_table = "order_products"
