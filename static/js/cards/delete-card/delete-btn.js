const deleteBtns = document.querySelectorAll('[data-delete-btn]');
const deleteCardPreview = document.getElementById('deleteCardPreview');
const modalDeleteBtn = document.getElementById('modalDeleteBtn');

deleteBtns.forEach((btn) => {
	btn.addEventListener('click', (e) => {
		const card = btn.closest('.card');
		modalDeleteBtn.dataset.card = btn.dataset.deleteBtn;

		const cardClone = card.cloneNode(true);
		deleteCardPreview.innerHTML = '';
		deleteCardPreview.append(cardClone);

		const iconBtns = deleteCardPreview.querySelectorAll('.icon-btn');

		iconBtns.forEach((btn) => {
			btn.classList.remove('remove-icon-btn');
			btn.classList.remove('edit-icon-btn');
			btn.style.cursor = 'auto';
			const btnSvg = btn.querySelector('svg');
			btnSvg.removeAttribute('data-bs-toggle');
			btnSvg.removeAttribute('data-bs-target');
		});
	});
});
