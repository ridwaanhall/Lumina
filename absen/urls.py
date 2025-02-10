from django.urls import path
from . import views

urlpatterns = [
    path('', views.LuminaAppView.as_view(), name='lumina-app'),
    path('terms/', views.TermsView.as_view(), name='terms'),
    path('about/', views.AboutView.as_view(), name='about'),
]