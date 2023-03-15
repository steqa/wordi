function validateEmail(field) {
	let fieldErrors = {};
	const errors = emailValidation(field);
	if (errors) {
		fieldErrors[field.id] = errors;
	}
	displayFieldErrors(field, fieldErrors);
}

function emailValidation(field) {
	const value = field.value;
	let errors = [];
	if (typeof value === 'undefined' || value === '' || value === null) {
		errors.push('Обязательное поле.');
	} else {
		const validRegex =
			/^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
		if (!value.match(validRegex)) {
			errors.push('Введите правильный адрес электронной почты.');
		}
	}
	if (errors.length < 1) {
		return false;
	}
	return errors;
}
