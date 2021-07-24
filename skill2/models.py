from django.db import models
from django.db import models
from .code import NamesOther, NamesProfessional
from attribute.models import NameAttr

# Список от 0 до 100
STEPS = [(str(x), str(x)) for x in range(101)]


class BaseSkillOther(models.Model):
    # Название общего навыка
    names = NamesOther()
    choices = names.get_choice_names()
    name_skill = models.CharField(max_length=50, verbose_name='Название навыка', choices=choices, null=True,
                                  blank=True,)
    attr = models.ForeignKey(NameAttr, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name='Базовая характеристика')
    description = models.TextField(verbose_name='Описание навыка', blank=True)

    def __str__(self):
        return self.name_skill

    class Meta:
        verbose_name = 'Название общего навыка'
        verbose_name_plural = 'Названия общих навыков'


class BaseSkillPro(models.Model):
    # Название профессионального навыка
    names = NamesProfessional()
    choices = names.get_choice_names()
    name_skill = models.CharField(max_length=50, verbose_name='Название навыка', choices=choices, null=True,
                                  blank=True)
    attr = models.ForeignKey(NameAttr, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name='Базовая характеристика')
    description = models.TextField(verbose_name='Описание навыка', blank=True)

    def __str__(self):
        return self.name_skill

    class Meta:
        verbose_name = 'Название профессионального навыка'
        verbose_name_plural = 'Названия профессиональных навыков'


class SkillOther(models.Model):
    # Модель для общих навыков
    base = models.ForeignKey(BaseSkillOther, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name='Навык')
    steps = models.CharField(max_length=3, verbose_name='Шаги развития', choices=STEPS, null=True,
                             blank=True, default='0')

    def __str__(self):
        return f'{self.base} - {self.steps}'

    class Meta:
        verbose_name = 'Общий навык с шагами'
        verbose_name_plural = 'Общие навыки с шагами'


class SkillPro(models.Model):
    # Модель для профессиональных навыков
    base = models.ForeignKey(BaseSkillPro, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name='Навык')
    steps = models.CharField(max_length=3, verbose_name='Шаги развития', choices=STEPS, default='0')

    def __str__(self):
        return f'{self.base} - {self.steps}'

    class Meta:
        verbose_name = 'Профессиональный навык'
        verbose_name_plural = 'Профессиональные навыки'


class ListOtherSkills(models.Model):
    # Список общих навыков для прикрепления к листу персонажа
    name = models.CharField(max_length=30, verbose_name='Название листа навыков', blank=True, null=True)
    skill = models.ManyToManyField(SkillOther, verbose_name='Общий навык', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Лист общих навыков'
        verbose_name_plural = 'Листы общих навыков'


class ListProSkills(models.Model):
    # Список профессиональных навыков для прикрепления к листу персонажа
    name = models.CharField(max_length=30, verbose_name='Название листа навыков', blank=True, null=True)
    skill = models.ManyToManyField(SkillPro, verbose_name='Профессиональный навык', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Лист профессиональных навыков'
        verbose_name_plural = 'Листы профессиональных навыков'
