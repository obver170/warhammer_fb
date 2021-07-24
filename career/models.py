from django.db import models
from baseList.models import Nation

# Create your models here.

class Class(models.Model):
    name_class = models.CharField(max_length=30, verbose_name='Название класса', blank=True, null=True)
    available_nation = models.ManyToManyField(Nation, verbose_name='Перечень доступных народов', blank=True, null=True)

    def __str__(self):
        return self.name_class

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Класс'
