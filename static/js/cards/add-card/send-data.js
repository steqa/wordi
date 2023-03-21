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
	let responseStatus = null;
	imageInputs.forEach((input) => {
		const image = input.files[0];
		if (image) {
			formData.append(input.id, image);
		}
	});
	textInputs.forEach((input) => {
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
			if (responseStatus === 200) {
				localStorage.setItem('toastStatus', 'success');
				localStorage.setItem('toastMessage', 'Карточка добавлена.');
				window.location.replace(data['redirectUrl']);
			} else if (responseStatus === 400) {
				showToast('error', 'Что-то пошло не так.');
			}
		})
		.catch((error) => console.error(error));
}
