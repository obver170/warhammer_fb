from warhammer_fb.code.answer import Answer
from warhammer_fb.code.dice import Dice


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

    def simpleCheck(self, proof, dice, modifier=0):
        # Простая проверка. Сначала указывается показатель навыка, затем бросок кубика
        # Возвращает разницу между проверяемым навыком и броском кубика
        # Положительный результат обозначает успех, отрицательный провал
        is_guaranteed = self.checkGuaranteed(dice)
        if is_guaranteed:
            return is_guaranteed
        print(f'Бросок кубика {dice} против {proof}')
        if proof + modifier - dice >= 0:
            return '1001'
        else:
            return '-1001'

    def setLvlHit(self, proof, dice, modifier=0):
        # Определяет количество успехов в текущей проверке
        self.lvl_hit = (proof+modifier) // 10 - dice // 10

    def setHitsLongCheck(self, hits):
        # Сохраняет текущую длительную проверку
        self.hits_long_check = hits

    def extendedCheck(self, proof, dice, modifier=0):
        # Расширенная проверка, без проверки на гарантированные исходы.
        # 0 успехов, считаются условным успехом
        self.setLvlHit(proof, dice, modifier)
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

    def longCheck(self, proof, dices, rounds, success=0, modifier=0):
        #  Метод для проведения длительной проверки.
        #  Для успешного выполнения необходимо набрать определенное количество успехов за ограниченное время раундов
        #  rounds - количество раундов отведенное на проверку
        # success - необходимое количество успехов, для выполнения действия
        i = 0
        hits = []
        for round in range(1, rounds+1):
            dice = dices[i]
            check = self.extendedCheck(proof, dice, modifier)
            i += 1
            hits.append(self.lvl_hit)
            success = success - self.lvl_hit
            if success <= 0:
                self.setHitsLongCheck(hits)
                return '1001'
        self.setHitsLongCheck(hits)
        return '-1001'


    def counterCheck(self, proof_one, dice_one, proof_two, dice_two, modifier_one=0, modifier_two=0):
        # Метод для проведения встречной проверки
        check_one = self.extendedCheck(proof_one, dice_one, modifier_one)
        hit_one = self.lvl_hit
        check_two = self.extendedCheck(proof_two, dice_two, modifier_two)
        hit_two = self.lvl_hit
        print(f'Первый - {check_one} бросок - {dice_one} проверка - {proof_one} уровень успеха - {hit_one}')
        print(f'Второй - {check_two} бросок - {dice_two} проверка - {proof_two} уровень успеха - {hit_two}')






dice = Dice()

print(dice.throwDice())
dices = dice.throwDices100(5)

check = Check()
check.critical_fail = 96
d100 = dice.throwDice()

print(check.simpleCheck(54, d100, 20))
print(check.extendedCheck(54, d100, 20), 'Количество успехов ', check.lvl_hit)
print(dices)

print(check.longCheck(proof=60, dices=dices, rounds=5, success=10))
print(check.hits_long_check)


check.counterCheck(50, dice.throwDice(), 50, dice.throwDice())

answ = Answer('SIMPLE')