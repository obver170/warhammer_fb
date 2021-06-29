import datetime

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
    # 'name': 'имя проверки'
    # 'date': 'дата и время проведения проверки'
    # 'participants': 'список, состоящий из объектов Answer(), других участников проверки'
    # }

    CODE_TYPE_CHECK = (
        'SIMPLE', 'EXTENDED', 'LONG', 'COUNTER', 'LONG_COUNTER'
    )

    def __init__(self, type_check):
        self.type_check = type_check
        self.verification = self.__checkType(self.type_check)

        self.__code = None
        self.__desc_code = None
        self.__name = None
        self.__date = datetime.datetime.today().strftime("%d.%m.%Y:%H.%M")
        self.__dice = None
        self.__proof = None
        self.__modifier = None
        self.__lvl_hit = None
        self.__rounds = None
        self.__success = None
        self.__participants = []


    def __repr__(self):
        repr = ''
        if self.__name:
            repr += f'Имя: {self.__name}. '
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
        if self.__date:
            repr += f'дата и время: {self.__date}, '

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

    @property
    def prof(self):
        return self.__proof

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


    def setName(self, vol):
        # Сохранить имя проверки
        self.__name = vol

    @property
    def name(self):
        return self.__name

    @property
    def date(self):
        return self.__date

    def addParticipants(self, answer):
        # Сохранить в ответе результат участника проверки
        self.__participants.append(answer)

    @property
    def participants(self):
        return self.__participants


    def getAnswer(self):
        # Сформировать и получить ответ
        context = {
            'code_type': self.type_check,
            'code': self.__code,
            'desc_code': self.__desc_code,
            'dice': self.__dice,
            'proof': self.__proof,
            'modifier': self.__modifier,
            'lvl_hit': self.__lvl_hit,
            'list_hits': self.__rounds,

        }
        return context


# a = Answer('SIMPLE')
# print(a.getAnswer())
# print(a.date)

