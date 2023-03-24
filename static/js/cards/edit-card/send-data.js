const editBtn = document.getElementById('modalEditBtn');
const imageInputs = document.querySelectorAll('.add-input[type="file"]');
const textInputs = document.querySelectorAll('textarea.add-input');

editBtn.addEventListener('click', (e) => {
	sendEditData();
});

function sendEditData() {
	let formData = new FormData();
	let responseStatus = null;
	imageInputs.forEach((input) => {
		const image = input.files[0];
		if (image) {
			if (image.type != 'initial') {
				formData.append(input.id, image);
			}
		}
	});
	textInputs.forEach((input) => {
		const value = input.value;
		if (value) {
			formData.append(input.id, value);
		}
	});
	fetch(window.location.href + `?cardID=${editBtn.dataset.card}`, {
		method: 'PUT',
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
				localStorage.setItem('toastMessage', 'Изменения сохранены.');
				window.location.replace(data['redirectUrl']);
			} else if (responseStatus === 400) {
				const msg = data['msg'];
				if (msg) {
					showToast('error', msg);
				} else {
					showToast('error', 'Что-то пошло не так.');
				}
			}
		})
		.catch((error) => console.error(error));
}
