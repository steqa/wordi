from .utils import (run_field_parameter_equal_test,
                    run_page_context_equal_test, run_page_template_equal_test)


class TestFieldsParametersValuesMixin:
    def run_fields_parameters_values_test(self, model):
        for parameter_name, fields_and_parameter_value in \
                self.parameters_and_fields_with_value.items():
            run_field_parameter_equal_test(
                model, self, fields_and_parameter_value, parameter_name
            )


class TestPagesUsesCorrectTemplateMixin:
    def run_pages_uses_correct_template_test(self):
        for expected_template, reverse_name \
                in self.templates_pages_names.items():
            run_page_template_equal_test(
                self, reverse_name, expected_template
            )


class TestPagesShowCorrectContext:
    def run_pages_show_correct_context_test(self):
        for reverse_name, context \
                in self.pages_and_context_keys_with_values.items():
            run_page_context_equal_test(
                self, reverse_name, context
            )
