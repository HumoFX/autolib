from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'apps.user'
    verbose_name = 'Пользователи'

    def ready(self):
        import api.v1.user.signal
