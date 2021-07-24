from django.db import models
from baseList.models import Nation, Estate
from attribute.models import NameAttr
from skill2.models import BaseSkillPro


# Create your models here.


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

    def __str__(self):
        return self.name_career

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должность'
