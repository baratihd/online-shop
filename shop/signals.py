from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ProductModel
from .tasks import add_product_send_email


@receiver(post_save, sender=ProductModel)
def send_email_after_create_product(sender, instance, created, **kwargs):
    if created:
        add_product_send_email(instance)
    return None
