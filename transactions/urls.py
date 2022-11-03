from django.urls import path, include
from rest_framework.routers import SimpleRouter

from transactions import views

router = SimpleRouter()
router.register(r'', views.TransactionsViewSet, basename='transaction')

urlpatterns = [
    path('', include(router.urls)),
]