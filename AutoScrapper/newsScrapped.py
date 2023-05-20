from django.conf import settings
import requests

def schedule_api():
    response = requests.get("https://nerdnucleusapidjango.onrender.com/api/news/startscrappy/")
    response2 = requests.get("https://nerdnucleusapidjango.onrender.com/api/animes/startscrappy/")




