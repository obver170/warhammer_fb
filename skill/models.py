from django.db import models


# Create your models here.
class BaseSkill(models.Model):
    # Базовый класс
    name_skill: str = 'Не указан'
    type_skill: str = 'Общий'
    base_attribute: str = 'Не указан'
    description: str = 'Нет описания'
    isActive = models.BooleanField(verbose_name='Активен?', default=False)

    steps = models.CharField(max_length=3, verbose_name='Шаги развития', default='0')

    def __str__(self):
        return self.steps


class Gamble(BaseSkill):
    base_attribute = 'Интеллект'
    name_skill = 'Азартные игры'

    class Meta:
        verbose_name = 'Азартные игры'
        verbose_name_plural = 'Азартные игры'


class OutdoorSurvival(BaseSkill):
    base_attribute = 'Интеллект'
    name_skill = 'Выживание'

    class Meta:
        verbose_name = 'Выживание'
        verbose_name_plural = 'Выживание'


class TrainingOfAnimals(BaseSkill):
    specialization = (
        ('Голуби', 'Голуби'),
        ('Демигрифы', 'Демигрифы'),
        ('Лошади', 'Лошади'),
        ('Пегасы', 'Пегасы'),
        ('Собаки', 'Собаки'),
    )
    special = models.CharField(max_length=25, verbose_name='Специализация', choices=specialization, default=0)

    base_attribute = 'Интеллект'
    name_skill = 'Дрессировка'
    type_skill = 'Профессиональный'

    class Meta:
        verbose_name = 'Дрессировка'
        verbose_name_plural = 'Дрессировка'


class Knowledge(BaseSkill):
    specialization = (
        ('Геология', 'Геология'),
        ('Геральдика', 'Геральдика'),
        ('Закон', 'Закон'),
        ('Инженерное дело', 'Инженерное дело'),
        ('История', 'История'),
        ('Магия', 'Магия'),
        ('Металлургия', 'Металлургия'),
        ('Наука', 'Наука'),
        ('Теология', 'Теология'),
    )

    special = models.CharField(max_length=25, verbose_name='Специализация', choices=specialization, default=0)

    base_attribute = 'Интеллект'
    name_skill = 'Знания'
    type_skill = 'Профессиональный'

    class Meta:
        verbose_name = 'Знания'
        verbose_name_plural = 'Знания'


class BookSearches (BaseSkill):
    base_attribute = 'Интеллект'
    name_skill = 'Книжные изыскания'
    type_skill = 'Профессиональный'

    class Meta:
        verbose_name = 'Книжные изыскания'
        verbose_name_plural = 'Книжные изыскания'


class Treatment (BaseSkill):
    base_attribute = 'Интеллект'
    name_skill = 'Лечение'
    type_skill = 'Профессиональный'

    class Meta:
        verbose_name = 'Лечение'
        verbose_name_plural = 'Лечение'


class Veterinarian (BaseSkill):
    base_attribute = 'Интеллект'
    name_skill = 'Обращение с животными'
    type_skill = 'Профессиональный'

    class Meta:
        verbose_name = 'Обращение с животными'
        verbose_name_plural = 'Обращение с животными'


class SkillList(models.Model):
    name_list = models.CharField(max_length=20, verbose_name='Название набора', default='Стандарт')
    gamble = models.ForeignKey(Gamble, on_delete=models.CASCADE, verbose_name=Gamble.name_skill)
    outdoorSurvival = models.ForeignKey(OutdoorSurvival, on_delete=models.CASCADE,
                                        verbose_name=OutdoorSurvival.name_skill, null=True)
    trainingOfAnimals = models.ForeignKey(TrainingOfAnimals, on_delete=models.CASCADE,
                                          verbose_name=TrainingOfAnimals.name_skill, null=True, blank=True)
    knowledge = models.ForeignKey(Knowledge, on_delete=models.CASCADE, verbose_name=Knowledge.name_skill,
                                  null=True, blank=True)
    bookSearches = models.ForeignKey(BookSearches, on_delete=models.CASCADE, verbose_name=BookSearches.name_skill,
                                       null=True, blank=True)
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE, verbose_name=Treatment.name_skill,
                                       null=True, blank=True)
    veterinarian = models.ForeignKey(Veterinarian, on_delete=models.CASCADE, verbose_name=Veterinarian.name_skill,
                                       null=True, blank=True)

    def __str__(self):
        return self.name_list

    class Meta:
        verbose_name = 'Набор навыков'
        verbose_name_plural = 'Наборы навыков'
