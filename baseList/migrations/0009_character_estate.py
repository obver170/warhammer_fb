# Generated by Django 3.2.4 on 2021-07-24 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseList', '0008_estate'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='estate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='baseList.estate', verbose_name='Статус'),
        ),
    ]
