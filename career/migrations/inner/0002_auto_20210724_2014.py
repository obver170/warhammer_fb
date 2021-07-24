# Generated by Django 3.2.4 on 2021-07-24 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attribute', '0014_auto_20210724_1935'),
        ('career', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='available_attr',
            field=models.ManyToManyField(blank=True, to='attribute.NameAttr', verbose_name='Доступные характеристики'),
        ),
        migrations.AddField(
            model_name='career',
            name='rank_career',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=2, verbose_name='Ступень карьеры'),
        ),
    ]