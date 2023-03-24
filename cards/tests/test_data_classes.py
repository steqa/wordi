from django.core.files.uploadedfile import TemporaryUploadedFile
from django.test import TestCase

from cards.data_classes import CardData, CardImagesData
from wordi.tests.mixins import TestDataClassFieldsPropertiesValuesMixin


class CardDataTests(TestCase, TestDataClassFieldsPropertiesValuesMixin):
    @classmethod
    def setUpTestData(cls):
        cls.fields_and_properties = {
            'formFrontText': {
                'title': 'Formfronttext',
                'minLength': 1,
                'type': 'string',
            },
            'formBackText': {
                'title': 'Formbacktext',
                'minLength': 1,
                'type': 'string',
            }
        }

    def test_properties(self):
        super().run_data_class_fields_properties_values_test(CardData)


class CardImagesDataTests(TestCase, TestDataClassFieldsPropertiesValuesMixin):
    @classmethod
    def setUpTestData(cls):
        cls.fields_and_properties = {
            'formFrontImage': {
                'title': 'Formfrontimage',
                'default': [None],
                'type': 'array',
                'items': {}
            },
            'formBackImage': {
                'title': 'Formbackimage',
                'default': [None],
                'type': 'array',
                'items': {}
            }
        }

    def test_properties(self):
        super().run_data_class_fields_properties_values_test(CardImagesData)

    def test_test_type_method(self):
        image_jpeg = TemporaryUploadedFile('test', 'image/jpeg', 0, None)
        self.assertEqual(CardImagesData.test_type([image_jpeg]), [image_jpeg])
        image_png = TemporaryUploadedFile('test', 'image/png', 0, None)
        self.assertEqual(CardImagesData.test_type([image_png]), [image_png])
        image_txt = TemporaryUploadedFile('test', 'text/plain', 0, None)
        with self.assertRaisesMessage(
                ValueError, 'Допустимые форматы изображений JPG и PNG.'):
            CardImagesData.test_type([image_txt])

    def test_test_max_size_method(self):
        image_equal_25_mb = TemporaryUploadedFile(
            'test', 'image/jpeg', 26214400, None)
        self.assertEqual(CardImagesData.test_max_size(
            [image_equal_25_mb]), [image_equal_25_mb])
        image_less_25_mb = TemporaryUploadedFile(
            'test', 'image/jpeg', 26214399, None)
        self.assertEqual(CardImagesData.test_max_size(
            [image_less_25_mb]), [image_less_25_mb])
        image_more_25_mb = TemporaryUploadedFile(
            'test', 'image/jpeg', 26214401, None)
        with self.assertRaisesMessage(
                ValueError, 'Максимальный размер изображения — 25MB.'):
            CardImagesData.test_max_size([image_more_25_mb])

    def test_is_not_empty(self):
        image_jpeg = TemporaryUploadedFile('test', 'image/jpeg', 0, None)
        IS_NOT_EMPTY_AND_FILES = {
            False: {},
            True: {'formFrontImage': [image_jpeg]},
        }
        for expected_is_not_empty, files in IS_NOT_EMPTY_AND_FILES.items():
            with self.subTest(f'{files=}'):
                card_images_data = CardImagesData.parse_obj(files)
                real_is_not_empty = card_images_data.is_not_empty()
                self.assertEqual(expected_is_not_empty, real_is_not_empty)
