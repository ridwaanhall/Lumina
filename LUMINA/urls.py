from django.urls import path, include
from . import views

urlpatterns = [
    path('@ridwaanhall', views.PortfolioWebsiteView.as_view(), name='ridwaanhall'),
    path('lanpage/', views.LandingPageView.as_view(), name='lanpage'),
    path('<path:url>', views.CatchAllView.as_view(), name='catch_all'),

    path('', include('absen.urls')),
    path('blog/', include('blog.urls')),
]
