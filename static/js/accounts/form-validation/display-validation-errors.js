function displayFieldsErrors(fieldsErrors) {
	fields.forEach((field) => {
		displayFieldErrors(field, fieldsErrors);
	});
}

function displayFieldErrors(field, errors = {}) {
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
