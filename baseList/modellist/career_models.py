from django.db import models
from .attr_models import NameAttr
from .skill_models import BaseSkillPro, BaseTalent

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


ESTATE = (
    ('Золотое', 'Золотое'),
    ('Медное', 'Медное'),
    ('Серебренное', 'Серебренное')
)
RANK_ESTATE = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
)


class Estate(models.Model):
    # Сословие
    name_estate = models.CharField(max_length=30, verbose_name='Сословие', choices=ESTATE)
    rank = models.CharField(max_length=2, verbose_name='Положение в сословии', choices=RANK_ESTATE)

    def __str__(self):
        return f'{self.name_estate} - {self.rank}'

    class Meta:
        verbose_name = 'Сословие'
        verbose_name_plural = 'Сословия'


class Class(models.Model):
    # Общий класс для карьеры
    name_class = models.CharField(max_length=30, verbose_name='Название класса', blank=True, null=True)
    available_nation = models.ManyToManyField(Nation, verbose_name='Перечень доступных народов', blank=True)
    description = models.TextField(verbose_name='Описание класса', blank=True)

    def __str__(self):
        return self.name_class

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Класс'


class Career(models.Model):
    # Должность
    name_class = models.ForeignKey(Class, on_delete=models.SET_NULL, verbose_name='Класс', blank=True, null=True)
    name_career = models.CharField(max_length=30, verbose_name='Должность', blank=True, null=True)

    RANKS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    )
    rank_career = models.CharField(max_length=2, verbose_name='Ступень карьеры', blank=True, choices=RANKS)

    estate = models.ForeignKey(Estate, on_delete=models.SET_NULL, verbose_name='Сословие и положение', blank=True,
                               null=True)
    available_attr = models.ManyToManyField(NameAttr, verbose_name='Доступные характеристики', blank=True)
    available_skills = models.ManyToManyField(BaseSkillPro, verbose_name='Доступные навыки', blank=True)
    available_talents = models.ManyToManyField(BaseTalent, verbose_name='Доступные таланты', blank=True)

    def __str__(self):
        return self.name_career

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должность'


class ListArchiveCarriers(models.Model):
    # Список предыдущих должностей
    archive = models.ManyToManyField(Career, verbose_name='Список должностей', blank=True)

    def __str__(self):
        return self.archive

    class Meta:
        verbose_name = 'Список должностей'
        verbose_name_plural = 'Списки должностей'