from rest_framework import serializers

from .models import ProductModel


class ProductModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductModel
        fields = (
            'id',
            'category',
            'reference_number',
            'title',
            'description',
            'price',
            'inventory',
            'created_at',
            'created_by'
        )
        read_only_fields = (
            'id',
            'reference_number',
            'created_at',
            'created_by'
        )
