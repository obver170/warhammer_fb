from django.db import models


# Create your models here.
# Список от 0 до 100
STEPS = [(str(x), str(x)) for x in range(101)]



class BaseSkill(models.Model):
    # Базовый класс
    name_skill: str = 'Не указан'
    type_skill: str = 'Общий'
    base_attribute: str = 'Не указан'
    description: str = 'Нет описания'

    steps = models.CharField(max_length=3, verbose_name='Шаги развития', choices=STEPS, default='0')

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
    base_attribute = 'Интеллект'
    name_skill = 'Дрессировка'
    type_skill = 'Профессиональный'

    specialization = (
        ('Голуби', 'Голуби'),
        ('Демигрифы', 'Демигрифы'),
        ('Лошади', 'Лошади'),
        ('Пегасы', 'Пегасы'),
        ('Собаки', 'Собаки'),
    )
    special = models.CharField(max_length=25, verbose_name='Специализация', choices=specialization, default=0)

    class Meta:
        verbose_name = 'Дрессировка'
        verbose_name_plural = 'Дрессировка'


class Knowledge(BaseSkill):
    base_attribute = 'Интеллект'
    name_skill = 'Знания'
    type_skill = 'Профессиональный'

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

    class Meta:
        verbose_name = 'Знания'
        verbose_name_plural = 'Знания'


class BookSearches(BaseSkill):
    base_attribute = 'Интеллект'
    name_skill = 'Книжные изыскания'
    type_skill = 'Профессиональный'

    class Meta:
        verbose_name = 'Книжные изыскания'
        verbose_name_plural = 'Книжные изыскания'


class Treatment(BaseSkill):
    base_attribute = 'Интеллект'
    name_skill = 'Лечение'
    type_skill = 'Профессиональный'

    class Meta:
        verbose_name = 'Лечение'
        verbose_name_plural = 'Лечение'


class Veterinarian(BaseSkill):
    base_attribute = 'Интеллект'
    name_skill = 'Обращение с животными'
    type_skill = 'Профессиональный'

    class Meta:
        verbose_name = 'Обращение с животными'
        verbose_name_plural = 'Обращение с животными'


class Grade(BaseSkill):
    base_attribute = 'Интеллект'
    name_skill = 'Оценка'
    type_skill = 'Профессиональный'

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценка'


class SecretSigns(BaseSkill):
    specialization = (
        ('Бродяги', 'Бродяги'),
        ('Воры', 'Воры'),
        ('Охотники', 'Охотники'),
        ('Разведчики', 'Разведчики'),
        ('Серый орден', 'Серый орден'),
        ('Гильдия', 'Гильдия'),
    )

    special = models.CharField(max_length=25, verbose_name='Специализация', choices=specialization, default=0)

    base_attribute = 'Интеллект'
    name_skill = 'Тайные знаки'
    type_skill = 'Профессиональный'

    class Meta:
        verbose_name = 'Тайные знаки'
        verbose_name_plural = 'Тайные знаки'


class Language(BaseSkill):
    specialization = (
        ('Боевой арго', 'Боевой арго'),
        ('Бретонский', 'Бретонский'),
        ('Воровской арго', 'Воровской арго'),
        ('Гильдейский арго', 'Гильдейский арго'),
        ('Классический', 'Классический'),
        ('Кхазалид', 'Кхазалид'),
        ('Магический', 'Магический'),
        ('Тилейский', 'Тилейский'),
    )

    special = models.CharField(max_length=25, verbose_name='Специализация', choices=specialization, default=0)

    base_attribute = 'Интеллект'
    name_skill = 'Язык'
    type_skill = 'Профессиональный'

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Язык'


class Entertain(BaseSkill):
    name_skill = 'Артистизм'
    base_attribute = 'Харизма'

    specialization = (
        ('Актерство', 'Актерство'),
        ('Комедия', 'Комедия'),
        ('Пение', 'Пение'),
        ('Сказительство', 'Сказительство'),
    )

    special = models.CharField(max_length=25, verbose_name='Специализация', choices=specialization, default=0)

    class Meta:
        verbose_name = 'Артистизм'
        verbose_name_plural = 'Артистизм'


