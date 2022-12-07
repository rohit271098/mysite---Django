from django.urls import path
from . import views

urlpatterns = [
    path('', views.first, name="first"),
    path('base/', views.second, name="second"),
    path('base1/', views.third, name="third")
]


