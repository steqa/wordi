const yearDropdown = document.getElementById('yearDropdown');
let selectedYear = new Date().getFullYear();

const yearBtns = document.querySelectorAll('.year-btn');

yearBtns.forEach((yearBtn) => {
	yearBtn.addEventListener('click', (e) => {
		const year = yearBtn.innerHTML;
		if (year < selectedYear) {
			selectedYear -= 1;
			rerenderCalendar();
		} else if (year > selectedYear) {
			selectedYear += 1;
			rerenderCalendar();
		}
	});
});
