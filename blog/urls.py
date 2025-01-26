from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog'),
    path('<slug:title>', views.BlogDetailView.as_view(), name='blog-detail'),
]