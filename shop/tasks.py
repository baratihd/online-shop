from celery import shared_task

from django.contrib.auth import get_user_model
from .celery.inform_using_mail import send_mail_to


User = get_user_model()


@shared_task
def add_product_send_email(product_instance):
    """ Send email to every other of the superusers to
        check product which it has added.
    """
    product_creator = product_instance.created_by.username
    product_reference_number = product_instance.reference_number
    subject = f'Create {product_reference_number} by {product_creator}'
    mas = f'A product created by {product_creator} with {product_reference_number} reference number. Please check it.'
    receivers = User.objects.filter(is_superuser=True, email__isnull=False).values_list('email', flat=True)
    send_mail_to(subject, mas, list(receivers))
