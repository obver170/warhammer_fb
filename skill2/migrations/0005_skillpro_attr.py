# Generated by Django 3.2.4 on 2021-07-24 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attribute', '0014_auto_20210724_1935'),
        ('skill2', '0004_skillother_attr'),
    ]

    operations = [
        migrations.AddField(
            model_name='skillpro',
            name='attr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='attribute.nameattr', verbose_name='Базовая характеристика'),
        ),
    ]