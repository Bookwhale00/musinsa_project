from django.urls import path
from . import views

urlpatterns = [
    path('product-create/', views.product_create, name='product-create'),
    path('product-list/', views.product_list, name='product-list'),
]
