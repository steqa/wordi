from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from .models import User
from .threads import SendEmailThread
from .tokens import email_token


def send_email(request, user: User, email_subject: str, email_template: str):
    email_subject = email_subject
    email_body = render_to_string(email_template, {
        'user': user,
        'domain': get_current_site(request),
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': email_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http',
    })
    email = EmailMessage(subject=email_subject, body=email_body,
                         from_email=settings.EMAIL_FROM_USER, to=[user.email])

    SendEmailThread(email).start()
