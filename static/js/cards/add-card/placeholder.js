const inputs = document.querySelectorAll('.add-input');
const formImageClearBtns = document.querySelectorAll('.form-image-clear-btn');

inputs.forEach((input) => {
	let time;
	input.addEventListener('input', (e) => {
		if (input.id === 'formFrontText' || input.id === 'formBackText') {
			clearTimeout(time);
			time = setTimeout((e) => {
				changeTextPlaceholder(input);
			}, 500);
		} else if (input.id === 'formFrontImage' || input.id === 'formBackImage') {
			changeImagePlaceholder(input);
		}
	});
});

formImageClearBtns.forEach((btn) => {
	btn.addEventListener('click', (e) => {
		let input = null;
		let placeholderTextHide = null;
		let placeholderTextShow = null;
		if (btn.dataset.side === 'front') {
			input = document.getElementById('formFrontImage');
			placeholderTextHide = document.getElementById(
				'placeholderFrontImageHide'
			);
			placeholderTextShow = document.getElementById(
				'placeholderFrontImageShow'
			);
		} else if (btn.dataset.side === 'back') {
			input = document.getElementById('formBackImage');
			placeholderTextHide = document.getElementById('placeholderBackImageHide');
			placeholderTextShow = document.getElementById('placeholderBackImageShow');
		}
		clearPreviewImage(input, btn, placeholderTextHide, placeholderTextShow);
		const feedbackBlock = input.parentNode.querySelector('.invalid-feedback');
		input.classList.remove('is-invalid');
		feedbackBlock.innerHTML = '';
	});
});

function changeTextPlaceholder(input) {
	let placeholderTextHide = null;
	let placeholderTextShow = null;
	if (input.id === 'formFrontText') {
		placeholderTextHide = document.getElementById('placeholderFrontTextHide');
		placeholderTextShow = document.getElementById('placeholderFrontTextShow');
	} else if (input.id === 'formBackText') {
		placeholderTextHide = document.getElementById('placeholderBackTextHide');
		placeholderTextShow = document.getElementById('placeholderBackTextShow');
	}
	if (input.value != '') {
		placeholderTextHide.classList.add('visually-hidden');
		placeholderTextShow.classList.remove('visually-hidden');
		const value = input.value.split('\n');
		innerValue = '';
		value.forEach((v) => {
			if (v === '') {
				innerValue += `&nbsp;<br>`;
			} else {
				innerValue += `${v}<br>`;
			}
		});
		placeholderTextShow.innerHTML = innerValue;
	} else {
		placeholderTextHide.classList.remove('visually-hidden');
		placeholderTextShow.classList.add('visually-hidden');
	}
}

function changeImagePlaceholder(input) {
	let placeholderImageHide = null;
	let placeholderImageShow = null;
	let imageClearBtn = null;
	if (input.id === 'formFrontImage') {
		placeholderImageHide = document.getElementById('placeholderFrontImageHide');
		placeholderImageShow = document.getElementById('placeholderFrontImageShow');
		imageClearBtn = document.querySelector(
			'.form-image-clear-btn[data-side="front"]'
		);
	} else if (input.id === 'formBackImage') {
		placeholderImageHide = document.getElementById('placeholderBackImageHide');
		placeholderImageShow = document.getElementById('placeholderBackImageShow');
		imageClearBtn = document.querySelector(
			'.form-image-clear-btn[data-side="back"]'
		);
	}
	const image = input.files[0];
	previewImage(image, placeholderImageHide, placeholderImageShow);
	imageClearBtn.classList.remove('visually-hidden');
}

function previewImage(image, placeholderImageHide, placeholderImageShow) {
	const reader = new FileReader();
	reader.addEventListener('load', () => {
		placeholderImageHide.classList.add('visually-hidden');
		placeholderImageShow.classList.remove('visually-hidden');
		const previewImageDiv = placeholderImageShow.querySelector('div');
		previewImageDiv.style.backgroundImage = `url(${reader.result})`;
	});
	reader.readAsDataURL(image);
}

function clearPreviewImage(
	input,
	btn,
	placeholderImageHide,
	placeholderImageShow
) {
	input.value = '';
	placeholderImageHide.classList.remove('visually-hidden');
	placeholderImageShow.classList.add('visually-hidden');
	const previewImageDiv = placeholderImageShow.querySelector('div');
	previewImageDiv.style.backgroundImage = '';
	btn.classList.add('visually-hidden');
}
