let temporaryStorage = {};

function getCalendarData() {
	if (selectedYear in temporaryStorage) {
		return new Promise((resolve, reject) => {
			data = temporaryStorage[selectedYear];
			const dataSource = formCalendarData(temporaryStorage[selectedYear]);
			resolve(dataSource);
		});
	}
	let responseStatus = null;
	return fetch(window.location.href + `?year=${selectedYear}`, {
		method: 'GET',
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
				data = data.calendarData;
				const dataSource = formCalendarData(data);
				return dataSource;
			} else if (responseStatus === 400) {
				showToast('error', 'Не удалось загрузить статистику.');
				return [];
			}
		})
		.catch((error) => {
			showToast('error', 'Не удалось загрузить статистику.');
			console.error(error);
			return [];
		});
}

function formCalendarData(data) {
	const calendarDataSource = [];
	temporaryStorage[selectedYear] = data;
	for (let date in data) {
		const color = '#0dcaf0';
		const correctAnswers = data[date];
		let startDate = new Date(date);
		let endDate = new Date(date);

		calendarDataSource.push({
			color: color,
			correctAnswers: correctAnswers,
			startDate: startDate,
			endDate: endDate,
		});
	}
	return calendarDataSource;
}
