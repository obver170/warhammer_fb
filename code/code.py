import random


class Dice:
    # Класс для броска кубиков
    def __init__(self):
        pass

    def throwDice(self, type=100):
        # Одиночный бросок по умолчанию d100
        dice = random.randint(1, type)
        return dice

    def throwDices100(self, number=2):
        # Несколько бросков d100, по умолчанию 2
        res = []
        for i in range(0, number):
            dice = self.throwDice(100)
            res.append(dice)
        return res

    def throwDices10(self, number=2):
        # Несколько бросков d10, по умолчанию 2
        res = []
        for i in range(0, number):
            dice = self.throwDice(10)
            res.append(dice)
        return res


class Check:
    # Класс для проверок

    def __init__(self):
        # Критический провал
        self.__critical_fail = 96
        # Критическая удача
        self.__critical_luck = 0
        # Количество текущих успехов
        self.lvl_hit = 0
        # Текущие результаты продолжительной проверки
        self.hits_long_check = []

    CODE_DICE = {
        '1000': 'Гарантированная удача',
        '1001': 'Успех',
        '1002': 'Условный успех',
        '1003': 'Впечатляющий успех',
        '1004': 'Невероятный успех',
        '-1000': 'Гарантированный провал',
        '-1001': 'Провал',
        '-1002': 'Условный провал',
        '-1003': 'Серьезный провал',
        '-1004': 'Ужасающий провал',
    }

    CODE_COMPLEXITY = {
        'Элементарная': 60,
        'Легкая': 40,
        'Заурядная': 20,
        'Серьезная': 0,
        'Трудная': -10,
        'Тяжелая': -20,
        'Безумная': -30,
    }

    @property
    def critical_fail(self):
        return self.__critical_fail

    @critical_fail.setter
    def critical_fail(self, vol):
        self.__critical_fail = vol

    @property
    def critical_luck(self):
        return self.__critical_luck

    @critical_luck.setter
    def critical_luck(self, vol):
        self.__critical_luck = vol

    def __checkGuarantFail(self, dice):
        # Служебный метод, проверка на гарантированную неудачу
        if dice >= self.__critical_fail:
            return '-1000'

    def __checkGuarantLuck(self, dice):
        # Служебный метод, проверка на гарантированную удачу
        if dice <= self.__critical_luck:
            return '1000'

    def checkGuaranteed(self, dice):
        self.dice = dice
        # Метод проверяет попадает ли бросок в гарантированный диапазон удачи и неудачи
        is_fail = self.__checkGuarantFail(dice)
        if is_fail:
            print(f'гарантированная неудача {dice}')
            return is_fail
        is_luck = self.__checkGuarantLuck(dice)
        if is_luck:
            print(f'гарантированная удача {dice}')
            return is_luck

    def simpleCheck(self, skill, dice, modifer=0):
        # Простая проверка. Сначала указывается показатель навыка, затем бросок кубика
        # Возвращает разницу между проверяемым навыком и броском кубика
        # Положительный результат обозначает успех, отрицательный провал
        is_guaranteed = self.checkGuaranteed(dice)
        if is_guaranteed:
            return is_guaranteed
        print(f'Бросок кубика {dice} против {skill}')
        if skill + modifer - dice >= 0:
            return '1001'
        else:
            return '-1001'

    def setLvlHit(self, skill, dice, modifer=0):
        # Определяет количество успехов в текущей проверке
        self.lvl_hit = (skill+modifer) // 10 - dice // 10

    def setHitsLongCheck(self, hits):
        # Сохраняет текущую длительную проверку
        self.hits_long_check = hits

    def extendedCheck(self, skill, dice, modifer=0):
        # Расширенная проверка, без проверки на гарантированные исходы.
        # 0 успехов, считаются 1 успехом
        self.setLvlHit(skill, dice, modifer)
        if self.lvl_hit < 0:
            if self.lvl_hit <= -6:
                return '-1004'
            elif self.lvl_hit <= -4:
                return '-1003'
            elif self.lvl_hit <= -2:
                return '-1001'
            else:
                return '-1002'
        if self.lvl_hit >= 0:
            if self.lvl_hit >= 6:
                return '1004'
            elif self.lvl_hit >= 4:
                return '1003'
            elif self.lvl_hit >= 2:
                return '1001'
            else:
                return '1002'

        print(f'успех = {self.lvl_hit}')
        return self.lvl_hit

    def longCheck(self, skill, dices, rounds, success=0, modifer=0):
        #  Метод для проведения длительной проверки.
        #  Для успешного выполнения необходимо набрать определенное количество успехов за ограниченное время раундов
        #  rounds - количество раундов отведенное на проверку
        # success - необходимое количество успехов, для выполнения действия
        i = 0
        hits = []
        for round in range(1, rounds+1):
            dice = dices[i]
            check = self.extendedCheck(skill, dice, modifer)
            i += 1
            hits.append(self.lvl_hit)
            success = success - self.lvl_hit
            if success <= 0:
                self.setHitsLongCheck(hits)
                return '1001'
        self.setHitsLongCheck(hits)
        return '-1001'


dice = Dice()

print(dice.throwDice())
dices = dice.throwDices100(5)

check = Check()
check.critical_fail = 96
d100 = dice.throwDice()

print(check.simpleCheck(54, d100, 20))
print(check.extendedCheck(54, d100, 20), 'Количество успехов ', check.lvl_hit)
print(dices)

print(check.longCheck(skill=60, dices=dices, rounds=5, success=10))
print(check.hits_long_check)

