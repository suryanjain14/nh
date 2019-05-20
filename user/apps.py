from django.apps import AppConfig


class RegisterConfig(AppConfig):
    name = 'user'

    def ready(self):
        import user.signals
