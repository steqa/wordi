from django.test import TestCase

from accounts.data_classes import (EmailData, UserChangeData,
                                   UserChangePasswordData, UserLoginData,
                                   UserRegistrationData, UserResetPasswordData)
from wordi.tests.mixins import TestDataClassFieldsPropertiesValuesMixin


class UserLoginDataTests(TestCase, TestDataClassFieldsPropertiesValuesMixin):
    @classmethod
    def setUpTestData(cls):
        cls.fields_and_properties = {
            'formEmail': {
                'title': 'Formemail',
                'type': 'string'
            },
            'formPassword': {
                'title': 'Formpassword',
                'type': 'string'
            }
        }

    def test_properties(self):
        super().run_data_class_fields_properties_values_test(UserLoginData)


class UserRegistrationDataTests(
        TestCase, TestDataClassFieldsPropertiesValuesMixin):
    @classmethod
    def setUpTestData(cls):
        cls.fields_and_properties = {
            'formEmail': {
                'title': 'Formemail',
                'type': 'string'
            },
            'formFirstName': {
                'title': 'Formfirstname',
                'type': 'string'
            },
            'formLastName': {
                'title': 'Formlastname',
                'type': 'string'
            },
            'formPassword1': {
                'title': 'Formpassword1',
                'type': 'string'
            },
            'formPassword2': {
                'title': 'Formpassword2',
                'type': 'string'
            }
        }

    def test_properties(self):
        super().run_data_class_fields_properties_values_test(
            UserRegistrationData)


class EmailDataTests(TestCase, TestDataClassFieldsPropertiesValuesMixin):
    @classmethod
    def setUpTestData(cls):
        cls.fields_and_properties = {
            'formEmail': {
                'title': 'Formemail',
                'type': 'string'
            }
        }

    def test_properties(self):
        super().run_data_class_fields_properties_values_test(EmailData)


class UserResetPasswordDataTests(
        TestCase, TestDataClassFieldsPropertiesValuesMixin):
    @classmethod
    def setUpTestData(cls):
        cls.fields_and_properties = {
            'formNewPassword1': {
                'title': 'Formnewpassword1',
                'type': 'string'
            },
            'formNewPassword2': {
                'title': 'Formnewpassword2',
                'type': 'string'
            }
        }

    def test_properties(self):
        super().run_data_class_fields_properties_values_test(
            UserResetPasswordData)


class UserChangeDataTests(
        TestCase, TestDataClassFieldsPropertiesValuesMixin):
    @classmethod
    def setUpTestData(cls):
        cls.fields_and_properties = {
            'formEmail': {
                'title': 'Formemail',
                'type': 'string'
            },
            'formFirstName': {
                'title': 'Formfirstname',
                'type': 'string'
            },
            'formLastName': {
                'title': 'Formlastname',
                'type': 'string'
            }
        }

    def test_properties(self):
        super().run_data_class_fields_properties_values_test(
            UserChangeData)


class UserChangePasswordDataTests(
        TestCase, TestDataClassFieldsPropertiesValuesMixin):
    @classmethod
    def setUpTestData(cls):
        cls.fields_and_properties = {
            'formOldPassword': {
                'title': 'Formoldpassword',
                'type': 'string'
            },
            'formNewPassword1': {
                'title': 'Formnewpassword1',
                'type': 'string'
            },
            'formNewPassword2': {
                'title': 'Formnewpassword2',
                'type': 'string'
            }
        }

    def test_properties(self):
        super().run_data_class_fields_properties_values_test(
            UserChangePasswordData)
