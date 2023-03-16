from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_user, name='login-user'),
    path('logout/', views.logout_user, name='logout-user'),
    path('registration/', views.registration_user, name='registration-user'),
    path('activate-user/<uidb64>/<token>',
         views.activate_user, name='activate-user'),
]
