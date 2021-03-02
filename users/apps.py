from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'registration'

    def ready(self):
        from . import signals
