from django.db import models
from baseList.models import Nation, Estate


# Create your models here.


class Class(models.Model):
    # Общий класс для карьеры
    name_class = models.CharField(max_length=30, verbose_name='Название класса', blank=True, null=True)
    available_nation = models.ManyToManyField(Nation, verbose_name='Перечень доступных народов', blank=True)

    def __str__(self):
        return self.name_class

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Класс'


class Career(models.Model):
    # Должность
    name_career = models.CharField(max_length=30, verbose_name='Должность', blank=True, null=True)
    name_class = models.ForeignKey(Class, on_delete=models.SET_NULL, verbose_name='Класс', blank=True, null=True)
    estate = models.ForeignKey(Estate, on_delete=models.SET_NULL, verbose_name='Сословие и положение', blank=True,
                               null=True)

    def __str__(self):
        return self.name_career

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должность'
