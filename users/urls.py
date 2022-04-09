from django.urls import path
from .views import RegisterView, HelloView

urlpatterns = [
    path('signup', RegisterView.as_view()),
    path('hello', HelloView.as_view())
]
