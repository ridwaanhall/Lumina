from django.urls import path
from . import views

urlpatterns = [
    path('decrypt/', views.UpdateEncryptedView.as_view(), name='decrypt-update'),
]
