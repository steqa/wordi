import json

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import render

from accounts.data_classes import UserChangeData, UserChangePasswordData
from accounts.forms import CustomPasswordChangeForm
from accounts.utils import get_absolute_url

from .utils import (edit_user, get_personal_data_errors,
                    password_data_is_not_empty)


@login_required
def edit_userprofile(request):
    if request.method == 'POST':
        post_json = json.dumps(request.POST)

        personal_data = UserChangeData.parse_raw(post_json)
        personal_data_errors = get_personal_data_errors(personal_data)

        password_data = UserChangePasswordData.parse_raw(post_json)
        password_form_data = CustomPasswordChangeForm(
            request.user, password_data.dict())
        if password_data_is_not_empty(password_data):
            password_data_errors = dict(password_form_data.errors)
            save_password = True
        else:
            password_data_errors = {}
            save_password = False

        if (personal_data_errors == {}) and (password_data_errors == {}):
            if save_password:
                password_form_data.save()

            user = edit_user(request.user, personal_data)
            login(request, user)

            json_status = 200
            redirect_url = get_absolute_url(request, 'edit-userprofile')
            json_data = {'redirectUrl': redirect_url}
        else:
            json_status = 400
            errors = json.dumps(dict(**personal_data_errors,
                                     **password_data_errors))
            errors = errors.replace('email', 'formEmail')
            errors = errors.replace('first_name', 'formFirstName')
            errors = errors.replace('last_name', 'formLastName')
            errors = errors.replace('old_password', 'formOldPassword')
            errors = errors.replace('new_password1', 'formNewPassword1')
            errors = errors.replace('new_password2', 'formNewPassword2')
            json_data = {'errors': errors}

        return JsonResponse(status=json_status, data=json_data)
    return render(request, 'userprofile/edit-userprofile.html')
