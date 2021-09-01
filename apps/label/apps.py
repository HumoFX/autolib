from django.apps import AppConfig


class LabelConfig(AppConfig):
    name = 'apps.label'

    class Meta:
        verbose_name = 'Метка'
        verbose_plural_name = 'Метки'
