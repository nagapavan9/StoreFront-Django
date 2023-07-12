from django.apps import AppConfig


class StoreCustomConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store_custom'

    def ready(self) -> None:
        from .signals import handlers