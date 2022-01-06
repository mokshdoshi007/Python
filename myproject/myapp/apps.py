from django.apps import AppConfig
from django.conf import settings

class MyappConfig(AppConfig):
    name = 'myapp'
    
    def ready(self):
        from myapp import scheduler