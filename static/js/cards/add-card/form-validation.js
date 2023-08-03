const createCardButton = document.getElementById('createCardBtn');
const textFields = document.querySelectorAll('textarea.add-input');
const imageFields = document.querySelectorAll('.add-input[type="file"]');

textFields.forEach((field) => {
	let time;
	field.addEventListener('input', (e) => {
		clearTimeout(time);
		time = setTimeout((e) => {
			if (field.value) {
				validateTextField(field);
			}
		}, 500);
	});
});

imageFields.forEach((field) => {
	field.addEventListener('input', (e) => {
		validateImageField(field);
	});
});

function validateTextField(field) {
	let fieldErrors = {};
	const errors = textFieldValidation(field);
	if (errors) {
		fieldErrors[field.id] = errors;
	}
	displayFieldErrors(field, fieldErrors);
}

function validateImageField(field) {
	let fieldErrors = {};
	const errors = imageFieldValidation(field);
	if (errors) {
		fieldErrors[field.id] = errors;
	}
	displayFieldErrors(field, fieldErrors);
}

function validateFields() {
	let fieldsErrors = {};
	textFields.forEach((field) => {
		const error = textFieldValidation(field);
		if (error) {
			fieldsErrors[field.id] = error;
		}
	});
	imageFields.forEach((field) => {
		const error = imageFieldValidation(field);
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

function textFieldValidation(field) {
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

function imageFieldValidation(field) {
	const file = field.files[0];
	let errors = [];
	if (typeof file === 'undefined' || file === '' || file === null) {
		return false;
	}
	if (file.size > 1048576) {
		errors.push('Максимальный размер изображения — 1MB.');
	}
	if (file.type != 'image/png' && file.type != 'image/jpeg') {
		errors.push('Допустимые форматы изображений JPG и PNG.');
	}
	if (errors.length < 1) {
		return false;
	}
	return errors;
}

function displayFieldsErrors(fieldsErrors) {
	textFields.forEach((field) => {
		displayFieldErrors(field, fieldsErrors);
	});
	imageFields.forEach((field) => {
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
