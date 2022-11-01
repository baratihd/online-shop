from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import ProductModel
from .serializer import ProductModelSerializer
from .constants import messages_constants


class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductModelSerializer
    permission_classes = (IsAdminUser, )

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        return super().perform_create(serializer)


class RemoveUnsoldProducts(APIView):
    permission_classes = (IsAdminUser, )

    def post(self, request):
        number_of_unsold_product = ProductModel.objects.filter(number_of_sales=0).delete()
        if number_of_unsold_product:
            return Response(
                messages_constants.REMOVE_PRODUCTS_WHICH_HAS_NOT_SOLD_YET % number_of_unsold_product,
                status=status.HTTP_200_OK
            )








