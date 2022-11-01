from celery import shared_task

from django.contrib.auth import get_user_model
from .celery.inform_using_mail import send_mail_to


User = get_user_model()


@shared_task
def add_product_send_email(product_instance):
    product_creator = product_instance.created_by.username
    product_reference_number = product_instance.reference_number
    subject = f'Create {product_reference_number} by {product_creator}'
    messages = (f'A product created by {product_creator} with {product_reference_number} reference number.',
                ' Please check it.')
    receivers = User.objects.filter(is_superuser=True).values_list('email', flat=True)
    send_mail_to(subject, messages, receivers)
