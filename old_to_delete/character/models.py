from django.db import models


# Create your models here.

class Eyes(models.Model):
    # Глаза
    color = models.CharField(max_length=20, verbose_name='Цвет глаз', default='Карие')
    description = models.TextField(verbose_name='Описание глаз', blank=True)

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = 'Глаза'
        verbose_name_plural = 'Глаза'


class Nation(models.Model):
    # Народ (Раса)
    name_nation = models.CharField(max_length=20, verbose_name='Народ персонажа', default='Человек')
    description = models.TextField(verbose_name='Описание народа', blank=True)

    def __str__(self):
        return self.name_nation

    class Meta:
        verbose_name = 'Народ'
        verbose_name_plural = 'Народы'


class Hair(models.Model):
    # Волосы
    color = models.CharField(max_length=20, verbose_name='Цвет волос', default='Коричнивые')
    description = models.TextField(verbose_name='Описание прически', blank=True)

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = 'Волосы'
        verbose_name_plural = 'Волосы'


class Sex(models.Model):
    # Пол
    SEX = (
        ('Men', 'Мужчина'),
        ('Women', 'Женщина'),
    )
    sex = models.CharField(max_length=5, choices=SEX, verbose_name='Пол')

    def __str__(self):
        return self.sex

    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Пол'


class Metal(models.Model):
    # Сословие
    METAL = (
        ('Золотое', 'Золотое'),
        ('Серебряное', 'Серебряное'),
        ('Медное', 'Медное'),
    )
    metal = models.CharField(max_length=10, choices=METAL, verbose_name='Сословие')
    description = models.TextField(verbose_name='Описание сословия', blank=True)

    def __str__(self):
        return self.metal

    class Meta:
        verbose_name = 'Сословие'
        verbose_name_plural = 'Сословия'


class NumberMetal(models.Model):
    # Положение в сословии
    NUMBER = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    )

    number = models.CharField(max_length=2, choices=NUMBER, verbose_name='Положение в сословии')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Положение в сословии'
        verbose_name_plural = 'Положение в сословии'


class Status(models.Model):
    # Статус персонажа
    metal = models.ForeignKey(Metal, on_delete=models.CASCADE, default='cuprum')
    number = models.ForeignKey(NumberMetal, on_delete=models.CASCADE, default='1')
    description = models.TextField(verbose_name='Описание статуса', blank=True)

    def __str__(self):
        return f'Сословие {self.metal}, положение внутри сословия - {self.number}'

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Talent(models.Model):
    # Описание талантов
    name_talent = models.CharField(max_length=30, verbose_name='Название таланта')
    description = models.TextField(verbose_name='Описание таланта', blank=True)
    max_rank = models.CharField(max_length=100, verbose_name='Максимальный уровень таланта', blank=True)

    def __str__(self):
        return self.name_talent

    class Meta:
        verbose_name = 'Талант'
        verbose_name_plural = 'Таланты'


class CurrentTalent(models.Model):
    # Талант и его текущий уровень
    talent = models.ForeignKey(Talent, on_delete=models.CASCADE, verbose_name='Талант')
    rank = models.CharField(max_length=3, verbose_name='Уровень таланта', default='1')

    def __str__(self):
        return f'{self.talent} ({self.rank})'

    class Meta:
        verbose_name = 'Талант и его текущий уровень'
        verbose_name_plural = 'Талант и его текущий уровень'


class Class(models.Model):
    name_class = models.CharField(max_length=15, verbose_name='Название класса')
    description = models.TextField(verbose_name='Описание класса', blank=True)

    def __str__(self):
        return self.name_class

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'


class Career(models.Model):
    # Карьера
    name_career = models.CharField(max_length=35, verbose_name='Название карьеры')
    description = models.TextField(verbose_name='Описание карьеры', blank=True)
    name_class = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name='Название класса')

    def __str__(self):
        return f'карьера: {self.name_career}, класс: {self.name_class}'

    class Meta:
        verbose_name = 'Карьера'
        verbose_name_plural = 'Карьеры'


