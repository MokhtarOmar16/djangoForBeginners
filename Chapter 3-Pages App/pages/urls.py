from django.urls import path
from .views import HomePageView , Info

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('info/', Info.as_view(), name="info")
]