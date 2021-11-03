from django.urls import path
from . import views

urlpatterns = [
    path('ocr/', views.OcrView.as_view(), name="ocr"),
]