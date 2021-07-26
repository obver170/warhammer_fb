from django.db import models
from .code.attr_code import ListNamesAttr


# Create your models here.
# Список от 0 до 100
STEPS = [(str(x), str(x)) for x in range(101)]


class NameAttr(models.Model):
    # Названия характеристик (для привязки к другим таблицам, таким как карьеры, навыки)
    # Может в переделаю характеристики так же как навыки
    names = ListNamesAttr()
    choices = names.get_choice_names()
    name_attr = models.CharField(max_length=30, verbose_name='Характеристика', blank=True, choices=choices)
    description = models.TextField(verbose_name='Описание характеристики', blank=True)

    def __str__(self):
        return self.name_attr

    class Meta:
        verbose_name = 'Название характеристики'
        verbose_name_plural = 'Названия характеристик'


class BaseAttribute(models.Model):
    # Основа для всех характеристик
    name_attribute: str = ''
    name_attr = models.ForeignKey(NameAttr, on_delete=models.SET_NULL, verbose_name='Характеристика', null=True,
                                  blank=True)
    initial_meaning = models.CharField(max_length=3, verbose_name='Начальное значение', default='0', choices=STEPS)

    def __str__(self):
        return f'{self.initial_meaning}'


class WeaponSkill(BaseAttribute):
    name_attribute = 'Ближний бой'

    class Meta:
        verbose_name = 'Ближний бой'
        verbose_name_plural = 'Ближний бой'


class BallisticSkill(BaseAttribute):
    name_attribute = 'Дальний бой'

    class Meta:
        verbose_name = 'Дальний бой'
        verbose_name_plural = 'Дальний бой'


class Strength(BaseAttribute):
    name_attribute = 'Сила'

    class Meta:
        verbose_name = 'Сила'
        verbose_name_plural = 'Сила'


class Toughness(BaseAttribute):
    name_attribute = 'Выносливость'

    class Meta:
        verbose_name = 'Выносливость'
        verbose_name_plural = 'Выносливость'


class Initiative(BaseAttribute):
    name_attribute = 'Инициатива'

    class Meta:
        verbose_name = 'Инициатива'
        verbose_name_plural = 'Инициатива'


class Agility(BaseAttribute):
    name_attribute = 'Проворство'

    class Meta:
        verbose_name = 'Проворство'
        verbose_name_plural = 'Проворство'


class Dexterity(BaseAttribute):
    name_attribute = 'Ловкость'

    class Meta:
        verbose_name = 'Ловкость'
        verbose_name_plural = 'Ловкость'


class Intelligence(BaseAttribute):
    name_attribute = 'Интеллект'

    class Meta:
        verbose_name = 'Интеллект'
        verbose_name_plural = 'Интеллект'


class Willpower(BaseAttribute):
    name_attribute = 'Сила воли'

    class Meta:
        verbose_name = 'Сила воли'
        verbose_name_plural = 'Сила воли'


class Fellowship(BaseAttribute):
    name_attribute = 'Харизма'

    class Meta:
        verbose_name = 'Харизма'
        verbose_name_plural = 'Харизма'


class AttributeList(models.Model):

    name_list = models.CharField(max_length=20, verbose_name='Название набора', default='Стандарт')
    weaponSkill = models.ForeignKey(WeaponSkill, on_delete=models.CASCADE, verbose_name='Ближний бой')
    ballisticSkill = models.ForeignKey(BallisticSkill, on_delete=models.CASCADE, verbose_name='Дальний бой')
    strength = models.ForeignKey(Strength, on_delete=models.CASCADE, verbose_name='Сила')
    toughness = models.ForeignKey(Toughness, on_delete=models.CASCADE, verbose_name='Выносливость')
    initiative = models.ForeignKey(Initiative, on_delete=models.CASCADE, verbose_name='Инициатива')
    agility = models.ForeignKey(Agility, on_delete=models.CASCADE, verbose_name='Проворство')
    dexterity = models.ForeignKey(Dexterity, on_delete=models.CASCADE, verbose_name='Ловкость')
    intelligence = models.ForeignKey(Intelligence, on_delete=models.CASCADE, verbose_name='Интеллект')
    willpower = models.ForeignKey(Willpower, on_delete=models.CASCADE, verbose_name='Сила воли')
    fellowship = models.ForeignKey(Fellowship, on_delete=models.CASCADE, verbose_name='Харизма')

    def __str__(self):
        return f'ББ:{self.weaponSkill}, ДБ:{self.ballisticSkill}, С:{self.strength}, ' \
               f'В:{self.toughness}, И:{self.initiative}, Пр:{ self.agility}, Л:{self.dexterity}' \
               f' Инт:{self.intelligence}, СВ:{self.willpower}, Х:{self.fellowship}'

    class Meta:
        verbose_name = 'Набор характеристик'
        verbose_name_plural = 'Наборы характеристик'
