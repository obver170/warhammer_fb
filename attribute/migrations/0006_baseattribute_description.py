# Generated by Django 3.2.4 on 2021-07-23 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attribute', '0005_remove_baseattribute_numbers_of_steps'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseattribute',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание характеристики'),
        ),
    ]
