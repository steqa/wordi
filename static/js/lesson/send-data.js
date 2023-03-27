function formAnswers() {
	const answerInputs = document.getElementsByName('answer');
	answers = {};
	answerInputs.forEach((answerInput) => {
		answers[answerInput.id] = answerInput.value;
	});
	return answers;
}

function sendData() {
	let formData = new FormData();
	let responseStatus = null;
	const answers = formAnswers();
	formData.append('answers', JSON.stringify(answers));
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
			if (responseStatus === 200) {
				const correctAnswers = document.getElementById('correctAnswers');
				const totalCards = document.getElementById('totalCards');

				correctAnswers.innerHTML = data['correct'];
				totalCards.innerHTML = data['total'];

				const cardsFeedback = document.getElementById('cardsFeedback');
				const fullCards = document.querySelectorAll('.full-card');
				fullCards.forEach((card) => {
					const cardFrontSide = document.createElement('div');
					const frontSide = card.querySelector('.front-side');
					cardFrontSide.classList.add('col-6');
					cardFrontSide.classList.add('mb-3');
					frontSide.classList.remove('bg-body-tertiary');
					cardFrontSide.appendChild(frontSide);

					const cardBackSide = document.createElement('div');
					const backSide = card.querySelector('.back-side');
					cardBackSide.classList.add('col-6');
					cardBackSide.classList.add('mb-3');
					backSide.classList.remove('mt-2');
					backSide.classList.remove('visually-hidden');
					backSide.classList.remove('bg-body-tertiary');
					cardBackSide.appendChild(backSide);

					cardsFeedback.appendChild(cardFrontSide);
					cardsFeedback.appendChild(cardBackSide);
					const answer = document.createElement('p');
					answer.classList.add('m-0');
					answer.innerHTML = `<p>Ваш ответ: <strong>${
						card.querySelector('textarea[type="text"]').value
					}</strong>`;
					cardsFeedback.appendChild(answer);
					const divider = document.createElement('hr');
					cardsFeedback.appendChild(divider);

					if (card.classList.contains('correct')) {
						frontSide.classList.add('card-correct');
						backSide.classList.add('card-correct');
						answer.classList.add('text-success');
					} else {
						frontSide.classList.add('card-incorrect');
						backSide.classList.add('card-incorrect');
						answer.classList.add('text-danger');
					}
				});
				const cardContainer = document.getElementById('card-container');
				const resultContainer = document.getElementById('result-container');
				cardContainer.classList.add('visually-hidden');
				resultContainer.classList.remove('visually-hidden');
			} else if (responseStatus === 400) {
				showToast('error', 'Что-то пошло не так.');
			}
		})
		.catch((error) => console.error(error));
}
