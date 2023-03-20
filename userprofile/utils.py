from accounts.data_classes import UserChangeData, UserChangePasswordData
from accounts.forms import CustomUserChangeForm
from accounts.models import User


def get_personal_data_errors(personal_data: UserChangeData) -> dict:
    personal_form_data = CustomUserChangeForm(personal_data.dict())
    personal_data_errors = {}
    for key, value in personal_data.dict().items():
        if (value != None) and (key in personal_form_data.errors):
            personal_data_errors[key] = personal_form_data.errors[key]

    return personal_data_errors


def edit_user(user: User, personal_data: UserChangeData) -> User:
    user = User.objects.get(pk=user.pk)
    if personal_data.email != None:
        user.email = personal_data.email
    if personal_data.first_name != None:
        user.first_name = personal_data.first_name
    if personal_data.last_name != None:
        user.last_name = personal_data.last_name
    user.save()
    return user


def password_data_is_not_empty(password_data: UserChangePasswordData) -> bool:
    return any(value != None for value in password_data.dict().values())
