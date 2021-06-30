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