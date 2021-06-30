from warhammer_fb.code.check import Check
from warhammer_fb.code.dice import Dice
from dataclasses import dataclass, field


# Минимальными действиями в битве являются Атака в ближнего боя и Атака дальнего боя
# Очередность ходов в бою определяется показателем инициативы
# Бой это Зацикленная очередность действий:
# 1) Определение игроков застигнутых врасплох. Все застигнутые не ходят в текущем раунде.
# 2) Начало раунда. Время событий происходящих в начале раунда
# 3) Ходы игроков (перемещение и действие) в зависимости от инициативы
# 4) Конец раунда. Время событий происходящих в конце раунда.

# Атаки ближнего боя бывают:
# Обычная атака ББ
# Атака с разгона



# Подумать нужен ли
@dataclass
class DataCombat:
    # Попал или нет
    isHit: bool
    # Значение кубика
    dice: int
    # Количество успехов
    lvl_hit: int






class Combat:

    def __init__(self):
        pass

    # def checkingTheHitWeapon(self, weapon_skill, dice,weapon_skill_e, dice_e,
    #                          modifer=0, name='Hero', modifer_e=0, name_e='Hero',):
    #     check = Check()
    #     answer_hero = check.extendedCheck(proof=weapon_skill, dice=dice, modifer=modifer, name=name)
    #     pass

    def isHit(self, answer_attack, answer_defense):
        # Проверяет попал ли атакующий в ближнем бою по цели, возвращает количество успехов
        # Принимает два объекта Answer, сгенерированный check.extendedCheck()
        # answer_attack - расширенная проверка для атакующего
        # answer_defense - расширенная проверка для защищающегося

        return answer_attack.lvl_hit[0] - answer_defense.lvl_hit[0]


# Инициатива
# Атака ближнего боя
# Атака дальнего боя


check = Check()
dice = Dice()

print(dice.isDouble(99))
print(dice.isEvenDouble(1))

d100 = dice.throwDice()
print(d100)
attack = check.extendedCheck(75, d100, name='Тигр')

d100 = dice.throwDice()
print(d100)
defender = check.extendedCheck(60, d100, name='Ягуар')

combat = Combat()
isHit = combat.isHit(answer_attack=attack, answer_defense=defender)
print(isHit)