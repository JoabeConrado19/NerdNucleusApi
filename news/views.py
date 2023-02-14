from django.shortcuts import render
import time
import requests
from bs4 import BeautifulSoup
from news.models import New

# Create your views here.

from rest_framework.views import APIView, Response, Request, status
from .models import New
from django.forms.models import model_to_dict
from news.apps import AppConfig
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404


# Create your views here.
    

class NewView(APIView, PageNumberPagination):

    def get(self, request: Request) -> Request:
        news_list = []
        news = New.objects.all()
        for new in news:
            news_list.append(model_to_dict(new))

        reverse = list(reversed(news_list))
        result_page = self.paginate_queryset(reverse, request)
        

        return self.get_paginated_response(result_page)
        


    def post(self, request: Request) -> Request:
        ...

        # return Response(team_dict, status.HTTP_201_CREATED)


class NewDetailView(APIView):
    def get(self, request: Request, news_id: int) -> Response:
        new = get_object_or_404(New, id = news_id)
        new_response = model_to_dict(new)
        
        return Response(new_response, status.HTTP_200_OK)


    def delete(self, request: Request, news_id: int) -> Response:
       ...

        # return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request: Request, news_id: int) -> Response:
       ...


        # return Response(team_dict, status.HTTP_200_OK)

class NewStartScrappyView(APIView):
    def get(self, request: Request) -> Request:
            print('Execultando get')
            
            news_list = []
       
            url = 'https://jovemnerd.com.br/nerdbunker/'
            response = requests.get(url)

            soup = BeautifulSoup(response.content, 'html.parser')
            articles = soup.select('article')
            

            for article in articles:
                new_content = {}
                title = article.find('img')
            
                if New.objects.filter(title = title['alt']).exists():
                    continue
                
                
                date = article.find('time').text.strip().replace("\t", "")
                category = article.select_one('.cat-item').text
                url2 = article.select_one('a')

                url3 = url2['href']
                
                response2 = requests.get(url3)
                soup2 = BeautifulSoup(response2.content, 'html.parser')
                text = soup2.select_one('.content-left')
                subtitle = soup2.select_one('.excerpt').text
         
                
   
                pretty_text = text.prettify().strip().replace("\n", "").replace("\t", "")
                
                new_content['title'] = title['alt']
                new_content['subtitle'] = subtitle
                new_content['thumb'] = title['src']
                new_content['date'] = date
                new_content['category'] = category
                new_content['text'] = pretty_text
                new_addict = New.objects.create(**new_content)
                news_list.append(new_content)

            
            return Response(news_list, status.HTTP_200_OK)

    def post(self, request: Request) -> Request:
        print('Service running')
        url = 'http://127.0.0.1:8000/api/news/startscrappy/'
        while True:
            response = requests.get(url)
            print(response.text)
            time.sleep(1800)
        



        
