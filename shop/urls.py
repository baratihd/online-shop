from django.urls import path

from . import views


app_name = 'shop'
urlpatterns = [
    path('product/create/', views.ProductCreateAPIView.as_view(), name='product-create'),
    path('remove-unsold-product/', views.RemoveUnsoldProducts.as_view(), name='remove-unsold-product'),
]
