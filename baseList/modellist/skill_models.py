from django.db import models
from django.db import models
from .code.skill_code import NamesOther, NamesProfessional
from .attr_models import NameAttr

# Список от 0 до 100
STEPS = [(str(x), str(x)) for x in range(101)]


class BaseSkillOther(models.Model):
    # Название общего навыка
    names = NamesOther()
    choices = names.get_choice_names()
    name_skill = models.CharField(max_length=50, verbose_name='Название навыка', choices=choices, null=True,
                                  blank=True, )
    attr = models.ForeignKey(NameAttr, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name='Базовая характеристика')
    description = models.TextField(verbose_name='Описание навыка', blank=True)

    def __str__(self):
        return self.name_skill

    class Meta:
        verbose_name = 'Общий навык абстрактный'
        verbose_name_plural = 'Общие навыки абстрактные'


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
        verbose_name = 'Профессиональный навык абстрактный'
        verbose_name_plural = 'Профессиональные навыки абстрактные'


class SkillOther(models.Model):
    # Модель для общих навыков
    base = models.ForeignKey(BaseSkillOther, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name='Навык')
    steps = models.CharField(max_length=3, verbose_name='Шаги развития', choices=STEPS, null=True,
                             blank=True, default='0')

    def __str__(self):
        return f'{self.base} - {self.steps}'

    class Meta:
        verbose_name = 'Общий навык персонажа'
        verbose_name_plural = 'Общие навыки персонажа'


class SkillPro(models.Model):
    # Модель для профессиональных навыков
    base = models.ForeignKey(BaseSkillPro, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name='Навык')
    steps = models.CharField(max_length=3, verbose_name='Шаги развития', choices=STEPS, default='0')

    def __str__(self):
        return f'{self.base} - {self.steps}'

    class Meta:
        verbose_name = 'Профессиональный навык персонажа'
        verbose_name_plural = 'Профессиональные навыки персонажа'


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





class BaseTalent(models.Model):
    # Талант общее описание
    name = models.CharField(max_length=30, verbose_name='Название таланта', blank=True)
    max = models.CharField(max_length=100, verbose_name='Максимальный уровень таланта', blank=True)
    depend_attr = models.ForeignKey(NameAttr, on_delete=models.SET_NULL, verbose_name='Связанная характеристика',
                                    blank=True, null=True)
    depend_skill_other = models.ForeignKey(BaseSkillOther, on_delete=models.SET_NULL,
                                           verbose_name='Бонус на проверку общего навыка', blank=True, null=True)
    depend_skill_pro = models.ForeignKey(BaseSkillPro, on_delete=models.SET_NULL,
                                         verbose_name='Бонус на проверку профессионального навыка',
                                         blank=True, null=True)
    description = models.TextField(verbose_name='Описание таланта', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Талант абстрактный'
        verbose_name_plural = 'Таланты абстрактные'


class Talent(models.Model):
    base = models.ForeignKey(BaseTalent, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Талант')
    lvl = models.CharField(max_length=3, choices=STEPS, verbose_name='Уровень развития',  blank=True, null=True)

    def __str__(self):
        return f'{self.base} - {self.lvl}'

    class Meta:
        verbose_name = 'Талант персонажа'
        verbose_name_plural = 'Таланты персонажа'