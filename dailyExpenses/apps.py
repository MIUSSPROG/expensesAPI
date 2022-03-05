from django.apps import AppConfig


class DailyexpensesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dailyExpenses'

    # def ready(self):
    #     import dailyExpenses.signal
