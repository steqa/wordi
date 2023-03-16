const emailField = document.getElementById('formEmail');

let time;
emailField.addEventListener('input', (e) => {
	clearTimeout(time);
	time = setTimeout((e) => {
		if (emailField.value) {
			validateEmail(emailField);
		} else {
			displayFieldErrors(emailField);
		}
	}, 500);
});

function validateFields() {
	let fieldsErrors = {};
	const error = emailValidation(emailField);
	if (error) {
		fieldsErrors[emailField.id] = error;
	}
	displayFieldErrors(emailField, fieldsErrors);
	if (Object.keys(fieldsErrors).length > 0) {
		return false;
	} else {
		return true;
	}
}
