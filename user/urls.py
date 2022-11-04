from django.urls import path

from user.views import RegistrationAPIView, UserAPIView

urlpatterns = [
    path('register/', RegistrationAPIView.as_view()),
    path('profile/', UserAPIView.as_view()),
]