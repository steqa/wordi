from pydantic import BaseModel, Field, validator


class CardData(BaseModel):
    front_text: str = Field(alias='formFrontText', min_length=1)
    back_text: str = Field(alias='formBackText', min_length=1)


class CardImagesData(BaseModel):
    front_image: None | list = Field(alias='formFrontImage')
    back_image: None | list = Field(alias='formBackImage')

    @ validator('front_image', 'back_image', allow_reuse=True)
    def test_type(cls, value: list) -> list:
        if value[0].content_type not in ['image/png', 'image/jpeg']:
            raise ValueError('Допустимые форматы изображений JPG и PNG.')
        return value

    @ validator('front_image', 'back_image', allow_reuse=True)
    def test_max_size(cls, value: list) -> list:
        if value[0].size > 26214400:
            raise ValueError('Максимальный размер изображения — 25MB.')
        return value
