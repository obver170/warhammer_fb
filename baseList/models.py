from django.db import models

from attribute.models import AttributeList
from skill2.models import ListOtherSkills, ListProSkills, Talent
from career.models import Nation, Estate, Career, ListArchiveCarriers


# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя персонажа', default='Джон')
    nation = models.ForeignKey(Nation, verbose_name='Народ', on_delete=models.SET_NULL, blank=True, null=True)
    age = models.CharField(max_length=4, verbose_name='Возраст', blank=True, null=True)
    height = models.CharField(max_length=4, verbose_name='Рост', blank=True, null=True)
    hair = models.CharField(max_length=20, verbose_name='Волосы', blank=True, null=True)
    estate = models.ForeignKey(Estate, verbose_name='Статус', on_delete=models.SET_NULL, blank=True, null=True)

    current_career = models.ForeignKey(Career, on_delete=models.SET_NULL, blank=True, null=True,
                                       verbose_name='Текущая должность')
    archive_career = models.ManyToManyField(ListArchiveCarriers, verbose_name='Ранние должности', blank=True)

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

    other_skills = models.ForeignKey(ListOtherSkills, on_delete=models.SET_NULL, blank=True, null=True,
                                     verbose_name='Лист общих навыков')
    pro_skills = models.ForeignKey(ListProSkills, on_delete=models.SET_NULL, blank=True, null=True,
                                   verbose_name='Лист профессиональных навыков')
    talents = models.ManyToManyField(Talent, verbose_name='Таланты', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'
