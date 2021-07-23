# Generated by Django 3.2.4 on 2021-07-23 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attribute', '0007_agility_dexterity_fellowship_initiative_intelligence_strength_toughness_willpower'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttributeList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, verbose_name='Название набора характеристик')),
                ('agility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attribute.agility', verbose_name='Проворство')),
                ('ballisticSkill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attribute.ballisticskill', verbose_name='Дальний бой')),
                ('dexterity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attribute.dexterity', verbose_name='Ловкость')),
                ('fellowship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attribute.fellowship', verbose_name='Харизма')),
                ('initiative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attribute.initiative', verbose_name='Инициатива')),
                ('intelligence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attribute.intelligence', verbose_name='Интеллект')),
                ('strength', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attribute.strength', verbose_name='Сила')),
                ('toughness', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attribute.toughness', verbose_name='Выносливость')),
                ('weaponSkill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attribute.weaponskill', verbose_name='Ближний бой')),
                ('willpower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attribute.willpower', verbose_name='Сила воли')),
            ],
            options={
                'verbose_name': 'Набор характеристик',
                'verbose_name_plural': 'Наборы характеристик',
            },
        ),
    ]