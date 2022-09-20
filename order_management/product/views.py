
# Create your views here.
from rest_framework.decorators import api_view

from core import response
from product import serializer as s
from product import models as m


@api_view(['POST', 'GET'])
def product_data(request):
    if request.method == 'POST':  # add product data
        serializer = s.ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()  # save to db if the data is valid
            return response.created(message='product data created successfully')
        return response.invalid_data(message=serializer.errors)
    if request.method == 'GET':
        # get the list of all products
        product_obj = m.Product.objects.all()
        serializer = s.ProductSerializer(product_obj, many=True)
        return response.success_data(data=serializer.data, message='product data fetched successfully')

