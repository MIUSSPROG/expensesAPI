# Generated by Django 3.2.9 on 2022-04-09 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyExpenses', '0014_delete_invitation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='date',
            field=models.BigIntegerField(),
        ),
    ]
