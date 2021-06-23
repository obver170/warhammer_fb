class Answer:
    # Класс для формирования ответа на проведенную проверку

    # Вид ответа
    # {'code_type': 'тип проверки',
    # 'code': 'код успешности проверки',
    # 'desc_code': 'расшифровка кода успешности',
    # 'dice': 'результат кубика или кубиков []'
    # 'proof': 'порог проверки',
    # 'modifier': 'модификатор проверки',
    # 'lvl_hit': 'уровень успеха []',
    # 'rounds': 'длительность проверки'
    #
    # 'code_enemy': 'код успешности проверки противника',
    # 'desc_code_enemy': 'расшифровка кода успешности противника',
    # 'dice_enemy': 'результат кубика или кубиков противника []'
    # 'proof_enemy': 'порог проверки противника'
    # 'modifier_enemy': 'модификатор проверки противника',
    # 'lvl_hit_enemy': 'уровень успеха противника []',
    # 'rounds_enemy': 'длительность проверки противника'
    # }

    CODE_TYPE_CHECK = (
        'SIMPLE', 'EXTENDED', 'LONG', 'COUNTER'
    )

    def __init__(self, type_check):
        self.code_type = type_check
        self.verification = self.__checkType(self.code_type)

        self.__code = None
        self.__desc_code = None
        self.__dice = None
        self.__proof = None
        self.__modifier = None
        self.__lvl_hit = None
        self.__rounds = None
        self.__success = None

        self.__code_enemy = None
        self.__desc_code_enemy = None
        self.__dice_enemy = None
        self.__proof_enemy = None
        self.__modifier_enemy = None
        self.__lvl_hit_enemy = None
        self.__rounds_enemy = None
        self.__success_enemy = None

    def __repr__(self):
        repr = ''
        if self.__code:
            repr += f'Код проверки: {self.__code}. '
        if self.__dice:
            repr += f'Значения кубиков: {self.__dice}, '
        if self.__proof:
            repr += f'порог проверки: {self.__proof}, '
        if self.__modifier:
            repr += f'участвующие модификаторы: {self.__modifier}, '
        if self.__lvl_hit:
            repr += f'уровень успехов: {self.__lvl_hit}, '
        if self.__rounds:
            repr += f'продолжительность проверки: {self.__rounds}, '
        if self.__success:
            repr += f'необходимое количество успехов: {self.__success}, '

        if self.__code_enemy:
            repr += f'Код проверки: {self.__code_enemy}. '
        if self.__dice_enemy:
            repr += f'Значения кубиков: {self.__dice_enemy}, '
        if self.__proof_enemy:
            repr += f'порог проверки: {self.__proof_enemy}, '
        if self.__modifier_enemy:
            repr += f'участвующие модификаторы: {self.__modifier_enemy}, '
        if self.__lvl_hit_enemy:
            repr += f'уровень успехов: {self.__lvl_hit_enemy}, '
        if self.__rounds_enemy:
            repr += f'продолжительность проверки: {self.__rounds_enemy}, '
        if self.__success_enemy:
            repr += f'необходимое количество успехов противника: {self.__success_enemy}, '
        return repr

    def __checkType(self, type_check):
        # Проверка, поддерживается ли возможность ответа на тип запрашиваемого вопроса
        if type_check.upper() in self.CODE_TYPE_CHECK:
            return True
        else:
            return False

    def setCode(self, vol):
        # Сохранить код успешности проверки
        self.__code = vol

    def setDescCode(self, vol):
        # Сохранить расшифровку кода успешности проверки
        self.__desc_code = vol

    def setDice(self, dice):
        # Сохранить значение выпавшее на кубах
        # Результат хранится в массиве
        dices = []
        if isinstance(dice, list):
            dices = dice
        else:
            dices.append(dice)
        self.__dice = dices

    @property
    def dice(self):
        return self.__dice

    def setProof(self, vol):
        # Сохранить значение проходимой проверки
        self.__proof = vol

    def setModifier(self, vol):
        # Сохранить значение модификаторов проверки
        self.__modifier = vol

    def setLvlHit(self, hit):
        # Сохранить количество успехов
        # Результат хранится в массиве
        hits = []
        if isinstance(hit, list):
            hits = hit
        else:
            hits.append(hit)
        self.__lvl_hit = hits

    @property
    def lvl_hit(self):
        return self.__lvl_hit

    def setRounds(self, vol):
        # Сохранить длительность проверки
        self.__rounds = vol

    def setSuccess(self, vol):
        # Сохранить необходимое количество успехов
        self.__success = vol



    def setCodeEnemy(self, vol):
        # Сохранить код успешности проверки противника
        self.__code_enemy = vol

    def setDescCodeEnemy(self, vol):
        # Сохранить расшифровку кода успешности проверки
        self.__desc_code_enemy = vol

    def setDiceEnemy(self, dice_enemy):
        # Сохранить значение выпавшее на кубах
        # Результат хранится в массиве
        dices = []
        if isinstance(dice_enemy, list):
            dices = dice_enemy
        else:
            dices.append(dice_enemy)
        self.__dice_enemy = dices

    @property
    def dice_enemy(self):
        return self.__dice_enemy

    def setProofEnemy(self, vol):
        # Сохранить значение проходимой проверки
        self.__proof_enemy = vol

    def setModifierEnemy(self, vol):
        # Сохранить значение модификаторов проверки
        self.__modifier_enemy = vol

    def setLvlHitEnemy(self, hit_enemy):
        # Сохранить количество успехов
        # Результат хранится в массиве
        hits = []
        if isinstance(hit_enemy, list):
            hits = hit_enemy
        else:
            hits.append(hit_enemy)
        self.__lvl_hit_enemy = hits

    @property
    def lvl_hit_enemy(self):
        return self.__lvl_hit_enemy

    def setRoundsEnemy(self, vol):
        # Сохранить длительность проверки противника
        self.__rounds_enemy = vol

    def setSuccessEnemy(self, vol):
        # Сохранить необходимое количество успехов противника
        self.__success_enemy = vol

    def getAnswer(self):
        # Сформировать и получить ответ
        context = {
            'code_type': self.code_type,
            'code': self.__code,
            'desc_code': self.__desc_code,
            'dice': self.__dice,
            'proof': self.__proof,
            'modifier': self.__modifier,
            'lvl_hit': self.__lvl_hit,
            'list_hits': self.__rounds,
            'code_enemy': self.__code_enemy,
            'desc_code_enemy': self.__desc_code_enemy,
            'dice_enemy': self.__dice_enemy,
            'proof_enemy': self.__proof_enemy,
            'modifier_enemy': self.__modifier_enemy,
            'lvl_hit_enemy': self.__lvl_hit_enemy,
            'list_hits_enemy': self.__rounds_enemy,
        }
        return context


a = Answer('SIMPLE')
print(a.getAnswer())


a = ['r', 'r']
a1 = 'a'

print(type(a))
print(type(a1))