# Generated by Django 3.2.4 on 2021-07-24 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0016_professionalskilllist_prayer'),
        ('baseList', '0003_auto_20210723_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='other_skills',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='skill.otherskilllist', verbose_name='Общие навыки'),
        ),
        migrations.AddField(
            model_name='character',
            name='pro_skills',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='skill.professionalskilllist', verbose_name='Профессиональные навыки'),
        ),
    ]
