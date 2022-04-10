from django.urls import path
from .views import RegisterView, HelloView, LogOut, ChangePasswordView

urlpatterns = [
    path('signup', RegisterView.as_view()),
    path('hello', HelloView.as_view()),
    path('logout', LogOut.as_view()),
    path('change-password', ChangePasswordView.as_view()),
]
