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
				for (let date in calendarData) {
					const color = '#0dcaf0';
					const correctAnswers = calendarData[date];
					let startDate = new Date(date);
					let endDate = new Date(date);

					calendarDataSource.push({
						color: color,
						correctAnswers: correctAnswers,
						startDate: startDate,
						endDate: endDate,
					});
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
