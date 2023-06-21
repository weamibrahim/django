from django.urls import path
from .views import movie_list, movie_detail

app_name = "home-api"

urlpatterns = [
    path('movies/', movie_list, name='movie_list'),
    path('movies/<int:pk>/', movie_detail, name='movie_detail'),
]