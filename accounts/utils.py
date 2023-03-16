from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from .models import User
from .threads import SendEmailThread
from .tokens import email_token


def send_email(request, user: User,
               email_subject: str,
               email_template: str) -> None:
    email_subject = email_subject
    email_body = render_to_string(email_template, {
        'user': user,
        'protocol': 'https' if request.is_secure() else 'http',
        'domain': get_current_site(request),
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': email_token.make_token(user),
    })
    email = EmailMessage(subject=email_subject, body=email_body,
                         from_email=settings.EMAIL_FROM_USER, to=[user.email])
    SendEmailThread(email).start()


def get_user_by_uidb64(uidb64: str) -> User | None:
    try:
        user_pk = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=user_pk)
    except:
        user = None

    return user


def get_absolute_url(request, url_name: str) -> str:
    return request.build_absolute_uri(reverse(url_name))
