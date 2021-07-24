from django.db import models
from django.db import models
from .code import NamesOther, NamesProfessional

# Список от 0 до 100
STEPS = [(str(x), str(x)) for x in range(101)]


class SkillOther(models.Model):
    # Модель для профессиональных навыков
    names = NamesOther()
    choices = names.get_choice_names()
    name_skill = models.CharField(max_length=50, verbose_name='Название навыка', choices=choices)
    steps = models.CharField(max_length=3, verbose_name='Шаги развития', choices=STEPS, default='0')

    def __str__(self):
        return f'{self.name_skill} - {self.steps}'

    class Meta:
        verbose_name = 'Общий навык'
        verbose_name_plural = 'Общие навыки'


class SkillPro(models.Model):
    # Модель для профессиональных навыков
    names = NamesProfessional()
    choices = names.get_choice_names()
    name_skill = models.CharField(max_length=50, verbose_name='Название навыка', choices=choices)
    steps = models.CharField(max_length=3, verbose_name='Шаги развития', choices=STEPS, default='0')

    def __str__(self):
        return f'{self.name_skill} - {self.steps}'

    class Meta:
        verbose_name = 'Профессиональный навык'
        verbose_name_plural = 'Профессиональные навыки'
