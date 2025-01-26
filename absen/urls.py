from django.urls import path
from .views import AbsenView

urlpatterns = [
    path('', AbsenView.as_view(), name='absen_view'),
]