const cards = document.querySelectorAll('.full-card');
const bg = document.querySelector('.center-outer');
const nextBtn = document.getElementById('nextBtn');
let currentCardIndex = 0;

function showNextCard() {
	nextBtn.classList.add('visually-hidden');
	nextBtn.classList.remove('btn-success');
	nextBtn.classList.remove('btn-danger');
	bg.classList.remove('bg-correct');
	bg.classList.remove('bg-incorrect');
	cards[currentCardIndex].classList.add('visually-hidden');
	currentCardIndex++;
	if (currentCardIndex >= cards.length) {
		sendData();
	} else {
		cards[currentCardIndex].classList.remove('visually-hidden');
	}
}

const submitBtns = document.querySelectorAll('.submit-btn');
submitBtns.forEach((submitBtn) => {
	submitBtn.addEventListener('click', (event) => {
		const currentCard = cards[currentCardIndex];
		const answer = currentCard
			.querySelector('input[type="text"]')
			.value.trim()
			.toLowerCase();
		const correctAnswer = currentCard
			.querySelector('input[type="hidden"]')
			.value.trim()
			.toLowerCase();

		if (answer === correctAnswer) {
			currentCard.classList.add('correct');
			nextBtn.classList.add('btn-success');
			bg.classList.add('bg-correct');
		} else {
			currentCard.classList.add('incorrect');
			currentCard
				.querySelector('.back-side')
				.classList.remove('visually-hidden');
			nextBtn.classList.add('btn-danger');
			bg.classList.add('bg-incorrect');
		}
		submitBtn.classList.add('visually-hidden');
		nextBtn.classList.remove('visually-hidden');
	});
});

nextBtn.addEventListener('click', (e) => {
	showNextCard();
});

cards[currentCardIndex].classList.remove('visually-hidden');
