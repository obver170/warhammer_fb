from django.db import models


class Psychology(models.Model):
    # Модель описывает психические особенности
    name = models.CharField(max_length=30, verbose_name='Название', blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Психическая особенность'
        verbose_name_plural = 'Психические особенности'


class Mutation(models.Model):
    # Модель описывает мутации
    name = models.CharField(max_length=30, verbose_name='Название', blank=True, null=True)
    effect = models.CharField(max_length=100, verbose_name='Эффект', blank=True, null=True)
    description = models.TextField(verbose_name='Расширенное описание', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мутация'
        verbose_name_plural = 'Мутации'