from django.urls import path

from .views import order_data

urlpatterns = [
    path('order/', order_data, name='manage_order')
]
