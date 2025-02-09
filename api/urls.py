from django.urls import path
from .views import DecryptView, EncryptView

urlpatterns = [
    path('decrypt/', DecryptView.as_view(), name='decrypt'),
    path('encrypt/', EncryptView.as_view(), name='encrypt'),
]
