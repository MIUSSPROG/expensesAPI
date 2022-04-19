# Generated by Django 3.2.9 on 2022-03-07 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dailyExpenses', '0006_auto_20220303_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='child', to=settings.AUTH_USER_MODEL),
        ),
    ]