const deleteBtns = document.querySelectorAll('[data-delete-btn]');
const deletedCardPreview = document.getElementById('deletedCardPreview');
const modalDeleteBtn = document.getElementById('modalDeleteBtn');

deleteBtns.forEach((btn) => {
	btn.addEventListener('click', (e) => {
		const card = btn.closest('.card');
		modalDeleteBtn.dataset.card = btn.dataset.deleteBtn;
		const cardClone = card.cloneNode(true);
		deletedCardPreview.innerHTML = '';
		deletedCardPreview.append(cardClone);
		const deletedCardPreviewEditBtn =
			deletedCardPreview.querySelector('.edit-icon-btn');
		deletedCardPreviewEditBtn.classList.remove('edit-icon-btn');
		deletedCardPreviewEditBtn.style.cursor = 'auto';
		const deletedCardPreviewDeleteBtn =
			deletedCardPreview.querySelector('.remove-icon-btn');
		deletedCardPreviewDeleteBtn.classList.remove('remove-icon-btn');
		deletedCardPreviewDeleteBtn.style.cursor = 'auto';
		const deletedCardPreviewDeleteBtnSvg =
			deletedCardPreviewDeleteBtn.querySelector('svg');
		deletedCardPreviewDeleteBtnSvg.removeAttribute('data-bs-toggle');
		deletedCardPreviewDeleteBtnSvg.removeAttribute('data-bs-target');
	});
});
