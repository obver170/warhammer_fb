import random


class Dice:
    # Класс для получения результата или результатов броска кубика
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

    def isDouble(self, dice):
        # Проверка на то, является ли бросок дублем
        tens = dice // 10
        if tens != 0:
            unit = dice - tens * 10
            if tens == unit:
                return True
        return False

    def isEvenDouble(self, dice):
        # Проверка является бросок четным дублем
        if self.isDouble(dice):
            if dice % 2 == 0:
                return True
        return False



