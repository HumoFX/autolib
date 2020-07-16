from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'User'
    verbose_name = 'Пользователи'

    def ready(self):
        import User.signal