class Species(models.Model):
    # Ступень карьеры/должность
    name_species = models.CharField(max_length=40, verbose_name='Название ступени карьеры (должность)')
    step = models.CharField(max_length=2, verbose_name='Порядковый номер ступени')
    career = models.ForeignKey(Career, on_delete=models.CASCADE, verbose_name='Карьера')
    is_current = models.BooleanField(default=False, verbose_name='Текущая должность')

    def __str__(self):
        return f'Должность: {self.name_species}, {self.career}. Текущая должность? - {self.is_current}'

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class NameAttribute(models.Model):
    # Название характеристики
    name_attribute = models.CharField(max_length=20, verbose_name='Название характеристики')
    description = models.TextField(verbose_name='Описание характеристики', blank=True)

    def __str__(self):
        return self.name_attribute

    class Meta:
        verbose_name = 'Название характеристики'
        verbose_name_plural = 'Название характеристики'


class Attribute(models.Model):
    # Характеристика
    name_attribute = models.ForeignKey(NameAttribute, on_delete=models.CASCADE, verbose_name='Название характеристики')
    start = models.CharField(max_length=3, verbose_name='Начальное значение')
    steps = models.CharField(max_length=3, verbose_name='Сделанные шаги', blank=True)

    def __str__(self):
        return f'{self.name_attribute} - {self.start} - {self.steps}'

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'


class SetAttributes(models.Model):
    # Набор атрибутов
    name_set_attribute = models.CharField(max_length=30, verbose_name='Название набора характеристик', blank=True)
    attributes = models.ManyToManyField(Attribute, verbose_name='Набор характеристик')

    def __str__(self):
        return self.name_set_attribute

    class Meta:
        verbose_name = 'Набор характеристик'
        verbose_name_plural = 'Набор характеристик'


class NameSkill(models.Model):
    # Название навыка
    name_skill = models.CharField(max_length=30, verbose_name='Название навыка')
    specialization = models.CharField(max_length=30, verbose_name='Специализация навыка', blank=True)
    description = models.TextField(verbose_name='Описание навыка', blank=True)
    is_other = models.BooleanField(default=False, verbose_name='Является общим навыком?')
    base_attribute = models.ForeignKey(NameAttribute, on_delete=models.CASCADE, verbose_name='Базовая характеристика')

    def __str__(self):
        return self.name_skill

    class Meta:
        verbose_name = 'Название навыка'
        verbose_name_plural = 'Название навыка'


class Skill(models.Model):
    # Навыки
    name_skill = models.ForeignKey(NameSkill, on_delete=models.CASCADE, verbose_name='Название навыка')
    start = models.CharField(max_length=3, verbose_name='Начальное значение')
    steps = models.CharField(max_length=3, verbose_name='Сделанные шаги', blank=True)

    def __str__(self):
        return f'{self.name_skill} - {self.start} - {self.steps}'

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'


class Character(models.Model):
    # Персонаж
    name = models.CharField(max_length=20, verbose_name='Имя', default='Рик')
    age = models.CharField(max_length=4, verbose_name='Возраст', default='33')
    height = models.CharField(max_length=4, verbose_name='Рост', default='174')
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE, verbose_name='Пол')
    eyes = models.ForeignKey(Eyes, on_delete=models.CASCADE, verbose_name='Глаза')
    hair = models.ForeignKey(Hair, on_delete=models.CASCADE, verbose_name='Волосы')
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE, verbose_name='Народ')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Статус персонажа')
    talents = models.ManyToManyField(CurrentTalent, verbose_name='Таланты')
    species = models.ManyToManyField(Species, verbose_name='Должности', blank=True)
    attributes = models.ManyToManyField(Attribute, verbose_name='Характеристики')
    # set_attributes = models.ForeignKey(SetAttributes, on_delete=models.CASCADE, verbose_name='Набор атрибутов',
    #                                    null=True)
    skills = models.ManyToManyField(Skill, verbose_name='Навыки')

    def __str__(self):
        return f'{self.name} из народа {self.nation}'

    class Meta:
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'
