from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import ProductModel
from .serializer import ProductModelSerializer
from .constants import messages_constants


class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'size'


class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductModelSerializer
    permission_classes = (IsAdminUser, )

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        return super().perform_create(serializer)


class ProductListAPIView(ListAPIView):
    permission_classes = (AllowAny, )
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = {
        'category__title': ['exact'],
        'created_at': ['let', 'gte'],
        'price': ['let', 'gte'],
        'title': ['exact'],
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        is_admin = user.is_staff or user.is_superuser
        number_of_objects = 1001 if is_admin else 101
        return queryset[:number_of_objects]


class RemoveUnsoldProducts(APIView):
    permission_classes = (IsAdminUser, )

    def post(self, request):
        number_of_unsold_product = ProductModel.objects.filter(number_of_sales=0).delete()
        if number_of_unsold_product:
            return Response(
                messages_constants.REMOVE_PRODUCTS_WHICH_HAS_NOT_SOLD_YET % number_of_unsold_product,
                status=status.HTTP_200_OK
            )
