# Generated by Django 3.2.9 on 2022-03-07 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyExpenses', '0008_auto_20220307_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='login',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='child',
            name='password',
            field=models.CharField(max_length=500),
        ),
    ]
