from django.apps import AppConfig
import os
from .views import train_nlp_model

class BotAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bot_app'

    def ready(self):
        model_path = 'model/trained_model'
        if not os.path.exists(model_path):
            print("Training NLP model....")
            train_nlp_model()
            print("Model training completed.")