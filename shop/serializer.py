from rest_framework import serializers

from .models import ProductModel


class ProductModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductModel
        exclude = tuple()
        read_only_fields = (
            'id',
            'reference_number',
            'created_at',
            'created_by',
        )
