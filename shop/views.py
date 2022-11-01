from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser

from .serializer import ProductModelSerializer


class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductModelSerializer
    permission_classes = (IsAdminUser, )
