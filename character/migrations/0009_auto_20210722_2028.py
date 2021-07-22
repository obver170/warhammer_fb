# Generated by Django 3.2.4 on 2021-07-22 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0008_auto_20210722_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='NameSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_skill', models.CharField(max_length=30, verbose_name='Название навыка')),
                ('specialization', models.CharField(blank=True, max_length=30, verbose_name='Специализация навыка')),
                ('description', models.TextField(blank=True, verbose_name='Описание навыка')),
                ('is_other', models.BooleanField(default=False, verbose_name='Является общим навыком?')),
            ],
            options={
                'verbose_name': 'Название навыка',
                'verbose_name_plural': 'Название навыка',
            },
        ),
        migrations.RemoveField(
            model_name='skill',
            name='description',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='is_other',
        ),
        migrations.AlterField(
            model_name='skill',
            name='name_skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='character.nameskill', verbose_name='Название навыка'),
        ),
    ]
