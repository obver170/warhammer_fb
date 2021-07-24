# Generated by Django 3.2.4 on 2021-07-24 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skill2', '0002_listotherskills'),
        ('baseList', '0003_auto_20210724_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='pro_skills',
        ),
        migrations.AddField(
            model_name='character',
            name='pro_skills',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='skill2.listotherskills', verbose_name='Профессиональные навыки'),
        ),
    ]
