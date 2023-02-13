def run_field_parameter_equal_test(
        model, self_,
        fields_and_parameter_value: dict,
        parameter_name: str) -> None:

    for instance in model.objects.all():
        for field, expected_value in fields_and_parameter_value.items():
            with self_.subTest(f'{field=}, {parameter_name=}'):
                parameter_real_value = getattr(
                    instance._meta.get_field(field), parameter_name
                )

                self_.assertEqual(parameter_real_value, expected_value)
