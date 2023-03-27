from django.http import HttpResponseBadRequest


def return_bad_request(request):
    return HttpResponseBadRequest(
        'Invalid request.', format(request.method), status=400)
