from django.db import models


# Create your models here.


class Step(models.Model):
    step = models.CharField(max_length=3, verbose_name='Значение', default='0')

    def __str__(self):
        return self.step

    class Meta:
        verbose_name = 'Шаги развития'
        verbose_name_plural = 'Шаги развития'


class BaseAttribute(models.Model):
    name_attribute: str = ''
    numbers_of_steps = models.ForeignKey(Step, on_delete=models.CASCADE, verbose_name='Количество шагов развития')

    def __str__(self):
        return f'{self.name_attribute} - {self.numbers_of_steps}'


class WeaponSkill(BaseAttribute):
    name_attribute = 'Ближний бой'

    class Meta:
        verbose_name = 'Ближний бой'
        verbose_name_plural = 'Ближний бой'
