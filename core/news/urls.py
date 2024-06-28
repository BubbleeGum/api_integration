from django.urls import path
from .views import NewsAPIView

urlpatterns = [
    path('<str:channel>', NewsAPIView.as_view(), name='news')
]


