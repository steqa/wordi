function getCSRFToken() {
	return document.getElementsByName('csrfmiddlewaretoken')[0].value;
}
