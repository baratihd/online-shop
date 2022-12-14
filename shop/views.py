from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
)
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from index.permissions import IsAdminOwnerOrReadOnly
from index.paginations import CustomPageNumberPagination
from .models import ProductModel
from .serializer import ProductModelSerializer
from .constants import messages_constants


class ProductCreateAPIView(CreateAPIView):
    """
    This view can create a product by admin user.
    It set product creator automatically.
    """
    serializer_class = ProductModelSerializer
    permission_classes = (IsAdminUser, )

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        return super().perform_create(serializer)


class ProductListAPIView(ListAPIView):
    """
    This API can return list of products.
    It can filter by date range of create products
    with `created_at` key. And also it filter
    range of prices. \n
    User can set size of pagination by `size` key
    in query params. \n
    ?size=10 \n
    Maximum number of products for admin users
    is 1000 and for other users is 100.
    """
    permission_classes = (AllowAny, )
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = {
        'created_at': ['lte', 'gte'],
        'price': ['lte', 'gte'],
    }
    search_fields = ('id', 'reference_number', 'category__title', 'title')

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        is_admin = user.is_staff or user.is_superuser
        number_of_objects = 1001 if is_admin else 101
        return queryset[:number_of_objects]


class RemoveUnsoldProducts(APIView):
    """
    This API can remove product which it has not been sold yet. \n
    Tips: Only superuser or product owner can execute this API.
    """
    permission_classes = (IsAdminOwnerOrReadOnly, )
    lookup_field = 'reference_number'

    def delete(self, request, reference_number):
        instance = get_object_or_404(ProductModel, number_of_sales=0, reference_number=reference_number)
        self.check_object_permissions(request, instance)
        instance.delete()
        return Response(messages_constants.PRODUCT_REMOVED, status=status.HTTP_204_NO_CONTENT)
