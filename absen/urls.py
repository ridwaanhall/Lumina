from django.urls import path
from . import views

urlpatterns = [
    path('', views.LuminaAppView.as_view(), name='lumina-app'),
    path('sec/', views.LuminaSecAppView.as_view(), name='lumina-sec-app'),
    path('simple/', views.LuminaSimpleAppView.as_view(), name='lumina-simple-app'),
    path('terms/', views.TermsView.as_view(), name='terms'),
    path('about/', views.AboutView.as_view(), name='about'),
]