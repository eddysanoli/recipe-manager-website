from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # Import the signals created to use them properly
    # (Done according to the documentation)
    def ready(self):
        import users.signals
