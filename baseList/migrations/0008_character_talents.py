# Generated by Django 3.2.4 on 2021-07-24 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill2', '0011_talent'),
        ('baseList', '0007_auto_20210724_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='talents',
            field=models.ManyToManyField(blank=True, null=True, to='skill2.Talent', verbose_name='Таланты'),
        ),
    ]
