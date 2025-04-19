from django.apps import AppConfig


class AppPawclockConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_pawclock'
    verbose_name = "Pawclock App"

    def ready(self):
        # Load test/dev data
        pass
