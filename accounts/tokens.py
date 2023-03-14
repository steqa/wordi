import six
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.crypto import constant_time_compare
from django.utils.http import base36_to_int

from .models import User


class EmailTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user: User, timestamp: int) -> str:
        return six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_email_verified)

    def check_token(self, user, token, token_lifetime_in_sec):
        if not (user and token):
            return False
        try:
            ts_b36, _ = token.split("-")
        except ValueError:
            return False

        try:
            ts = base36_to_int(ts_b36)
        except ValueError:
            return False

        for secret in [self.secret, *self.secret_fallbacks]:
            if constant_time_compare(
                self._make_token_with_timestamp(user, ts, secret),
                token,
            ):
                break
        else:
            return False

        if (self._num_seconds(self._now()) - ts) > token_lifetime_in_sec:
            return False

        return True


email_token = EmailTokenGenerator()
