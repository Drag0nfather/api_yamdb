import random

from django.core.mail import send_mail
from django.utils.crypto import salted_hmac
from django.utils.http import int_to_base36


def generate_confirm_code(self, user, timestamp):
    # timestamp is number of seconds since 2001-1-1. Converted to base 36,
    # this gives us a 6 digit string until about 2069.
    ts_b36 = int_to_base36(timestamp)
    hash_string = salted_hmac(
        self.key_salt,
        self._make_hash_value(user, timestamp),
        secret=self.secret,
        algorithm=self.algorithm,
    ).hexdigest()[::2]  # Limit to shorten the URL.
    return "%s-%s" % (ts_b36, hash_string)


def send_mail_func(email, confirmation_code):
    send_mail(
        subject='Код подтверждения Yamdb',
        message=f'Код подтверждения {confirmation_code}',
        recipient_list=[email],
        fail_silently=False
    )
