
from django.shortcuts import render, get_object_or_404
import time
import json
import requests
from bs4 import BeautifulSoup
from anime.models import Anime

# Create your views here.

from rest_framework.views import APIView, Response, Request, status
from django.forms.models import model_to_dict
from news.apps import AppConfig
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from animesDetails.models import AnimeDetails


# Create your views here.
    

class AnimeView(APIView, PageNumberPagination):

    # def get(self, request: Request) -> Request:
    #     news_list = []
    #     news = New.objects.all()
    #     titulo = request.GET.get('title')
    #     category = request.GET.get('category')

    #     if titulo:
    #         news= news.filter(title__icontains=titulo)
    #     if category:
    #         news= news.filter(category__icontains=category)
    #     for new in news:
    #         news_list.append(model_to_dict(new))

    #     reverse = list(reversed(news_list))
    #     result_page = self.paginate_queryset(reverse, request)
        

    #     return self.get_paginated_response(result_page)
        


    def post(self, request: Request) -> Request:
        ...

        # return Response(team_dict, status.HTTP_201_CREATED)


class AnimeDetailView(APIView):
    def get(self, request: Request, news_id: int) -> Response:
        anime = get_object_or_404(Anime, id = news_id)
        new_response = model_to_dict(anime)
        
        return Response(new_response, status.HTTP_200_OK)


    def delete(self, request: Request, news_id: int) -> Response:
       ...

        # return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request: Request, news_id: int) -> Response:
       ...


        # return Response(team_dict, status.HTTP_200_OK)

class AnimeStartScrappyView(APIView):

    def get(self, request: Request) -> Request:
            
        
            print('Execultando get')
            
            anime_list = []
       
            url = 'https://animefire.net/'
            headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
}
            response = requests.get(url, headers=headers)


            soup = BeautifulSoup(response.content, 'html.parser')
            articles = soup.select('.divCardUltimosEpsHome')

            for article in articles:
                new_content = {}
                title = article.select_one('.animeTitle').text
                ep = article.select_one('.numEp').text.split(" ")[1]
                img = article.select_one(".imgAnimesUltimosEps")['data-src']
                url2 = article.select_one('a')
                url3 = url2['href']
                response2 = requests.get(url3, headers=headers)
                soup2 = BeautifulSoup(response2.content, 'html.parser')
                description = soup2.select_one('p#video_sinopse').text.replace("\n", " ")
                links = soup2.select_one(".video-js")['data-video-src']
                response3 = requests.get(links, headers=headers)
                soup3 = BeautifulSoup(response3.content, 'html.parser')
                jsonLoads = json.loads(soup3.text)
                srcMedium = jsonLoads['data'][0]['src']
                srcHD = jsonLoads['data'][1]['src']
                new_content['title'] = title
                new_content['ep'] = int(ep)
                new_content['thumb'] = img
                new_content['text'] = description
                new_content['srcMedium'] = srcMedium
                new_content['srcHD'] = srcHD

                ul = soup2.select('.paginationEp')
                if ul:

                    ul_elements = ul[0]
                    li_elements = ul_elements.find_all('li')
                    fouth_li = li_elements[3]
                    a = fouth_li.select_one('a')['href']
                    response4 = requests.get(a, headers=headers)
                    soup3 = BeautifulSoup(response4.content, 'html.parser')

                    divName = soup3.select_one('.div_anime_names')
                    name = divName.select_one('h1').text
                    banner = soup3.select_one('.sub_animepage_img')
                    bannerImg = banner.select_one('img')['data-src']
                    
                    if not AnimeDetails.objects.filter(title=name).exists():
                        AnimeDetailsPage = {}
                        AnimeDetailsPage['title'] = name
                        AnimeDetailsPage['text'] = description
                        AnimeDetailsPage['thumb'] = bannerImg
                        AnimeDetailsAddict = AnimeDetails.objects.create(**AnimeDetailsPage)
                        anime_details = AnimeDetails.objects.get(title=name)
                        animeAdd = Anime.objects.create(**new_content, anime=anime_details)
                        anime_list.append(new_content)


                        

                    else:
                        anime_details = AnimeDetails.objects.get(title=name)
                        if not Anime.objects.filter(title=title).exists():
                            animeAdd = Anime.objects.create(**new_content, anime=anime_details)
                            anime_list.append(new_content)


                        
                    




            #     print("vem tuilutoooooo")

            
            #     if New.objects.filter(title = title['alt']).exists():
            #         continue
                
                
            #     date = article.find('time').text.strip().replace("\t", "")
            #     category = article.select_one('.cat-item').text
            #     url2 = article.select_one('a')

            #     url3 = url2['href']
                
            #     response2 = requests.get(url3)
            #     soup2 = BeautifulSoup(response2.content, 'html.parser')
            #     text = soup2.select_one('.content-left')
            #     subtitle = soup2.select_one('.excerpt').text
         
                
   
            #     pretty_text = text.prettify().strip().replace("\n", "").replace("\t", "")
                
            #     new_content['title'] = title['alt']
            #     new_content['subtitle'] = subtitle
            #     new_content['thumb'] = title['src']
            #     new_content['date'] = date
            #     new_content['category'] = category
            #     new_content['text'] = pretty_text
            #     new_addict = New.objects.create(**new_content)

            
            return Response(anime_list, status.HTTP_200_OK)

    def post(self, request: Request) -> Request:
        ...


        # print('Service running')
        # url = 'http://127.0.0.1:8000/api/animes/startscrappy/'
        # while True:
        #     response = requests.get(url)
        #     print(response.text)
        #     time.sleep(1800)
        