from django.urls import path
from .views import  animeDetailsView

urlpatterns = [
    path("animesDetails/", animeDetailsView.as_view())

]
