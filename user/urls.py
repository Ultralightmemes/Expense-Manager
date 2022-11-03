from django.urls import path

from user.views import RegistrationAPIView

urlpatterns = [
    path('register/', RegistrationAPIView.as_view()),
]