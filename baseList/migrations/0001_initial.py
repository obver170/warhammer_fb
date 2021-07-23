# Generated by Django 3.2.4 on 2021-07-23 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('attribute', '0004_ballisticskill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Джон', max_length=30, verbose_name='Имя персонажа')),
                ('weaponSkill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attribute.weaponskill', verbose_name='Ближний бой')),
            ],
            options={
                'verbose_name': 'Персонаж',
                'verbose_name_plural': 'Персонажи',
            },
        ),
    ]