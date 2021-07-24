# Generated by Django 3.2.4 on 2021-07-24 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill2', '0002_listotherskills'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListProSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Название листа навыков')),
                ('skill', models.ManyToManyField(blank=True, to='skill2.SkillPro', verbose_name='Профессиональный навык')),
            ],
            options={
                'verbose_name': 'Лист профессиональных навыков',
                'verbose_name_plural': 'Листы профессиональных навыков',
            },
        ),
    ]