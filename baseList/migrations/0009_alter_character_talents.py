# Generated by Django 3.2.4 on 2021-07-24 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill2', '0011_talent'),
        ('baseList', '0008_character_talents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='talents',
            field=models.ManyToManyField(blank=True, to='skill2.Talent', verbose_name='Таланты'),
        ),
    ]