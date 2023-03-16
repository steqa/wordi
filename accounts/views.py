import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from wordi import settings

from .data_classes import (EmailData, UserLoginData, UserRegistrationData,
                           UserResetPasswordData)
from .decorators import unauthenticated_user
from .forms import (CustomSetPasswordForm, CustomUserCreationForm,
                    PasswordResetForm)
from .models import User
from .threads import DeleteUserAfterTimeElapsed
from .tokens import email_token
from .utils import get_absolute_url, get_user_by_uidb64, send_email


@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        post_json = json.dumps(request.POST)
        data = UserLoginData.parse_raw(post_json)
        user = authenticate(email=data.email, password=data.password)
        if user:
            login(request, user)

            json_status = 200
            redirect_url = get_absolute_url(request, 'cards')
            json_data = {'redirectUrl': redirect_url}
        else:
            json_status = 400
            error_message = 'Неверный адрес электронной почты или пароль.'
            json_data = {'msg': error_message}

        return JsonResponse(status=json_status, data=json_data)
    return render(request, 'accounts/login.html')


@login_required
def logout_user(request):
    logout(request)
    return redirect('login-user')


@unauthenticated_user
def registration_user(request):
    if request.method == 'POST':
        post_json = json.dumps(request.POST)
        data = UserRegistrationData.parse_raw(post_json)
        form_data = CustomUserCreationForm(data.dict())
        if form_data.is_valid():
            user = form_data.save()
            email_subject = 'Wordi: подтверждение адреса электронной почты'
            email_template = 'accounts/registration-verification/email.html'
            send_email(request, user,
                       email_subject=email_subject,
                       email_template=email_template)
            user_lifetime = settings.LIFETIME_EMAIL_USER_ACTIVATION
            DeleteUserAfterTimeElapsed(user, user_lifetime).start()

            json_status = 200
            template_name = 'accounts/registration-verification/request.html'
            context = {'user': user}
            template = render_to_string(template_name, context, request)
            json_data = {'renderTemplate': template}
        else:
            json_status = 400
            errors = form_data.errors.as_json()
            errors = errors.replace('email', 'formEmail')
            errors = errors.replace('first_name', 'formFirstName')
            errors = errors.replace('last_name', 'formLastName')
            errors = errors.replace('password1', 'formPassword1')
            errors = errors.replace('password2', 'formPassword2')
            json_data = {'errors': errors}

        return JsonResponse(status=json_status, data=json_data)
    return render(request, 'accounts/registration.html')


@unauthenticated_user
def activate_user(request, uidb64: str, token: str):
    user = get_user_by_uidb64(uidb64)
    allowed_token_lifetime = settings.LIFETIME_EMAIL_USER_ACTIVATION
    token_is_valid = email_token.check_token(
        user, token, allowed_token_lifetime)
    if ((token_is_valid) and (user) and (not user.is_email_verified)):
        user.is_email_verified = True
        user.save()
        return redirect('login-user')
    else:
        return render(request, 'accounts/registration-verification/fail.html')


@unauthenticated_user
def reset_password(request):
    if request.method == 'POST':
        post_json = json.dumps(request.POST)
        data = EmailData.parse_raw(post_json)
        form_data = PasswordResetForm(data.dict())
        if form_data.is_valid():
            user = User.objects.filter(email=data.email).first()
            if user:
                email_subject = 'Wordi: восстановление пароля'
                email_template = 'accounts/reset-password/email.html'
                send_email(request, user,
                           email_subject=email_subject,
                           email_template=email_template)

                json_status = 200
                template_name = 'accounts/reset-password/request.html'
                context = {'user': user}
                template = render_to_string(template_name, context, request)
                json_data = {'renderTemplate': template}
            else:
                json_status = 400
                error_message = 'Пользователь с таким адресом' \
                                'электронной почты не найден.'
                json_data = {'msg': error_message}
        else:
            json_status = 400
            errors = form_data.errors.as_json()
            errors = errors.replace('email', 'formEmail')
            json_data = {'errors': errors}

        return JsonResponse(status=json_status, data=json_data)
    return render(request, 'accounts/reset-password/reset-password.html')


@unauthenticated_user
def reset_password_confirm(request, uidb64: str, token: str):
    user = get_user_by_uidb64(uidb64)
    allowed_token_lifetime = settings.LIFETIME_EMAIL_RESET_PASSWORD
    token_is_valid = email_token.check_token(
        user, token, allowed_token_lifetime)
    if (token_is_valid and user):
        if request.method == 'POST':
            post_json = json.dumps(request.POST)
            data = UserResetPasswordData.parse_raw(post_json)
            form_data = CustomSetPasswordForm(user, data.dict())
            if form_data.is_valid():
                form_data.save()

                json_status = 200
                redirect_url = get_absolute_url(request, 'login-user')
                json_data = {'redirectUrl': redirect_url}
            else:
                json_status = 400
                errors = form_data.errors.as_json()
                errors = errors.replace('new_password1', 'formNewPassword1')
                errors = errors.replace('new_password2', 'formNewPassword2')
                json_data = {'errors': errors}

            return JsonResponse(status=json_status, data=json_data)

        return render(request, 'accounts/reset-password/confirm.html')
    else:
        return render(request, 'accounts/reset-password/fail.html', {'user': user})
