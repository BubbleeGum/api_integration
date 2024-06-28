from django.urls import path
from .views import CuacaGempaAPIView

urlpatterns = [
    path('', CuacaGempaAPIView.as_view(), name='cuaca_gempa')
]


