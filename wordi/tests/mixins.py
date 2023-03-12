from .utils import (run_data_class_properties_equal_test,
                    run_field_parameter_equal_test,
                    run_form_fields_labels_equal_test,
                    run_form_fields_max_length_equal_test,
                    run_page_context_equal_test, run_page_template_equal_test)


class TestFieldsParametersValuesMixin:
    def run_fields_parameters_values_test(self, model):
        for parameter_name, fields_and_parameter_value in \
                self.parameters_and_fields_with_value.items():
            run_field_parameter_equal_test(
                model, self, fields_and_parameter_value, parameter_name
            )


class TestFormFieldsLabels:
    def run_form_fields_labels_test(self, form):
        for field_name, expected_label in \
                self.fields_with_labels.items():
            run_form_fields_labels_equal_test(
                form, self, field_name, expected_label
            )


class TestFormFieldsMaxLength:
    def run_form_fields_max_length_test(self, form):
        for field_name, expected_max_length in \
                self.fields_with_max_length.items():
            run_form_fields_max_length_equal_test(
                form, self, field_name, expected_max_length
            )


class TestPagesUsesCorrectTemplateMixin:
    def run_pages_uses_correct_template_test(self):
        for expected_template, reverse_name \
                in self.templates_pages_names.items():
            run_page_template_equal_test(
                self, reverse_name, expected_template
            )


class TestPagesShowCorrectContextMixin:
    def run_pages_show_correct_context_test(self):
        for reverse_name, context \
                in self.pages_and_context_keys_with_values.items():
            run_page_context_equal_test(
                self, reverse_name, context
            )


class TestDataClassFieldsPropertiesValuesMixin:
    def run_data_class_fields_properties_values_test(self, data_class):
        for field, properties \
                in self.fields_and_properties.items():
            run_data_class_properties_equal_test(
                data_class, self, field, properties
            )
