# Generated by Django 3.2.9 on 2022-03-07 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dailyExpenses', '0009_auto_20220307_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child',
            name='role',
        ),
        migrations.RemoveField(
            model_name='parent',
            name='role',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
