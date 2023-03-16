from django.test import TestCase

from accounts.data_classes import (EmailData, UserLoginData,
                                   UserRegistrationData)
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


class UserRegistrationDataTests(TestCase, TestDataClassFieldsPropertiesValuesMixin):
    @classmethod
    def setUpTestData(cls):
        cls.fields_and_properties = {
            'formEmail': {
                'title': 'Formemail',
                'minLength': 1,
                'type': 'string',
            },
            'formFirstName': {
                'title': 'Formfirstname',
                'minLength': 1,
                'type': 'string',
            },
            'formLastName': {
                'title': 'Formlastname',
                'minLength': 1,
                'type': 'string',
            },
            'formPassword1': {
                'title': 'Formpassword1',
                'minLength': 1,
                'type': 'string',
            },
            'formPassword2': {
                'title': 'Formpassword2',
                'minLength': 1,
                'type': 'string',
            }
        }

    def test_properties(self):
        super().run_data_class_fields_properties_values_test(UserRegistrationData)


class EmailDataTests(TestCase, TestDataClassFieldsPropertiesValuesMixin):
    @classmethod
    def setUpTestData(cls):
        cls.fields_and_properties = {
            'formEmail': {
                'title': 'Formemail',
                'minLength': 1,
                'type': 'string',
            }
        }

    def test_properties(self):
        super().run_data_class_fields_properties_values_test(EmailData)
