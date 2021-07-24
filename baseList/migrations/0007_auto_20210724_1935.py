# Generated by Django 3.2.4 on 2021-07-24 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skill2', '0003_listproskills'),
        ('baseList', '0006_auto_20210724_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='other_skills',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='skill2.listotherskills', verbose_name='Лист общих навыков'),
        ),
        migrations.AlterField(
            model_name='character',
            name='pro_skills',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='skill2.listproskills', verbose_name='Лист профессиональных навыков'),
        ),
    ]