# Generated by Django 3.2.4 on 2021-07-24 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skill2', '0003_listproskills'),
        ('baseList', '0005_alter_character_pro_skills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='other_skills',
        ),
        migrations.AddField(
            model_name='character',
            name='other_skills',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='skill2.listotherskills', verbose_name='Лист общих навыки'),
        ),
        migrations.AlterField(
            model_name='character',
            name='pro_skills',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='skill2.listproskills', verbose_name='Лист профессиональных навыки'),
        ),
    ]
