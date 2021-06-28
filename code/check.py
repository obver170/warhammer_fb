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
            print(f'гарантированный провал {dice}')
            return is_fail
        is_luck = self.__checkGuarantLuck(dice)
        if is_luck:
            print(f'гарантированный успех {dice}')
            return is_luck

    def simpleCheck(self, proof, dice, modifier=0, name='Noname'):
        # Простая проверка. Сначала указывается показатель навыка, затем бросок кубика
        # Возвращает разницу между проверяемым навыком и броском кубика
        # Положительный результат обозначает успех, отрицательный провал
        answer = Answer('SIMPLE')
        answer.setDice(dice)
        answer.setProof(proof)
        answer.setModifier(modifier)
        answer.setName(name)
        if self.checkGuaranteed(dice):
            answer.setCode(self.checkGuaranteed(dice))
            return answer
        if proof + modifier - dice >= 0:
            answer.setCode('1001')
        else:
            answer.setCode('-1001')
        return answer


    def setLvlHit(self, proof, dice, modifier=0):
        # Определяет количество успехов в текущей проверке
        return (proof+modifier) // 10 - dice // 10

    # def setHitsLongCheck(self, hits):
    #     # Сохраняет текущую длительную проверку
    #     # скоро удалить
    #     self.hits_long_check = hits

    def extendedCheck(self, proof, dice, modifier=0, set_i=0, name='Nоname'):
        # Расширенная проверка, без проверки на гарантированные исходы.
        # 0 успехов, считаются условным успехом

        answer = self.simpleCheck(proof, dice, modifier, name=name)
        answer.type_check = 'EXTENDED'

        lvl_hit = self.setLvlHit(proof, dice, modifier)
        answer.setLvlHit(lvl_hit)

        # Количество раундов, в течении которых длится проверка.
        # В случае простой расширенной проверки это 1 раунд и берется первый элемент из списка успехов
        # Это необходимо для того чтобы в дальнейшем использовать этот метод при длительной проверке
        # !!!!! Тем не менее это костыль. Думать как реализовать безопаснее. !!!!
        i = set_i

        if answer.lvl_hit[i] < 0:
            if answer.lvl_hit[i] <= -6:
                answer.setCode('-1004')
            elif answer.lvl_hit[i] <= -4:
                answer.setCode('-1003')
            elif answer.lvl_hit[i] <= -2:
                answer.setCode('-1001')
            else:
                answer.setCode('-1002')
        if answer.lvl_hit[i] >= 0:
            if answer.lvl_hit[i] >= 6:
                answer.setCode('1004')
            elif answer.lvl_hit[i] >= 4:
                answer.setCode('1003')
            elif answer.lvl_hit[i] >= 2:
                answer.setCode('1001')
            else:
                answer.setCode('1002')

        return answer


    # def longCheck(self, proof, dices, rounds, success=0, modifier=0):
    #     # Метод для проведения длительной проверки.
    #     # Для успешного выполнения необходимо набрать определенное количество успехов за ограниченное время раундов
    #     # rounds - количество раундов отведенное на проверку
    #     # success - необходимое количество успехов, для выполнения действия
    #     answer = Answer('LONG')
    #     answer.setProof(proof)
    #     answer.setDice(dices)
    #     answer.setRounds(rounds)
    #     answer.setSuccess(success)
    #     answer.setModifier(modifier)
    #
    #
    #     i = 0
    #     hits = []
    #     for round in range(1, rounds+1):
    #         dice = dices[i]
    #         check = self.extendedCheck(proof, dice, modifier)
    #         i += 1
    #         hits.append(self.lvl_hit)
    #         success = success - self.lvl_hit
    #         if success <= 0:
    #             self.setHitsLongCheck(hits)
    #             return '1001'
    #     self.setHitsLongCheck(hits)
    #     return '-1001'

    def longCheck(self, proof, dices, rounds, success=0, modifier=0, name='Noname'):
        # Метод для проведения длительной проверки.
        # Для успешного выполнения необходимо набрать определенное количество успехов за ограниченное время раундов
        # rounds - количество раундов отведенное на проверку
        # success - необходимое количество успехов, для выполнения действия
        answer = Answer('LONG')
        answer.setProof(proof)
        answer.setDice(dices)
        answer.setRounds(rounds)
        answer.setSuccess(success)
        answer.setModifier(modifier)
        answer.setName(name)


        i = 0
        hits = []
        for round in range(1, rounds+1):
            dice = dices[i]
            lvl_hit = self.setLvlHit(proof, dice, modifier)
            hits.append(lvl_hit)

            i += 1

            success = success - lvl_hit
            if success <= 0:
                answer.setCode('1001')
                answer.setLvlHit(hits)
                return answer

        answer.setLvlHit(hits)
        answer.setCode('-1001')
        return answer




    # def counterCheck(self, proof_one, dice_one, proof_two, dice_two, modifier_one=0, modifier_two=0):
    #     # Метод для проведения встречной проверки
    #     check_one = self.extendedCheck(proof_one, dice_one, modifier_one)
    #     hit_one = self.lvl_hit
    #     check_two = self.extendedCheck(proof_two, dice_two, modifier_two)
    #     hit_two = self.lvl_hit
    #     print(f'Первый - {check_one} бросок - {dice_one} проверка - {proof_one} уровень успеха - {hit_one}')
    #     print(f'Второй - {check_two} бросок - {dice_two} проверка - {proof_two} уровень успеха - {hit_two}')


    def counterCheck(self, answers):
        # Метод для мгновенной встречной проверки
        # Принимает массив объектов Answer сформированных методом extendedCheck
        res = None
        min_hit = -1000
        min_skill = -100
        for answer in answers:
            if answer.lvl_hit[0] > min_hit:
                min_hit = answer.lvl_hit[0]
                min_skill = answer.prof
                res = answer
            # Если количество успехов при встречной проверке одинаковое
            # сравнивается показатель навыка, у кого выше - тот и победил
            if answer.lvl_hit[0] == min_hit:
                if answer.prof > min_skill:
                    min_hit = answer.lvl_hit[0]
                    min_skill = answer.prof
                    res = answer

        res.type_check ='COUNTER'
        for answer in answers:
            res.addParticipants(answer)
        return res





print('*'*15)

check = Check()
dice = Dice()
check.critical_fail = 96
d100 = dice.throwDice()

# simple_check = check.simpleCheck(60, d100, -20)
# print(simple_check.code_type)
# print(simple_check)
#
#
d100 = dice.throwDice()
extended_check = check.extendedCheck(60, d100, 10)
print(extended_check.type_check)
print(extended_check)
print(extended_check.lvl_hit[0])
#
#
# dices = dice.throwDices100(10)
# long_check = check.longCheck(60, dices, 10, 6, -10)
# print(long_check.code_type)
# print(long_check)

print('*'*10)
print('Встречная проверка')
proof = 60
mod = 10
answers = []
answers.append(check.extendedCheck(10, dice.throwDice(), mod, name='Тирг'))
answers.append(check.extendedCheck(70, 20, mod, name='Олень'))
answers.append(check.extendedCheck(60, 10, mod, name='Медведь'))

winner = check.counterCheck(answers)
for a in answers:
    print(a)
print('Победитель')
print(winner)

