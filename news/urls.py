from django.urls import path
from .views import latest_news

urlpatterns = [
    path('api/news/', latest_news),
]