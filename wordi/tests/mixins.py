from .utils import run_field_parameter_equal_test


class TestFieldsParametersValuesMixin:
    def run_fields_parameters_values_test(self, model):
        for parameter_name, fields_and_parameter_value in \
                self.parameters_and_fields_with_value.items():
            run_field_parameter_equal_test(
                model, self, fields_and_parameter_value, parameter_name
            )
