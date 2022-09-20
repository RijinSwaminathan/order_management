from rest_framework.decorators import api_view

from core import response

# Create your views here.
from order import models as m
from order import serializers as s
from product.models import Product


@api_view(['POST', 'GET', 'DELETE', 'PUT'])
def order_data(request):
    if request.method == 'POST':
        # add order data
        serializer = s.OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order_obj = serializer.save()  # save to db if the data is valid and create a order instance
        product_list = request.POST.getlist('product_id[]')
        quantity_list = request.POST.getlist('quantity[]')
        for i, product_id in enumerate(product_list, 0):
            product_obj = Product.objects.get(id=product_id)
            order_products = m.OrderProducts.objects.create(
                order_id=order_obj,
                product_id=product_obj,
                quantity=quantity_list[i]
            )
            order_products.save()
        return response.created(message='order crested successfully')
    elif request.method == 'GET':
        # get the list of all active orders
        order_obj = m.Order.objects.filter(is_delete=False)
        serializer = s.GetOrderSerializer(order_obj, many=True)
        return response.success_data(data=serializer.data, message='product data fetched successfully')
    elif request.method == 'DELETE':
        # cancel the order
        order_id = request.data.get('order_id')
        order_obj = m.Order.objects.get(id=order_id, is_delete=False)
        order_obj.is_active = False
        order_obj.is_delete = True
        order_obj.save()
        return response.success(message='order canceled successfully')
    elif request.method == 'PUT':
        # deliver the order
        order_id = request.data.get('order_id')
        order_obj = m.Order.objects.get(id=order_id, is_delete=False)
        order_obj.is_delivered = True
        order_obj.save()
        return response.success(message='order delivered successfully')
