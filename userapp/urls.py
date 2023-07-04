from django.urls import path

from userapp.views import RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view()),
]
