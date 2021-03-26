import random

from django.core.mail import send_mail


def generate_confirm_code():
    return random.randint(100000, 999999)


def send_mail_func(email, confirmation_code):
    send_mail(
        subject='Код подтверждения Yamdb',
        message=f'Код подтверждения {confirmation_code}',
        from_email='admin@yamdb.test',
        recipient_list=[email],
        fail_silently=False
    )
