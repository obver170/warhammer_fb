# Generated by Django 3.2.4 on 2021-06-30 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0005_auto_20210630_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='current_species',
        ),
        migrations.AddField(
            model_name='character',
            name='species',
            field=models.ManyToManyField(blank=True, null=True, to='character.Species', verbose_name='Должности'),
        ),
        migrations.AddField(
            model_name='species',
            name='is_current',
            field=models.BooleanField(default=False, verbose_name='Текущая должность'),
        ),
        migrations.DeleteModel(
            name='SetArchiveSpecies',
        ),
    ]
