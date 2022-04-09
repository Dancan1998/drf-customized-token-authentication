from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from users.views import ObtainAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api-token-auth/', ObtainAuthToken.as_view()),
]
