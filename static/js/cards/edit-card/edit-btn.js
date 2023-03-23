const editBtns = document.querySelectorAll('[data-edit-btn]');
const modalEditBtn = document.getElementById('modalEditBtn');

editBtns.forEach((btn) => {
	btn.addEventListener('click', (e) => {
		modalEditBtn.dataset.card = btn.dataset.editBtn;

		const card = btn.closest('.card');

		const frontText = card.querySelector('.frontText').innerHTML;
		const formFrontText = document.getElementById('formFrontText');
		formFrontText.value = frontText;
		const placeholderFrontTextHide = document.getElementById(
			'placeholderFrontTextHide'
		);
		placeholderFrontTextHide.classList.add('visually-hidden');
		const placeholderFrontTextShow = document.getElementById(
			'placeholderFrontTextShow'
		);
		placeholderFrontTextShow.innerHTML = frontText;
		placeholderFrontTextShow.classList.remove('visually-hidden');

		const backText = card.querySelector('.backText').innerHTML;
		const formBackText = document.getElementById('formBackText');
		formBackText.value = backText;
		const placeholderBackTextHide = document.getElementById(
			'placeholderBackTextHide'
		);
		placeholderBackTextHide.classList.add('visually-hidden');
		const placeholderBackTextShow = document.getElementById(
			'placeholderBackTextShow'
		);
		placeholderBackTextShow.innerHTML = backText;
		placeholderBackTextShow.classList.remove('visually-hidden');

		const frontImage = card.querySelector('.frontImage');
		const placeholderFrontImageHide = document.getElementById(
			'placeholderFrontImageHide'
		);
		const placeholderFrontImageShow = document.getElementById(
			'placeholderFrontImageShow'
		);
		if (frontImage) {
			placeholderFrontImageHide.classList.add('visually-hidden');
			placeholderFrontImageShow.style.backgroundImage = `url(${frontImage.src})`;
			placeholderFrontImageShow.style.backgroundRepeat = 'no-repeat';
			placeholderFrontImageShow.style.backgroundPosition = 'center';
			placeholderFrontImageShow.style.backgroundSize = 'cover';
			placeholderFrontImageShow.classList.remove('visually-hidden');
		} else {
			placeholderFrontImageHide.classList.remove('visually-hidden');
			placeholderFrontImageShow.style.backgroundImage = '';
			placeholderFrontImageShow.classList.add('visually-hidden');
		}

		const backImage = card.querySelector('.backImage');
		const placeholderBackImageHide = document.getElementById(
			'placeholderBackImageHide'
		);
		const placeholderBackImageShow = document.getElementById(
			'placeholderBackImageShow'
		);
		if (backImage) {
			placeholderBackImageHide.classList.add('visually-hidden');
			placeholderBackImageShow.style.backgroundImage = `url(${backImage.src})`;
			placeholderBackImageShow.style.backgroundRepeat = 'no-repeat';
			placeholderBackImageShow.style.backgroundPosition = 'center';
			placeholderBackImageShow.style.backgroundSize = 'cover';
			placeholderBackImageShow.classList.remove('visually-hidden');
		} else {
			placeholderBackImageHide.classList.remove('visually-hidden');
			placeholderBackImageShow.style.backgroundImage = '';
			placeholderBackImageShow.classList.add('visually-hidden');
		}

		const formFrontImage = document.getElementById('formFrontImage');
		const frontFile = new File([''], 'front_image.jpg');
		const frontDataTransfer = new DataTransfer();
		frontDataTransfer.items.add(frontFile);
		formFrontImage.files = frontDataTransfer.files;
		if (formFrontImage.webkitEntries.length) {
			formFrontImage.dataset.file = `${frontDataTransfer.files[0].name}`;
		}

		const formBackImage = document.getElementById('formBackImage');
		const backFile = new File([''], 'back_image.jpg');
		const backDataTransfer = new DataTransfer();
		backDataTransfer.items.add(backFile);
		formBackImage.files = backDataTransfer.files;
		if (formBackImage.webkitEntries.length) {
			formBackImage.dataset.file = `${backDataTransfer.files[0].name}`;
		}
	});
});
