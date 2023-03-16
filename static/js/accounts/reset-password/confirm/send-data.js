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
			'X-CSRFToken': getCookie('csrftoken'),
		},
		body: formData,
	})
		.then((response) => {
			responseStatus = response.status;
			return response.json();
		})
		.then((data) => {
			console.log(data);
			// if (responseStatus === 200) {
			// 	const renderTemplate = JSON.parse(data)['renderTemplate'];
			// 	document.querySelector('.content-block').innerHTML = renderTemplate;
			// } else if (responseStatus === 400) {
			// 	const msg = JSON.parse(data)['msg'];
			// 	if (msg) {
			// 		showToast('error', msg);
			// 	} else {
			// 		showToast('error', 'Что-то пошло не так.');
			// 	}
			// }
		})
		.catch((error) => console.error(error));
}
