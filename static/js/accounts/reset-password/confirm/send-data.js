const confirmResetPasswordBtn = document.getElementById(
	'confirmResetPasswordBtn'
);
const inputs = document.querySelectorAll('input.form-control');

confirmResetPasswordBtn.addEventListener('click', (e) => {
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
			'X-CSRFToken': getCSRFToken(),
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
				localStorage.setItem('toastMessage', 'Вы успешно сменили пароль.');
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
		.catch((error) => {
			showToast('error', 'Что-то пошло не так.');
			console.error(error);
		});
}
