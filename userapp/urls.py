from django.urls import path

from userapp.views import RegisterView, LoginView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
]
