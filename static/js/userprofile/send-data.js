const saveButton = document.getElementById('saveBtn');
const formInputs = document.querySelectorAll('input.form-control');

saveButton.addEventListener('click', (e) => {
	const validationResult = validateFields();
	if (validationResult) {
		sendData();
	}
});

function sendData() {
	let formData = new FormData();
	let responseStatus = null;
	formInputs.forEach((input) => {
		const value = input.value;
		const defaultValue = document.querySelector(
			`[data-default-input="${input.dataset.default}"]`
		).dataset.defaultValue;
		if (value && value != defaultValue) {
			formData.append(input.id, value);
		}
	});
	fetch(window.location.href, {
		method: 'POST',
		headers: {
			'X-CSRFToken': getCSRFToken(),
		},
		body: formData,
	})
		.then((response) => {
			responseStatus = response.status;
			return response.json();
		})
		.then((data) => {
			if (responseStatus === 200) {
				localStorage.setItem('toastStatus', 'success');
				localStorage.setItem('toastMessage', 'Изменения сохранены.');
				window.location.replace(data['redirectUrl']);
			} else if (responseStatus === 400) {
				const errors = data['errors'];
				if (errors) {
					const fieldsWithErrors = JSON.parse(errors);
					let fieldsErrors = {};
					for (const [field, errorsArray] of Object.entries(fieldsWithErrors)) {
						let errors = [];
						errorsArray.forEach((error) => {
							errors.push(error);
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
