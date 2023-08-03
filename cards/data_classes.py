from pydantic import BaseModel, Field, validator


class CardData(BaseModel):
    front_text: str = Field(alias='formFrontText', min_length=1)
    back_text: str = Field(alias='formBackText', min_length=1)


class CardImagesData(BaseModel):
    front_image: list = Field(alias='formFrontImage', default=[None])
    back_image: list = Field(alias='formBackImage', default=[None])

    @ validator('front_image', 'back_image', allow_reuse=True)
    def test_type(cls, value: list) -> list:
        if value[0].content_type not in ['image/png', 'image/jpeg']:
            raise ValueError('Допустимые форматы изображений JPG и PNG.')
        return value

    @ validator('front_image', 'back_image', allow_reuse=True)
    def test_max_size(cls, value: list) -> list:
        if value[0].size > 1048576:
            raise ValueError('Максимальный размер изображения — 1MB.')
        return value

    def is_not_empty(self) -> bool:
        front_image_is_not_empty = self.front_image != [None]
        back_image_is_not_empty = self.back_image != [None]
        if front_image_is_not_empty or back_image_is_not_empty:
            return True
        else:
            return False
