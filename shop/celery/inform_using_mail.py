from django.core.mail import send_mail
from django.conf import settings


def send_mail_to(subject, message, receivers):
    send_mail(subject, message, settings.EMAIL_HOST_USER, [receivers], fail_silently=False)
    return None
