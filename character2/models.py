from django.db import models


# Create your models here.

class BaseAttribute(models.Model):
    # Базовый класс для характеристики
    initial_value = models.IntegerField(verbose_name="Начальное значение", default=0)
    numbers_of_steps = models.IntegerField(verbose_name="Количество шагов", default=0)

    def __str__(self):
        return f'Начальное значение: {self.initial_value}, количество шагов: {self.numbers_of_steps}'


class WeaponSkill(BaseAttribute):
    # Ближний бой

    class Meta:
        verbose_name = 'Ближний бой'
        verbose_name_plural = 'Ближний бой'


class BallisticSkill(BaseAttribute):
    # Дальний бой

    class Meta:
        verbose_name = 'Дальний бой'
        verbose_name_plural = 'Дальний бой'


class Strength(BaseAttribute):
    # Сила

    class Meta:
        verbose_name = 'Сила'
        verbose_name_plural = 'Сила'


class Toughness(BaseAttribute):
    # Выносливость

    class Meta:
        verbose_name = 'Выносливость'
        verbose_name_plural = 'Выносливость'


class Initiative(BaseAttribute):
    # Инициатива

    class Meta:
        verbose_name = 'Инициатива'
        verbose_name_plural = 'Инициатива'


class Agility(BaseAttribute):
    # Проворство

    class Meta:
        verbose_name = 'Проворство'
        verbose_name_plural = 'Проворство'


class Dexterity(BaseAttribute):
    # Ловкость

    class Meta:
        verbose_name = 'Ловкость'
        verbose_name_plural = 'Ловкость'


class Intelligence(BaseAttribute):
    # Интеллект

    class Meta:
        verbose_name = 'Интеллект'
        verbose_name_plural = 'Интеллект'


class Willpower(BaseAttribute):
    # Сила воли

    class Meta:
        verbose_name = 'Сила воли'
        verbose_name_plural = 'Сила воли'


class Fellowship(BaseAttribute):
    # Харизма

    class Meta:
        verbose_name = 'Харизма'
        verbose_name_plural = 'Харизма'