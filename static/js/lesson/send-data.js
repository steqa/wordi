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
			console.log(data);
		})
		.catch((error) => console.error(error));
}
