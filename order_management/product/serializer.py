from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product  # model that being serialized
        fields = (
            'id',
            'product_name',
            'product_type',
            'product_price'
        )
