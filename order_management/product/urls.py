from django.urls import path

from .views import product_data

urlpatterns = [
    path('product/', product_data, name='manage_product')
]
