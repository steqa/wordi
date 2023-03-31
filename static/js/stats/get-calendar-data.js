function getCalendarData() {
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
			const calendarDataSource = [];
			if (responseStatus === 200) {
				const calendarData = data.calendarData;
				for (let i in calendarData) {
					const color = '#0dcaf0';
					const correctAnswers = calendarData[i].correctAnswers;
					let startDate = new Date(calendarData[i].date);
					let endDate = new Date(calendarData[i].date);

					if (correctAnswers > 0) {
						calendarDataSource.push({
							color: color,
							correctAnswers: correctAnswers,
							startDate: startDate,
							endDate: endDate,
						});
					}
				}
			} else if (responseStatus === 400) {
				showToast('error', 'Не удалось загрузить статистику.');
			}
			return calendarDataSource;
		})
		.catch((error) => {
			showToast('error', 'Не удалось загрузить статистику.');
			console.error(error);
			return [];
		});
}
