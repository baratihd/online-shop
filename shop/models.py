import random

from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.exceptions import ValidationError

from .constants import models_verbose_names, messages_constants


User = get_user_model()
random.seed(timezone.now())


class CategoryModel(models.Model):
    parent = models.ForeignKey(
        'self',
        related_name='children',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    title = models.CharField(
        max_length=70,
        verbose_name=models_verbose_names.TITLE
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=models_verbose_names.CREATED_AT
    )

    class Meta:
        verbose_name = models_verbose_names.CATEGORY
        verbose_name_plural = models_verbose_names.CATEGORIES

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # prevent a category to be itself parent
        if self.id and self.parent and self.id == self.parent.id:
            self.parent = None
        super().save(*args, **kwargs)


class ProductModel(models.Model):

    @staticmethod
    def create_new_ref_number():
        """ Generate a random unique of 10-digit number """
        return str(random.randint(1000000000, 9999999999))

    category = models.ForeignKey(
        'shop.CategoryModel',
        on_delete=models.CASCADE,
        verbose_name=models_verbose_names.CATEGORY
    )
    reference_number = models.CharField(
        max_length=10,
        editable=False,
        unique=True,
        default=create_new_ref_number,
        verbose_name=models_verbose_names.REFERENCE_NUMBER
    )
    title = models.CharField(
        max_length=100,
        verbose_name=models_verbose_names.TITLE
    )
    description = models.TextField(
        max_length=1000,
        blank=True,
        verbose_name=models_verbose_names.DESCRIPTION
    )
    number_of_sales = models.IntegerField(
        default=0,
        verbose_name=models_verbose_names.NUMBER_OF_SALES
    )
    price = models.BigIntegerField(
        verbose_name=models_verbose_names.PRICE
    )
    inventory = models.IntegerField(
        verbose_name=models_verbose_names.INVENTORY
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=models_verbose_names.CREATED_AT
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=models_verbose_names.CREATED_BY
    )

    class Meta:
        verbose_name = models_verbose_names.PRODUCT
        verbose_name_plural = models_verbose_names.PRODUCTS

    def __str__(self):
        return str(self.reference_number)

    def clean(self):
        print()
        has_not_permission_to_create_product = not (self.created_by.is_staff or self.created_by.is_superuser)
        if has_not_permission_to_create_product:
            raise ValidationError(messages_constants.THIS_USER_HAS_NOT_PERMISSION_TO_CREATE_PRODUCT)
        return super().clean()
