

from .models import AnimeDetails
from rest_framework.pagination import PageNumberPagination


from rest_framework.generics import  ListCreateAPIView
from .serializer import AnimeDetailsSerializer


class animeDetailsView(ListCreateAPIView, PageNumberPagination):

    queryset = AnimeDetails.objects.all()
    serializer_class = AnimeDetailsSerializer

