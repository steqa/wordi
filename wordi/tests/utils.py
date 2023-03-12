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


def run_form_fields_labels_equal_test(
        form, self_,
        field_name: str,
        expected_label: str) -> None:

    with self_.subTest(f'{field_name=}, {expected_label=}'):
        field_real_label = form.fields[field_name].label

        self_.assertEqual(field_real_label, expected_label)


def run_form_fields_max_length_equal_test(
        form, self_,
        field_name: str,
        expected_max_length: str) -> None:

    with self_.subTest(f'{field_name=}, {expected_max_length=}'):
        field_real_max_length = form.fields[field_name].max_length

        self_.assertEqual(field_real_max_length, expected_max_length)


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


def run_data_class_properties_equal_test(
        data_class, self_, field: str, properties: dict) -> None:

    with self_.subTest(f'{field=}, {properties=}'):
        real_properties = data_class.schema()['properties'][field]
        self_.assertEqual(real_properties, properties)
