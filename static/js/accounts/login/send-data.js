const loginBtn = document.getElementById('loginBtn');
const inputs = document.querySelectorAll('input.form-control');

loginBtn.addEventListener('click', (e) => {
	const validationResult = validateFields();
	if (validationResult) {
		sendData();
	}
});

function sendData() {
	let formData = new FormData();
	let responseStatus = null;
	inputs.forEach((input) => {
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
				localStorage.setItem('toastMessage', 'Добро пожаловать.');
				window.location.replace(JSON.parse(data)['redirectUrl']);
			} else if (responseStatus === 400) {
				const msg = JSON.parse(data)['msg'];
				if (msg) {
					showToast('error', msg);
				} else {
					showToast('error', 'Что-то пошло не так.');
				}
			}
		})
		.catch((error) => console.error(error));
}
