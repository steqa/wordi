const toastExample = document.getElementById('toastExample');

function showToast(toastStatus, toastMessage = '') {
	if (toastStatus == 'success') {
		toastExample.classList.remove('text-bg-danger');
		toastExample.classList.add('text-bg-success');
		document.querySelector('.toast-icon-danger').style.display = 'none';
		document.querySelector('.toast-icon-success').style.display = 'flex';
		document.querySelector('.toast-message').innerHTML = toastMessage;
	} else if (toastStatus == 'error') {
		toastExample.classList.remove('text-bg-success');
		toastExample.classList.add('text-bg-danger');
		document.querySelector('.toast-icon-success').style.display = 'none';
		document.querySelector('.toast-icon-danger').style.display = 'flex';
		document.querySelector('.toast-message').innerHTML = toastMessage;
	}
	const toast = new bootstrap.Toast(toastExample);
	toast.show();
}

if (localStorage.getItem('toastStatus')) {
	toastMessage = localStorage.getItem('toastMessage');
	if (localStorage.getItem('toastStatus') == 'success') {
		toastStatus = 'success';
	} else if (localStorage.getItem('toastStatus') == 'error') {
		toastStatus = 'success';
	}
	showToast(toastStatus, toastMessage);
	localStorage.clear();
}
