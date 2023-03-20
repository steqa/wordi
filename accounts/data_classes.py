from pydantic import BaseModel, Field


class UserLoginData(BaseModel):
    email: None | str = Field(alias='formEmail')
    password: None | str = Field(alias='formPassword')


class UserRegistrationData(BaseModel):
    email: None | str = Field(alias='formEmail')
    first_name: None | str = Field(alias='formFirstName')
    last_name: None | str = Field(alias='formLastName')
    password1: None | str = Field(alias='formPassword1')
    password2: None | str = Field(alias='formPassword2')


class EmailData(BaseModel):
    email: None | str = Field(alias='formEmail')


class UserResetPasswordData(BaseModel):
    new_password1: None | str = Field(alias='formNewPassword1')
    new_password2: None | str = Field(alias='formNewPassword2')


class UserChangeData(BaseModel):
    email: None | str = Field(alias='formEmail')
    first_name: None | str = Field(alias='formFirstName')
    last_name: None | str = Field(alias='formLastName')


class UserChangePasswordData(BaseModel):
    old_password: None | str = Field(alias='formOldPassword')
    new_password1: None | str = Field(alias='formNewPassword1')
    new_password2: None | str = Field(alias='formNewPassword2')
