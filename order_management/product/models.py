import uuid

from django.db import models


# Create your models here.
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    product_name = models.CharField(max_length=50)
    product_type = models.CharField(max_length=50)
    product_price = models.FloatField(max_length=20)

    objects = models.Manager

    class Meta:
        """
            to set table name in database
        """
        db_table = "product"

    def __str__(self):
        return self.product_name
