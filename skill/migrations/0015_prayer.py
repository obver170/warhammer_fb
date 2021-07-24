# Generated by Django 3.2.4 on 2021-07-23 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0014_auto_20210723_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prayer',
            fields=[
                ('baseskill_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='skill.baseskill')),
            ],
            options={
                'verbose_name': 'Молитвословие',
                'verbose_name_plural': 'Молитвословие',
            },
            bases=('skill.baseskill',),
        ),
    ]