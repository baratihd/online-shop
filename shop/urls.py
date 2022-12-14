from django.urls import path

from .views import (
    ProductCreateAPIView,
    ProductListAPIView,
    RemoveUnsoldProducts,
)


app_name = 'shop'
urlpatterns = [
    path('product/create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('product/<slug:reference_number>/', RemoveUnsoldProducts.as_view(), name='remove-unsold-product'),
]
