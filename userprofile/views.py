from django.shortcuts import render


def edit_userprofile(request):
    return render(request, 'userprofile/edit-userprofile.html')
