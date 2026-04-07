from django.urls import path
from . import views

urlpatterns = [
    path('joke/', views.random_joke, name='random_joke'),
    path('joke/stream/', views.stream_joke, name='stream_joke'),
]