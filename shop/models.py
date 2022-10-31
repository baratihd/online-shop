from django.db import models

from .constants import models_verbose_names


class CategoryModel(models.Model):
    parent = models.ForeignKey(
        'self',
        related_name='children',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=models_verbose_names.PARENT
    )
    title = models.CharField(
        max_length=70,
        verbose_name=models_verbose_names.TITLE
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=models_verbose_names.CREATED_AT
    )
