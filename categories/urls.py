from django.urls import path, include
from rest_framework.routers import SimpleRouter

from categories import views

router = SimpleRouter()
router.register(r'category', views.CategoryViewSet, basename='category')


urlpatterns = [
    path('', include(router.urls)),
]