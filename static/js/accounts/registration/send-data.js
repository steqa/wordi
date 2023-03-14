const registrationBtn = document.getElementById('registrationBtn');
const inputs = document.querySelectorAll('input.form-control');

registrationBtn.addEventListener('click', (e) => {
	const validationResult = validateFields();
	if (validationResult) {
		sendData();
	}
});

function sendData() {
	let formData = new FormData();
	let responseStatus = null;
	inputs.forEach((input) => {
		const value = input.value;
		if (value) {
			formData.append(input.id, value);
		}
	});
	fetch(window.location.href, {
		method: 'POST',
		headers: {
			'X-CSRFToken': getCookie('csrftoken'),
		},
		body: formData,
	})
		.then((response) => {
			responseStatus = response.status;
			return response.json();
		})
		.then((data) => {
			if (responseStatus === 200) {
				window.location.replace(JSON.parse(data)['redirectUrl']);
			} else if (responseStatus === 400) {
				const errors = JSON.parse(data)['errors'];
				if (errors) {
					const fieldsWithErrors = JSON.parse(errors);
					let fieldsErrors = {};
					for (const [field, errorsArray] of Object.entries(fieldsWithErrors)) {
						let errors = [];
						errorsArray.forEach((error) => {
							errors.push(error['message']);
						});
						fieldsErrors[field] = errors;
					}
					displayFieldsErrors(fieldsErrors);
				} else {
					showToast('error', 'Что-то пошло не так.');
				}
			}
		})
		.catch((error) => console.error(error));
}
