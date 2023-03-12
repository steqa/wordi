from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_user, name='login-user'),
    path('logout/', views.logout_user, name='logout-user'),
    path('registration/', views.registration_user, name='registration-user'),
]
