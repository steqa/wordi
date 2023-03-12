import json

from django.contrib.auth import authenticate, login, logout
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from pydantic import ValidationError

from .data_classes import UserLoginData, UserRegistrationData
from .decorators import unauthenticated_user
from .forms import CustomUserCreationForm


@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        input_post_json = json.dumps(request.POST)
        try:
            user_data = UserLoginData.parse_raw(input_post_json)
        except ValidationError as e:
            response_status = 400
            response_data = e.json().replace(
                'field required', 'Обязательное поле.')
        else:
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
        finally:
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
        try:
            user_data = UserRegistrationData.parse_raw(input_post_json)
        except ValidationError as e:
            response_status = 400
            response_data = e.json().replace(
                'field required', 'Обязательное поле.')
        else:
            user_data = UserRegistrationData.parse_raw(input_post_json)
            form_data = CustomUserCreationForm(user_data.dict())
            if form_data.is_valid():
                form_data.save()
                response_status = 200
                response_data = {
                    'redirectUrl': request.build_absolute_uri(reverse('login-user'))
                }
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
        finally:
            return JsonResponse(status=response_status,
                                data=json.dumps(response_data), safe=False)
    return render(request, 'accounts/registration.html')
