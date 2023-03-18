const fields = document.querySelectorAll('input.form-control');

fields.forEach((field) => {
	let time;
	field.addEventListener('input', (e) => {
		clearTimeout(time);
		time = setTimeout((e) => {
			if (field.value) {
				if (field.id === 'formEmail') {
					validateEmail(field);
				} else if (field.id === 'formNewPassword1') {
					validatePassword(field);
					validatePasswordsMatch();
				} else if (field.id === 'formNewPassword2') {
					validateSecondPassword(field);
				} else {
					validateField(field);
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
		} else if (field.id === 'formNewPassword1') {
			const error = passwordValidation(field);
			if (error) {
				fieldsErrors[field.id] = error;
			}
		} else if (field.id === 'formNewPassword2') {
			const error = secondPasswordValidation(field);
			if (error) {
				fieldsErrors[field.id] = error;
			}
		} else {
			const error = fieldValidation(field);
			if (error) {
				fieldsErrors[field.id] = error;
			}
		}
	});
	displayFieldsErrors(fieldsErrors);
	if (Object.keys(fieldsErrors).length > 0 || !validatePasswordsMatch()) {
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

function validateSecondPassword(field) {
	let fieldErrors = {};
	const errors = secondPasswordValidation(field);
	if (errors) {
		fieldErrors[field.id] = errors;
	}
	displayFieldErrors(field, fieldErrors);
}

function validatePasswordsMatch() {
	password1 = document.getElementById('formNewPassword1');
	password2 = document.getElementById('formNewPassword2');
	if (password2.value) {
		if (password1.value === password2.value) {
			displayFieldErrors(password2, {});
			return true;
		} else {
			displayFieldErrors(password2, {
				formNewPassword2: ['Введенные пароли не совпадают.'],
			});
			return false;
		}
	}
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

function secondPasswordValidation(field) {
	const value = field.value;
	let errors = [];
	if (typeof value === 'undefined' || value === '' || value === null) {
		errors.push('Обязательное поле.');
	} else {
		if (value != document.getElementById('formNewPassword1').value) {
			errors.push('Введенные пароли не совпадают.');
		}
	}
	if (errors.length < 1) {
		return false;
	}
	return errors;
}
