from django.urls import path
from . import views

app_name = 'loginsystem'

urlpatterns = [
    path("", views.registerPage, name="Register"),
    path("login/", views.loginPage, name="Login"),
    path("logout/", views.logoutUser, name="Logout"),
]