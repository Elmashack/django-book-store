from django.urls import path
from .views import HomePageView, AbotPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AbotPageView.as_view(), name='about'),
]