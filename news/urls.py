from django.urls import path
from .views import NewView, NewDetailView, NewStartScrappyView

urlpatterns = [
    path("news/", NewView.as_view()),
    path("news/<int:news_id>/", NewDetailView.as_view()),
    path("news/startscrappy/", NewStartScrappyView.as_view())

]
