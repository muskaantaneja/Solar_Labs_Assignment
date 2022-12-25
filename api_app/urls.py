from django.urls import path
from api_app import views

urlpatterns = [
    path('', views.home),
    path('country_info/<cname>', views.country_info),
]