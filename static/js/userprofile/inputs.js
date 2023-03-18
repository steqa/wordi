const editBtns = document.querySelectorAll('[data-edit-btn]');
const saveBtn = document.getElementById('saveBtn');
const inputs = document.querySelectorAll('input.form-control');

editBtns.forEach((btn) => {
	btn.addEventListener('click', (e) => {
		const editBlock =
			btn.parentNode.parentNode.parentNode.querySelector('[data-edit-block]');
		editBlock.style.display = 'none';
		const saveBlock =
			btn.parentNode.parentNode.parentNode.querySelector('[data-save-block]');
		saveBlock.style.display = 'flex';
		btn.parentNode.parentNode.parentNode.classList.add('bg-body-tertiary');
		const input = saveBlock.querySelectorAll('input.form-control')[0];
		input.focus();
		const inputValue = input.value;
		input.value = '';
		input.value = inputValue;
	});
});

inputs.forEach((input) => {
	input.addEventListener('input', (e) => {
		saveBtn.style.display = 'block';
	});
});
