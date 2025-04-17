from django.urls import path
from django.shortcuts import redirect 

from . import views

urlpatterns = [
    path('', lambda request: redirect('login')),
    path('api/login/', views.login, name='login'),
    path('api/register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('api/stadiums/', views.stadiums, name='stadiums'),
    path('api/matches/', views.matches, name='matches'),
    path('api/matches/<int:pk>/seats', views.match_seats, name='match_seats'),
    path('api/matches/<int:pk>/seats/<int:seat_id>/book', views.bookSeat.as_view(), name='book_seat'),
]