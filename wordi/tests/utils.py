from django.urls import reverse


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


def run_page_template_equal_test(
        self_, reverse_name: str, expected_template: str) -> None:

    with self_.subTest(f'{reverse_name=}'):
        response = self_.authorized_client.get(reverse_name)
        self_.assertTemplateUsed(response, expected_template)


def run_page_context_equal_test(
        self_, reverse_name: str, context: dict) -> None:

    response = self_.authorized_client.get(reverse(reverse_name))
    for context_key, expected_context_value in context.items():
        with self_.subTest(f'{reverse_name=}, {context_key=}'):
            real_context_value = response.context[context_key][0]
            self_.assertEqual(real_context_value, expected_context_value)
