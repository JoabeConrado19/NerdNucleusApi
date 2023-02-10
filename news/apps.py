from django.apps import AppConfig
import requests
import schedule
import time


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'
    def ready(self):
        from AutoScrapper import updater
        updater.start()
        
