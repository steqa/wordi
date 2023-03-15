const loginButton = document.getElementById('loginBtn');
const fields = document.querySelectorAll('input.form-control');

fields.forEach((field) => {
	let time;
	field.addEventListener('input', (e) => {
		clearTimeout(time);
		time = setTimeout((e) => {
			if (field.value) {
				if (field.id === 'formEmail') {
					validateEmail(field);
				} else if (field.id === 'formPassword') {
					validatePassword(field);
				}
			} else {
				displayFieldErrors(field);
			}
		}, 500);
	});
});

function validateFields() {
	let fieldsErrors = {};
	fields.forEach((field) => {
		if (field.id === 'formEmail') {
			const error = emailValidation(field);
			if (error) {
				fieldsErrors[field.id] = error;
			}
		} else if (field.id === 'formPassword1') {
			const error = passwordValidation(field);
			if (error) {
				fieldsErrors[field.id] = error;
			}
		}
	});
	displayFieldsErrors(fieldsErrors);
	if (Object.keys(fieldsErrors).length > 0) {
		return false;
	} else {
		return true;
	}
}

function validatePassword(field) {
	let fieldErrors = {};
	const errors = passwordValidation(field);
	if (errors) {
		fieldErrors[field.id] = errors;
	}
	displayFieldErrors(field, fieldErrors);
}

function passwordValidation(field) {
	const value = field.value;
	let errors = [];
	if (typeof value === 'undefined' || value === '' || value === null) {
		errors.push('Обязательное поле.');
	} else {
		if (value.length < 8) {
			errors.push(
				'Введённый пароль слишком короткий. Он должен содержать как минимум 8 символов.'
			);
		}
		if (/^[0-9]+$/.test(value)) {
			errors.push('Введённый пароль состоит только из цифр.');
		}
	}
	if (errors.length < 1) {
		return false;
	}
	return errors;
}
