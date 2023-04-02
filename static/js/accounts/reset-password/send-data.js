const resetPasswordBtn = document.getElementById('resetPasswordBtn');
const emailInput = document.getElementById('formEmail');

resetPasswordBtn.addEventListener('click', (e) => {
	const validationResult = validateFields();
	if (validationResult) {
		sendData();
	}
});

function sendData() {
	let formData = new FormData();
	let responseStatus = null;
	formData.append(emailInput.id, emailInput.value);
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
				const renderTemplate = data['renderTemplate'];
				document.querySelector('.content-block').innerHTML = renderTemplate;
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
