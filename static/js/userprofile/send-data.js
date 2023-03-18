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
			console.log(data);
			// if (responseStatus === 200) {
			// 	const renderTemplate = data['renderTemplate'];
			// 	document.querySelector('.content-block').innerHTML = renderTemplate;
			// } else if (responseStatus === 400) {
			// 	const errors = data['errors'];
			// 	if (errors) {
			// 		const fieldsWithErrors = JSON.parse(errors);
			// 		let fieldsErrors = {};
			// 		for (const [field, errorsArray] of Object.entries(fieldsWithErrors)) {
			// 			let errors = [];
			// 			errorsArray.forEach((error) => {
			// 				errors.push(error['message']);
			// 			});
			// 			fieldsErrors[field] = errors;
			// 		}
			// 		displayFieldsErrors(fieldsErrors);
			// 	} else {
			// 		showToast('error', 'Что-то пошло не так.');
			// 	}
			// }
		})
		.catch((error) => console.error(error));
}
