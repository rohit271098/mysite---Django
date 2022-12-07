from django.urls import path
from . import views

urlpatterns = [
    path('first/', views.second_app, name="second_app")
]
