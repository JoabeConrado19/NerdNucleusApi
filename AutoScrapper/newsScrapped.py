from django.conf import settings
import requests

def schedule_api():
    response = requests.get("http://127.0.0.1:8000/api/news/startscrappy/")
    response2 = requests.get("http://127.0.0.1:8000/api/animes/startscrappy/")




