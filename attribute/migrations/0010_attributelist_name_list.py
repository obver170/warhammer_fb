# Generated by Django 3.2.4 on 2021-07-23 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attribute', '0009_remove_attributelist_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='attributelist',
            name='name_list',
            field=models.CharField(default='Стандарт', max_length=20, verbose_name='Название набора'),
        ),
    ]