const createCardBtn = document.getElementById('createCardBtn');
const imageInputs = document.querySelectorAll('.add-input[type="file"]');
const textInputs = document.querySelectorAll('textarea.add-input');

createCardBtn.addEventListener('click', (e) => {
	const validationResult = validateFields();
	if (validationResult) {
		sendData();
	}
});

function sendData() {
	let formData = new FormData();
	imageInputs.forEach((input) => {
		const image = input.files[0];
		if (image) {
			if (input.id === 'formFrontImage') {
				formData.append('front_image', image);
			} else if (input.id === 'formBackImage') {
				formData.append('back_image', image);
			}
		}
	});
	textInputs.forEach((input) => {
		const value = input.value;
		if (value) {
			if (input.id === 'formFrontText') {
				formData.append('front_text', value);
			} else if (input.id === 'formBackText') {
				formData.append('back_text', value);
			}
		}
	});
	fetch(window.location.href, {
		method: 'POST',
		headers: {
			'X-CSRFToken': getCookie('csrftoken'),
		},
		body: formData,
	});
}
