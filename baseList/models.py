from django.db import models

from .modellist.health_models import Psychology, Mutation
# from attribute.models import AttributeList
from .modellist.attr_models import AttributeList
# from skill2.models import ListOtherSkills, ListProSkills, Talent
from .modellist.skill_models import ListOtherSkills, ListProSkills, Talent
# from career.models import Nation, Estate, Career, ListArchiveCarriers
from .modellist.career_models import Nation, Estate, Career, ListArchiveCarriers




class Eyes(models.Model):
    # Модель описывает глаза персонажа
    color = models.CharField(max_length=20, verbose_name='Цвет глаз', blank=True, null=True)
    description = models.CharField(max_length=60, verbose_name='Описание глаз', blank=True, null=True)

    def __str__(self):
        return f'{self.color} {self.description}'

    class Meta:
        verbose_name = 'Глаза'
        verbose_name_plural = 'Глаза'


class Movement(models.Model):
    # Модель описывает скорость передвижения
    movement = models.CharField(max_length=3, verbose_name='Скорость', blank=True, null=True)
    walk = models.CharField(max_length=3, verbose_name='Скорость шагом (ярдов за ход)', blank=True, null=True)
    run = models.CharField(max_length=3, verbose_name='Скорость бегом (ярдов за ход)', blank=True, null=True)

    def __str__(self):
        return self.movement

    class Meta:
        verbose_name = 'Перемещение'
        verbose_name_plural = 'Перемещение'


class Character(models.Model):
    # Модель сводит всю информацию об игровом персонаже (лист персонажа)
    name = models.CharField(max_length=30, verbose_name='Имя персонажа', default='Джон')
    nation = models.ForeignKey(Nation, verbose_name='Народ', on_delete=models.SET_NULL, blank=True, null=True)
    age = models.CharField(max_length=4, verbose_name='Возраст', blank=True, null=True)
    height = models.CharField(max_length=4, verbose_name='Рост', blank=True, null=True)
    hair = models.CharField(max_length=20, verbose_name='Волосы', blank=True, null=True)
    eyes = models.ForeignKey(Eyes, verbose_name='Глаза', on_delete=models.SET_NULL, blank=True, null=True)

    estate = models.ForeignKey(Estate, verbose_name='Статус', on_delete=models.SET_NULL, blank=True, null=True)
    current_career = models.ForeignKey(Career, on_delete=models.SET_NULL, blank=True, null=True,
                                       verbose_name='Текущая должность')
    archive_career = models.ManyToManyField(ListArchiveCarriers, verbose_name='Ранние должности', blank=True)

    fate = models.CharField(max_length=3, verbose_name='Судьба', blank=True, null=True)
    fortune = models.CharField(max_length=3, verbose_name='Удача', blank=True, null=True)
    resilience = models.CharField(max_length=3, verbose_name='Упорство', blank=True, null=True)
    resolve = models.CharField(max_length=3, verbose_name='Решимость', blank=True, null=True)
    motivation = models.CharField(max_length=30, verbose_name='Мотивация', blank=True, null=True)
    exp_current = models.CharField(max_length=5, verbose_name='Запас опыта', blank=True, null=True)
    exp_spent = models.CharField(max_length=5, verbose_name='Портаченый опыт', blank=True, null=True)
    short_ambition = models.CharField(max_length=100, verbose_name='Краткосрочная амбиция', blank=True, null=True)
    long_ambition = models.CharField(max_length=100, verbose_name='Долгосрочная амбиция', blank=True, null=True)

    movement = models.ForeignKey(Movement, on_delete=models.SET_NULL, default=0, verbose_name='Скорость', blank=True,
                                 null=True)

    init_attribute = models.ForeignKey(AttributeList, on_delete=models.SET_NULL, default=0,
                                       verbose_name='Начальные значения характеристик', blank=True, null=True)
    add_weaponSkill = models.CharField(max_length=3, verbose_name='Шаги в Ближний бой', default='0')
    add_ballisticSkill = models.CharField(max_length=3, verbose_name='Шаги в Дальний бой', default='0')
    add_strength = models.CharField(max_length=3, verbose_name='Шаги в Сила', default='0')
    add_toughness = models.CharField(max_length=3, verbose_name='Шаги в Выносливость', default='0')
    add_initiative = models.CharField(max_length=3, verbose_name='Шаги в Инициатива', default='0')
    add_agility = models.CharField(max_length=3, verbose_name='Шаги в Проворство', default='0')
    add_dexterity = models.CharField(max_length=3, verbose_name='Шаги в Ловкость', default='0')
    add_intelligence = models.CharField(max_length=3, verbose_name='Шаги в Интеллект', default='0')
    add_willpower = models.CharField(max_length=3, verbose_name='Шаги в Сила воли', default='0')
    add_fellowship = models.CharField(max_length=3, verbose_name='Шаги в Харизма', default='0')

    other_skills = models.OneToOneField(ListOtherSkills, on_delete=models.SET_NULL, blank=True, null=True,
                                        verbose_name='Лист общих навыков')
    pro_skills = models.OneToOneField(ListProSkills, on_delete=models.SET_NULL, blank=True, null=True,
                                      verbose_name='Лист профессиональных навыков')
    talents = models.ManyToManyField(Talent, verbose_name='Таланты', blank=True)

    penny = models.CharField(max_length=10, verbose_name='Количество пенни', blank=True, null=True)

    psy = models.ManyToManyField(Psychology, verbose_name='Психика', blank=True)

    corruption = models.CharField(max_length=10, verbose_name='Пункты скверны', blank=True, null=True)
    mutation = models.ManyToManyField(Mutation, verbose_name='Психика', blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'


class Party(models.Model):
    # Модель описывает команду (сообщество) персонажей
    name_party = models.CharField(max_length=50, verbose_name='Название команды', blank=True, null=True)
    short_ambition = models.CharField(max_length=100, verbose_name='Краткосрочная амбиция', blank=True, null=True)
    long_ambition = models.CharField(max_length=100, verbose_name='Долгосрочная амбиция', blank=True, null=True)
    members = models.ManyToManyField(Character, verbose_name='Список участников', blank=True)
    description = models.TextField(verbose_name='Расширенное описание группы', blank=True)

    def __str__(self):
        return self.name_party

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'
