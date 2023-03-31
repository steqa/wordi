let calendar = null;

function rerenderCalendar() {
	const c = document.getElementById('calendar');
	c.removeEventListener('mouseOnDay', mouseOnDayFunc, false);
	c.removeEventListener('mouseOutDay', mouseOutDayFunc, false);
	calendar = null;
	const calendarDiv = document.getElementById('calendar');
	calendarDiv.innerHTML = '';
	renderCalendar();
}

function renderCalendar() {
	yearDropdown.querySelector('span').innerHTML = selectedYear;
	getCalendarData().then((dataSource) => {
		setTimeout(() => {
			calendar = new Calendar('#calendar', {
				language: 'ru',
				startYear: selectedYear,
				minDate: new Date(selectedYear, 0, 1),
				maxDate: new Date(selectedYear, 11, 31),
				displayHeader: false,
				dataSource: dataSource,
			});
			const c = document.getElementById('calendar');
			c.addEventListener('mouseOnDay', mouseOnDayFunc);
			c.addEventListener('mouseOutDay', mouseOutDayFunc);
		});
	});
}

function mouseOnDayFunc(e) {
	if (e.events.length > 0) {
		let content = '';

		for (let i in e.events) {
			if (typeof e.events[i].correctAnswers !== 'undefined') {
				content += 'Правильных ответов: ' + e.events[i].correctAnswers;
			}
		}

		const popover = new bootstrap.Popover(e.element, {
			trigger: 'manual',
			container: 'body',
			html: true,
			content: content,
		});
		popover.show();
	}
}
function mouseOutDayFunc(e) {
	if (e.events.length > 0) {
		bootstrap.Popover.getOrCreateInstance(e.element).hide();
	}
}

renderCalendar();
