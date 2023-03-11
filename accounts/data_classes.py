from pydantic import BaseModel, Field


class UserLoginData(BaseModel):
    email: str = Field(alias='formEmail', min_length=1)
    password: str = Field(alias='formPassword', min_length=1)
