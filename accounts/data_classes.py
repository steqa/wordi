from pydantic import BaseModel, Field


class UserLoginData(BaseModel):
    email: str = Field(alias='formEmail', min_length=1)
    password: str = Field(alias='formPassword', min_length=1)


class UserRegistrationData(BaseModel):
    email: str = Field(alias='formEmail', min_length=1)
    first_name: str = Field(alias='formFirstName', min_length=1)
    last_name: str = Field(alias='formLastName', min_length=1)
    password1: str = Field(alias='formPassword1', min_length=1)
    password2: str = Field(alias='formPassword2', min_length=1)
