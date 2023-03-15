function validateField(field) {
	let fieldErrors = {};
	const errors = fieldValidation(field);
	if (errors) {
		fieldErrors[field.id] = errors;
	}
	displayFieldErrors(field, fieldErrors);
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
