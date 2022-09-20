from rest_framework import serializers

from order.models import Order, OrderProducts
from product.models import Product


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order  # model that being serialized
        fields = (
            '__all__'
        )


class GetOrderSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    order_date = serializers.DateTimeField(read_only=True)
    is_delete = serializers.BooleanField(read_only=True)
    is_delivered = serializers.BooleanField(read_only=True)
    product_data = serializers.SerializerMethodField(read_only=True)

    def get_product_data(self, obj):
        # get the product data under each order
        if OrderProducts.objects.filter(order_id=obj.id).exists():
            ordered_product = OrderProducts.objects.filter(order_id=obj.id).values()
            product_list = []
            for product_data in ordered_product:
                product_obj = Product.objects.get(id=product_data.get('product_id_id'))
                product_list.append({
                    'product_name': product_obj.product_name,
                    'product_type': product_obj.product_type,
                    'amount': product_obj.product_price * product_data.get('quantity')
                })
            return product_list
