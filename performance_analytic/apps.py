from django.apps import AppConfig

class PerformanceAnalyticConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "performance_analytic"

    def ready(self):
        import performance_analytic.signals  # Đảm bảo signals.py được import