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

    CODE_DICE = {
        '1100': 'Гарантированная неудача',
        '1000': 'Гарантированная удача'
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
            return 1100

    def __checkGuarantLuck(self, dice):
        # Служебный метод, проверка на гарантированную удачу
        if dice <= self.__critical_luck:
            return 1000

    def checkGuaranteed(self, dice):
        # Метод проверяет попадает ли бросок в гарантированный диапазон удачи и неудачи
        is_fail = self.__checkGuarantFail(dice)
        if is_fail:
            print(f'гарантированная неудача {dice}')
            return is_fail
        is_luck = self.__checkGuarantLuck(dice)
        if is_luck:
            print(f'гарантированная удача {dice}')
            return is_luck

    def simpleCheck(self, skill, dice):
        # Простая проверка. Сначала указывается показатель навыка, затем бросок кубика
        is_guaranteed = self.checkGuaranteed(dice)
        if is_guaranteed:
            return is_guaranteed
        print(f'Бросок кубика {dice} против {skill}')
        return skill-dice



dice = Dice()

print(dice.throwDice())
print(dice.throwDices100(5))
print(dice.throwDices10(5))

check = Check()
check.critical_fail = 96
d100 = dice.throwDice()

print(check.simpleCheck(54, d100))

print(check.critical_luck)
print(check.critical_fail)