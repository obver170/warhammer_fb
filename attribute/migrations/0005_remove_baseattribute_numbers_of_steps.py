# Generated by Django 3.2.4 on 2021-07-23 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attribute', '0004_ballisticskill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseattribute',
            name='numbers_of_steps',
        ),
    ]
