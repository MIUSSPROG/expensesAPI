from django.apps import AppConfig


class DailyexpensesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dailyExpenses'


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        from accounts import signals
