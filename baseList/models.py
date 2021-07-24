from django.db import models

from attribute.models import AttributeList
from skill.models import OtherSkillList, ProfessionalSkillList

# Create your models here.
nation_list = ('Человек', 'Полурослик', 'Гном', 'Высший эльф', 'Лесной эльф')
NATION_TUPLE = [(x, x) for x in nation_list]


class Nation(models.Model):
    name_nation = models.CharField(max_length=30, verbose_name='Народ', choices=NATION_TUPLE)

    def __str__(self):
        return self.name_nation

    class Meta:
        verbose_name = 'Народ'
        verbose_name_plural = 'Народы'


class Character(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя персонажа', default='Джон')
    nation = models.ForeignKey(Nation, verbose_name='Народ', on_delete=models.SET_NULL, blank=True, null=True)

    init_attribute = models.ForeignKey(AttributeList, on_delete=models.SET_NULL, default=0,
                                       verbose_name='Начальные значения характеристик', blank=True, null=True)
    add_weaponSkill = models.CharField(max_length=3, verbose_name='Шаги в Ближний бой', default='0')
    add_ballisticSkill = models.CharField(max_length=3, verbose_name='Шаги в Дальний бой', default='0')
    add_strength = models.CharField(max_length=3, verbose_name='Шаги в Сила', default='0')
    add_toughness = models.CharField(max_length=3, verbose_name='Шаги в Выносливость', default='0')
    add_initiative = models.CharField(max_length=3, verbose_name='Шаги в Инициатива', default='0')
    add_agility = models.CharField(max_length=3, verbose_name='Шаги в Проворство', default='0')
    add_dexterity = models.CharField(max_length=3, verbose_name='Шаги в Ловкость', default='0')
    add_intelligence = models.CharField(max_length=3, verbose_name='Шаги в Интеллект', default='0')
    add_willpower = models.CharField(max_length=3, verbose_name='Шаги в Сила воли', default='0')
    add_fellowship = models.CharField(max_length=3, verbose_name='Шаги в Харизма', default='0')

    other_skills = models.ForeignKey(OtherSkillList, on_delete=models.CASCADE, verbose_name='Шаги в общих навыках',
                                     blank=True, null=True)
    pro_skills = models.ForeignKey(ProfessionalSkillList, on_delete=models.CASCADE,
                                   verbose_name='Шаги в профессиональных навыках', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'
