const loginButton = document.getElementById('loginBtn');
const fields = document.querySelectorAll('input.form-control');

fields.forEach((field) => {
	let time;
	field.addEventListener('input', (e) => {
		clearTimeout(time);
		time = setTimeout((e) => {
			if (field.value) {
				validateield(field);
			}
		}, 500);
	});
});

function validateield(field) {
	let fieldErrors = {};
	const errors = fieldValidation(field);
	if (errors) {
		fieldErrors[field.id] = errors;
	}
	displayFieldErrors(field, fieldErrors);
}

function validateFields() {
	let fieldsErrors = {};
	fields.forEach((field) => {
		const error = fieldValidation(field);
		if (error) {
			fieldsErrors[field.id] = error;
		}
	});
	displayFieldsErrors(fieldsErrors);
	if (Object.keys(fieldsErrors).length > 0) {
		return false;
	} else {
		return true;
	}
}

function fieldValidation(field) {
	const value = field.value;
	let errors = [];
	if (typeof value === 'undefined' || value === '' || value === null) {
		errors.push('Обязательное поле.');
	}
	if (errors.length < 1) {
		return false;
	}
	return errors;
}

function displayFieldsErrors(fieldsErrors) {
	fields.forEach((field) => {
		displayFieldErrors(field, fieldsErrors);
	});
}

function displayFieldErrors(field, errors) {
	const feedbackBlock = field.parentNode.querySelector('.invalid-feedback');
	if (Object.keys(errors).includes(field.id)) {
		field.classList.add('is-invalid');
		let innerValue = '';
		errors[field.id].forEach((error) => {
			innerValue += `<span>${error}</span><br>`;
		});
		feedbackBlock.innerHTML = innerValue;
	} else {
		field.classList.remove('is-invalid');
		feedbackBlock.innerHTML = '';
	}
}
