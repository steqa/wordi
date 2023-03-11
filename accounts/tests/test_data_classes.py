from django.test import TestCase

from accounts.data_classes import UserLoginData
from wordi.tests.mixins import TestDataClassFieldsPropertiesValuesMixin


class UserLoginDataTests(TestCase, TestDataClassFieldsPropertiesValuesMixin):
    @classmethod
    def setUpTestData(cls):
        cls.fields_and_properties = {
            'formEmail': {
                'title': 'Formemail',
                'minLength': 1,
                'type': 'string',
            },
            'formPassword': {
                'title': 'Formpassword',
                'minLength': 1,
                'type': 'string',
            }
        }

    def test_properties(self):
        super().run_data_class_fields_properties_values_test(UserLoginData)
