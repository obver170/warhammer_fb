# Generated by Django 3.2.4 on 2021-07-24 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListOtherSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Название листа навыков')),
                ('skill', models.ManyToManyField(blank=True, to='skill2.SkillOther', verbose_name='Общий навык')),
            ],
            options={
                'verbose_name': 'Лист общих навыков',
                'verbose_name_plural': 'Листы общих навыков',
            },
        ),
    ]