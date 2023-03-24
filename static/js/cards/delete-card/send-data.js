const deleteBtn = document.getElementById('modalDeleteBtn');

deleteBtn.addEventListener('click', (e) => {
	sendDeleteData();
});

function sendDeleteData() {
	let responseStatus = null;
	fetch(window.location.href + `?cardID=${deleteBtn.dataset.card}`, {
		method: 'DELETE',
		headers: {
			'X-CSRFToken': getCookie('csrftoken'),
		},
	})
		.then((response) => {
			responseStatus = response.status;
			return response.json();
		})
		.then((data) => {
			if (responseStatus === 200) {
				localStorage.setItem('toastStatus', 'success');
				localStorage.setItem('toastMessage', 'Карточка удалена.');
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
