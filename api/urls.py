from django.urls import path
from . import views

urlpatterns = [
    path('decrypt/', views.DecryptView.as_view(), name='decrypt'),
    path('encrypt/', views.EncryptView.as_view(), name='encrypt'),
]
