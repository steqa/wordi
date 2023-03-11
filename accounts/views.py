from django.shortcuts import render


def login_user(request):
    return render(request, 'accounts/login.html')