class Leadership(BaseSkill):
    name_skill = 'Лидерство'
    base_attribute = 'Харизма'

    class Meta:
        verbose_name = 'Лидерство'
        verbose_name_plural = 'Лидерство'


class Charm(BaseSkill):
    name_skill = 'Обаяние'
    base_attribute = 'Харизма'

    class Meta:
        verbose_name = 'Обаяние'
        verbose_name_plural = 'Обаяние'


class Bribery(BaseSkill):
    name_skill = 'Подкуп'
    base_attribute = 'Харизма'

    class Meta:
        verbose_name = 'Подкуп'
        verbose_name_plural = 'Подкуп'


class Gossip(BaseSkill):
    name_skill = 'Сплетничество'
    base_attribute = 'Харизма'

    class Meta:
        verbose_name = 'Сплетничество'
        verbose_name_plural = 'Сплетничество'


class Haggle(BaseSkill):
    name_skill = 'Торговля'
    base_attribute = 'Харизма'

    class Meta:
        verbose_name = 'Торговля'
        verbose_name_plural = 'Торговля'


class Prayer(BaseSkill):
    name_skill = 'Молитвословие'
    base_attribute = 'Харизма'
    type_skill = 'Профессиональный'

    class Meta:
        verbose_name = 'Молитвословие'
        verbose_name_plural = 'Молитвословие'


class OtherSkillList(models.Model):
    name_list = models.CharField(max_length=20, verbose_name='Название набора', default='Общие навыки')

    gamble = models.ForeignKey(Gamble, on_delete=models.CASCADE, verbose_name=Gamble.name_skill)
    outdoorSurvival = models.ForeignKey(OutdoorSurvival, on_delete=models.CASCADE,
                                        verbose_name=OutdoorSurvival.name_skill, null=True)
    entertain = models.ForeignKey(Entertain, on_delete=models.CASCADE, verbose_name=Entertain.name_skill, null=True)
    leadership = models.ForeignKey(Leadership, on_delete=models.CASCADE, verbose_name=Leadership.name_skill, null=True)
    charm = models.ForeignKey(Charm, on_delete=models.CASCADE, verbose_name=Charm.name_skill, null=True)
    bribery = models.ForeignKey(Bribery, on_delete=models.CASCADE, verbose_name=Bribery.name_skill, null=True)
    gossip = models.ForeignKey(Gossip, on_delete=models.CASCADE, verbose_name=Gossip.name_skill, null=True)
    haggle = models.ForeignKey(Haggle, on_delete=models.CASCADE, verbose_name=Haggle.name_skill, null=True)

    def __str__(self):
        return self.name_list

    class Meta:
        verbose_name = 'Набор общих навыков'
        verbose_name_plural = 'Наборы общих навыков'


class ProfessionalSkillList(models.Model):
    name_list = models.CharField(max_length=20, verbose_name='Название набора', default='Профессиональные навыки')

    trainingOfAnimals = models.ForeignKey(TrainingOfAnimals, on_delete=models.CASCADE,
                                          verbose_name=TrainingOfAnimals.name_skill, null=True, blank=True)
    veterinarian = models.ForeignKey(Veterinarian, on_delete=models.CASCADE, verbose_name=Veterinarian.name_skill,
                                     null=True, blank=True)
    knowledge = models.ForeignKey(Knowledge, on_delete=models.CASCADE, verbose_name=Knowledge.name_skill,
                                  null=True, blank=True)
    bookSearches = models.ForeignKey(BookSearches, on_delete=models.CASCADE, verbose_name=BookSearches.name_skill,
                                     null=True, blank=True)
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE, verbose_name=Treatment.name_skill,
                                  null=True, blank=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, verbose_name=Grade.name_skill,
                              null=True, blank=True)
    secretSigns = models.ForeignKey(SecretSigns, on_delete=models.CASCADE, verbose_name=SecretSigns.name_skill,
                                    null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name=Language.name_skill,
                                 null=True, blank=True)
    prayer = models.ForeignKey(Prayer, on_delete=models.CASCADE, verbose_name=Prayer.name_skill,
                               null=True, blank=True)

    def __str__(self):
        return self.name_list

    class Meta:
        verbose_name = 'Набор профессиональных навыков'
        verbose_name_plural = 'Наборы профессиональных навыков'
