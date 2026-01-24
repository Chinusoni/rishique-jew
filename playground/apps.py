from django.apps import AppConfig

class PlaygroundConfig(AppConfig): # Changed from MainConfig
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'playground'