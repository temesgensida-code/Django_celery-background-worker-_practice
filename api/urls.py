from django.urls import path
from . import views

urlpatterns = [
    path('joke/', views.random_joke, name='random_joke'),
]