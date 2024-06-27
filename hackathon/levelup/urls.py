from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsArticleViewSet

router = DefaultRouter()
router.register(r'articles', NewsArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]