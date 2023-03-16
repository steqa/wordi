from pydantic import BaseModel, Field


class UserLoginData(BaseModel):
    email: None | str = Field(alias='formEmail', min_length=1)
    password: None | str = Field(alias='formPassword', min_length=1)


class UserRegistrationData(BaseModel):
    email: None | str = Field(alias='formEmail', min_length=1)
    first_name: None | str = Field(alias='formFirstName', min_length=1)
    last_name: None | str = Field(alias='formLastName', min_length=1)
    password1: None | str = Field(alias='formPassword1', min_length=1)
    password2: None | str = Field(alias='formPassword2', min_length=1)


class EmailData(BaseModel):
    email: None | str = Field(alias='formEmail', min_length=1)
