from django.urls import path
from . import views

urlpatterns = [
    path('', views.AbsenDisiniView.as_view(), name='absen-disini'),
    path('terms/', views.TermsView.as_view(), name='terms'),
]