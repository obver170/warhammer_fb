# Generated by Django 3.2.4 on 2021-07-24 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attribute', '0015_alter_nameattr_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='nameattr',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание характеристики'),
        ),
    ]
