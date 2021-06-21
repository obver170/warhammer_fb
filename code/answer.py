class Answer:
    # Класс для формирования ответа на проведенную проверку

    # Вид ответа
    # {'code_type': 'тип проверки',
    # 'code': 'код успешности проверки',
    # 'desc_code': 'расшифровка кода успешности',
    # 'dice': 'результат кубика или кубиков'
    # 'proof': 'порог проверки',
    # 'modifier': 'модификатор проверки',
    # 'lvl_hit': 'уровень успеха',
    # 'list_hits': 'список успехов при длительной проверке'
    #
    # 'code_enemy': 'код успешности проверки противника',
    # 'desc_code_enemy': 'расшифровка кода успешности противника',
    # 'dice_enemy': 'результат кубика или кубиков противника'
    # 'proof_enemy': 'порог проверки противника'
    # 'modifier_enemy': 'модификатор проверки противника',
    # 'lvl_hit_enemy': 'уровень успеха противника',
    # 'list_hits_enemy': 'список успехов при длительной проверке противника'
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
        self.__list_hits = None
        self.__code_enemy = None
        self.__desc_code_enemy = None
        self.__dice_enemy = None
        self.__proof_enemy = None
        self.__modifier_enemy = None
        self.__lvl_hit_enemy = None
        self.__list_hits_enemy = None

    def __checkType(self, type_check):
        # Проверка, поддерживается ли возможность ответа на тип запрашиваемого вопроса
        if type_check.upper() in self.CODE_TYPE_CHECK:
            return True
        else:
            return False

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
            'list_hits': self.__list_hits,
            'code_enemy': self.__code_enemy,
            'desc_code_enemy': self.__desc_code_enemy,
            'dice_enemy': self.__dice_enemy,
            'proof_enemy': self.__proof_enemy,
            'modifier_enemy': self.__modifier_enemy,
            'lvl_hit_enemy': self.__lvl_hit_enemy,
            'list_hits_enemy': self.__list_hits_enemy,
        }
        return context

a = Answer('SIMPLE')
print(a.getAnswer())