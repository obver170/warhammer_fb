# Generated by Django 3.2.4 on 2021-07-24 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0023_alter_otherskilllist_gamble'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otherskilllist',
            name='bribery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='skill.bribery', verbose_name='Подкуп'),
        ),
        migrations.AlterField(
            model_name='otherskilllist',
            name='charm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='skill.charm', verbose_name='Обаяние'),
        ),
        migrations.AlterField(
            model_name='otherskilllist',
            name='entertain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='skill.entertain', verbose_name='Артистизм'),
        ),
        migrations.AlterField(
            model_name='otherskilllist',
            name='gamble',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='skill.gamble', verbose_name='Азартные игры'),
        ),
        migrations.AlterField(
            model_name='otherskilllist',
            name='gossip',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='skill.gossip', verbose_name='Сплетничество'),
        ),
        migrations.AlterField(
            model_name='otherskilllist',
            name='haggle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='skill.haggle', verbose_name='Торговля'),
        ),
        migrations.AlterField(
            model_name='otherskilllist',
            name='leadership',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='skill.leadership', verbose_name='Лидерство'),
        ),
        migrations.AlterField(
            model_name='otherskilllist',
            name='outdoorSurvival',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='skill.outdoorsurvival', verbose_name='Выживание'),
        ),
        migrations.AlterField(
            model_name='professionalskilllist',
            name='bookSearches',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='skill.booksearches', verbose_name='Книжные изыскания'),
        ),
        migrations.AlterField(
            model_name='professionalskilllist',
            name='grade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='skill.grade', verbose_name='Оценка'),
        ),
        migrations.AlterField(
            model_name='professionalskilllist',
            name='knowledge',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='skill.knowledge', verbose_name='Знания'),
        ),
        migrations.AlterField(
            model_name='professionalskilllist',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='skill.language', verbose_name='Язык'),
        ),
        migrations.AlterField(
            model_name='professionalskilllist',
            name='prayer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='skill.prayer', verbose_name='Молитвословие'),
        ),
        migrations.AlterField(
            model_name='professionalskilllist',
            name='secretSigns',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='skill.secretsigns', verbose_name='Тайные знаки'),
        ),
        migrations.AlterField(
            model_name='professionalskilllist',
            name='trainingOfAnimals',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='skill.trainingofanimals', verbose_name='Дрессировка'),
        ),
        migrations.AlterField(
            model_name='professionalskilllist',
            name='treatment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='skill.treatment', verbose_name='Лечение'),
        ),
        migrations.AlterField(
            model_name='professionalskilllist',
            name='veterinarian',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='skill.veterinarian', verbose_name='Обращение с животными'),
        ),
    ]
