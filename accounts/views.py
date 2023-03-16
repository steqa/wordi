import json

from django.contrib.auth import authenticate, login, logout
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse

from . import constants
from .data_classes import UserLoginData, UserRegistrationData
from .decorators import unauthenticated_user
from .forms import CustomUserCreationForm
from .models import User
from .threads import DeleteUserAfterTimeElapsed
from .tokens import email_token
from .utils import get_user_by_uidb64, send_email


@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        input_post_json = json.dumps(request.POST)
        user_data = UserLoginData.parse_raw(input_post_json)
        user = authenticate(email=user_data.email,
                            password=user_data.password)
        if user is not None:
            login(request, user)
            response_status = 200
            response_data = {
                'redirectUrl': request.build_absolute_uri(reverse('cards'))
            }
        else:
            response_status = 400
            response_data = {
                'msg': 'Неверный адрес электронной почты или пароль.'
            }
        return JsonResponse(status=response_status,
                            data=json.dumps(response_data), safe=False)
    return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    return redirect('login-user')


@unauthenticated_user
def registration_user(request):
    if request.method == 'POST':
        input_post_json = json.dumps(request.POST)
        user_data = UserRegistrationData.parse_raw(input_post_json)
        form_data = CustomUserCreationForm(user_data.dict())
        if form_data.is_valid():
            user = form_data.save()
            email_subject = 'Wordi: подтверждение адреса электронной почты'
            email_template = 'accounts/registration-verification/email.html'
            send_email(request, user,
                       email_subject=email_subject,
                       email_template=email_template)
            DeleteUserAfterTimeElapsed(
                user, constants.LIFETIME_EMAIL_USER_ACTIVATION).start()
            response_status = 200
            template = render_to_string(
                request=request, context={'user': user},
                template_name='accounts/registration-verification/request.html'
            )
            response_data = {'renderTemplate': template}
        else:
            response_status = 400
            response_data = {
                'errors': form_data.errors.as_json().replace(
                    'email', 'formEmail').replace(
                    'first_name', 'formFirstName').replace(
                    'last_name', 'formLastName').replace(
                    'password1', 'formPassword1').replace(
                    'password2', 'formPassword2')
            }

        return JsonResponse(status=response_status,
                            data=json.dumps(response_data), safe=False)
    return render(request, 'accounts/registration.html')


@unauthenticated_user
def activate_user(request, uidb64: str, token: str):
    user = get_user_by_uidb64(uidb64)
    if (user is not None
        and email_token.check_token(
            user, token, constants.LIFETIME_EMAIL_USER_ACTIVATION)
            and not user.is_email_verified):
        user.is_email_verified = True
        user.save()
        return redirect('login-user')
    else:
        return render(request,
                      'accounts/registration-verification/fail.html')
