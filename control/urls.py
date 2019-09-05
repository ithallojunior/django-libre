from django.urls import path
from .views import list_products, create_products, update_products,  delete_products
from .views import list_orders, create_orders, update_orders, delete_orders

urlpatterns = [
    path('', list_products, name='list_products'),
    path('new', create_products, name='create_products'),
    path('update/<int:id>/', update_products, name='update_products'),
    path('delete/<int:id>/', delete_products, name='delete_products'),

    path('orders', list_orders, name='list_orders'),
    path('newOrder/<int:id>/', create_orders, name='create_orders'),
    path('orderUpadate/<int:id>/', update_orders, name='update_orders'),
    path('orderDelete/<int:id>/', delete_orders, name='delete_orders'),
]
