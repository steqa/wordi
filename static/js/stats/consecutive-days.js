const consecutiveDays = document.getElementById('consecutiveDays');
const consecutiveDaysTitle = document.getElementById('consecutiveDaysTitle');

consecutiveDaysTitle.innerHTML = dayTitle(consecutiveDays.innerHTML);

function dayTitle(number) {
	if (number > 10 && [11, 12, 13, 14].includes(number % 100)) return 'дней';
	last_num = number % 10;
	if (last_num == 1) return 'день';
	if ([2, 3, 4].includes(last_num)) return 'дня';
	if ([5, 6, 7, 8, 9, 0].includes(last_num)) return 'дней';
}
