from django.urls import path
from .views import index, GamesView, GameView

urlpatterns = [
    path('game/<slug:slug>', GameView.as_view(), name='game'),
    path('games/', GamesView.as_view(), name='games'),
    path('', index, name='index'),
]
