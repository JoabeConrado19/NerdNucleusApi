from django.urls import path
from .views import AnimeDetailView, AnimeStartScrappyView, AnimeView

urlpatterns = [
    path("animes/", AnimeView.as_view()),
    path("animes/<int:anime_id>/", AnimeDetailView.as_view()),
    path("animes/startscrappy/", AnimeStartScrappyView.as_view())

]
