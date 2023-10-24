from django.apps import AppConfig
import time


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        while True:
            print('\n','Hello','\n')
            time.sleep(30)
