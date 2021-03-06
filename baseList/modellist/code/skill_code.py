class NameSkillBase:
    list_names: list = ()

    def get_choice_names(self):
        # вернуть список из имен (для использования в моделях choice=)
        res = []
        for x in self.list_names:
            name = x.get('name')
            spec = x.get('spec')
            if spec == '':
                res.append((name, name))
            else:
                res.append((f'{name} ({spec})', f'{name} ({spec})'))
            temp = tuple(res)

        return temp

    def get_list_names(self):
        # Вернуть все названия навыков
        return [x.get('name') for x in self.list_names]

    def get_attr(self, name):
        # Получить связанную характеристику по названию навыка
        res = ''
        for x in self.list_names:
            if x.get('name').lower() == name.lower():
                res = x.get('attr')
                return res
        return res

    def get_list_by_attr(self, attr):
        # Вернуть список названий навыков по указанной характеристике
        res = []
        for x in self.list_names:
            if x.get('attr').lower() == attr.lower():
                if x.get('spec') == '':
                    res.append(x.get('name'))
                else:
                    res.append(x.get('name') + ' (' + x.get('spec') + ')')
        return res


# Список общих навыков
class NamesOther(NameSkillBase):
    list_names = (
        {'name': 'Азартные игры', 'attr': 'Интеллект', 'spec': ''},
        {'name': 'Атлетика', 'attr': 'Проворство', 'spec': ''},
        {'name': 'Артистизм', 'attr': 'Харизма', 'spec': 'Актерство'},
        {'name': 'Артистизм', 'attr': 'Харизма', 'spec': 'Комедия'},
        {'name': 'Артистизм', 'attr': 'Харизма', 'spec': 'Пение'},
        {'name': 'Артистизм', 'attr': 'Харизма', 'spec': 'Сказительство'},
        {'name': 'Верховая езда', 'attr': 'Проворство', 'spec': 'Гигантские волки'},
        {'name': 'Верховая езда', 'attr': 'Проворство', 'spec': 'Грифоны'},
        {'name': 'Верховая езда', 'attr': 'Проворство', 'spec': 'Демигрифы'},
        {'name': 'Верховая езда', 'attr': 'Проворство', 'spec': 'Лошади'},
        {'name': 'Верховая езда', 'attr': 'Проворство', 'spec': 'Пегасы'},
        {'name': 'Вождение', 'attr': 'Проворство', 'spec': ''},
        {'name': 'Выживание', 'attr': 'Интеллект', 'spec': ''},
        {'name': 'Гребля', 'attr': 'Сила', 'spec': ''},
        {'name': 'Запугивание', 'attr': 'Сила', 'spec': ''},
        {'name': 'Интуиция', 'attr': 'Инициатива', 'spec': ''},
        {'name': 'Искусство', 'attr': 'Ловкость', 'spec': 'Гравюра'},
        {'name': 'Искусство', 'attr': 'Ловкость', 'spec': 'Живопись'},
        {'name': 'Искусство', 'attr': 'Ловкость', 'spec': 'Картография'},
        {'name': 'Искусство', 'attr': 'Ловкость', 'spec': 'Мозаика'},
        {'name': 'Искусство', 'attr': 'Ловкость', 'spec': 'Скульптура'},
        {'name': 'Искусство', 'attr': 'Ловкость', 'spec': 'Татуировка'},
        {'name': 'Искусство', 'attr': 'Ловкость', 'spec': 'Ткачество'},
        {'name': 'Кутеж', 'attr': 'Выносливость', 'spec': ''},
        {'name': 'Лазанье', 'attr': 'Сила', 'spec': ''},
        {'name': 'Лидерство', 'attr': 'Харизма', 'spec': ''},
        {'name': 'Наблюдательность', 'attr': 'Инициатива', 'spec': ''},
        {'name': 'Обаяние', 'attr': 'Харизма', 'spec': ''},
        {'name': 'Ориентирование', 'attr': 'Инициатива', 'spec': ''},
        {'name': 'Подкуп', 'attr': 'Харизма', 'spec': ''},
        {'name': 'Рукопашный бой', 'attr': 'Ближний бой', 'spec': 'Основное'},
        {'name': 'Рукопашный бой', 'attr': 'Ближний бой', 'spec': 'Двуручное'},
        {'name': 'Рукопашный бой', 'attr': 'Ближний бой', 'spec': 'Древковое'},
        {'name': 'Рукопашный бой', 'attr': 'Ближний бой', 'spec': 'Кавалерийское'},
        {'name': 'Рукопашный бой', 'attr': 'Ближний бой', 'spec': 'Кулачное'},
        {'name': 'Рукопашный бой', 'attr': 'Ближний бой', 'spec': 'Парирующее'},
        {'name': 'Рукопашный бой', 'attr': 'Ближний бой', 'spec': 'Фехтовальное'},
        {'name': 'Рукопашный бой', 'attr': 'Ближний бой', 'spec': 'Цепы'},
        {'name': 'Скрытность', 'attr': 'Проворство', 'spec': 'Города'},
        {'name': 'Скрытность', 'attr': 'Проворство', 'spec': 'Дикая природа'},
        {'name': 'Скрытность', 'attr': 'Проворство', 'spec': 'Подземелья'},
        {'name': 'Сплетничество', 'attr': 'Харизма', 'spec': ''},
        {'name': 'Стойкость', 'attr': 'Выносливость', 'spec': ''},
        {'name': 'Торговля', 'attr': 'Харизма', 'spec': ''},
        {'name': 'Уклонение', 'attr': 'Проворство', 'spec': ''},
        {'name': 'Усмирение животных', 'attr': 'Сила воли', 'spec': ''},
        {'name': 'Хладнокровие', 'attr': 'Сила воли', 'spec': ''},
    )


class NamesProfessional(NameSkillBase):
    list_names = (
        {'name': 'Взлом', 'attr': 'Ловкость', 'spec': ''},
        {'name': 'Выслеживание', 'attr': 'Инициатива', 'spec': ''},
        {'name': 'Дрессировка', 'attr': 'Интеллект', 'spec': 'Голуби'},
        {'name': 'Дрессировка', 'attr': 'Интеллект', 'spec': 'Демигрифы'},
        {'name': 'Дрессировка', 'attr': 'Интеллект', 'spec': 'Лошади'},
        {'name': 'Дрессировка', 'attr': 'Интеллект', 'spec': 'Пегасы'},
        {'name': 'Дрессировка', 'attr': 'Интеллект', 'spec': 'Собаки'},
        {'name': 'Знание', 'attr': 'Интеллект', 'spec': 'Геология'},
        {'name': 'Знание', 'attr': 'Интеллект', 'spec': 'Геральдика'},
        {'name': 'Знание', 'attr': 'Интеллект', 'spec': 'Закон'},
        {'name': 'Знание', 'attr': 'Интеллект', 'spec': 'Инженерное дело'},
        {'name': 'Знание', 'attr': 'Интеллект', 'spec': 'История'},
        {'name': 'Знание', 'attr': 'Интеллект', 'spec': 'Магия'},
        {'name': 'Знание', 'attr': 'Интеллект', 'spec': 'Металлургия'},
        {'name': 'Знание', 'attr': 'Интеллект', 'spec': 'Наука'},
        {'name': 'Знание', 'attr': 'Интеллект', 'spec': 'Теология'},
        {'name': 'Книжные изыскания', 'attr': 'Интеллект', 'spec': ''},
        {'name': 'Концентрация', 'attr': 'Сила Воли', 'spec': 'Азир'},
        {'name': 'Концентрация', 'attr': 'Сила Воли', 'spec': 'Акши'},
        {'name': 'Концентрация', 'attr': 'Сила Воли', 'spec': 'Гайран'},
        {'name': 'Концентрация', 'attr': 'Сила Воли', 'spec': 'Гарр'},
        {'name': 'Концентрация', 'attr': 'Сила Воли', 'spec': 'Дхар'},
        {'name': 'Концентрация', 'attr': 'Сила Воли', 'spec': 'Улгу'},
        {'name': 'Концентрация', 'attr': 'Сила Воли', 'spec': 'Шамон'},
        {'name': 'Концентрация', 'attr': 'Сила Воли', 'spec': 'Хиш'},
        {'name': 'Концентрация', 'attr': 'Сила Воли', 'spec': 'Шаиш'},
        {'name': 'Лечение', 'attr': 'Интеллект', 'spec': ''},
        {'name': 'Ловкость рук', 'attr': 'Ловкость', 'spec': ''},
        {'name': 'Молитвословие', 'attr': 'Харизма', 'spec': ''},
        {'name': 'Музицирование', 'attr': 'Ловкость', 'spec': 'Волынка'},
        {'name': 'Музицирование', 'attr': 'Ловкость', 'spec': 'Клавесин'},
        {'name': 'Музицирование', 'attr': 'Ловкость', 'spec': 'Лютня'},
        {'name': 'Музицирование', 'attr': 'Ловкость', 'spec': 'Рожок'},
        {'name': 'Музицирование', 'attr': 'Ловкость', 'spec': 'Скрипка'},
        {'name': 'Обращение с животными', 'attr': 'Интеллект', 'spec': ''},
        {'name': 'Обращение с ловушками', 'attr': 'Ловкость', 'spec': ''},
        {'name': 'Оценка', 'attr': 'Интеллект', 'spec': ''},
        {'name': 'Плавание', 'attr': 'Сила', 'spec': ''},
        {'name': 'Ремесло', 'attr': 'Ловкость', 'spec': 'Аптекарь'},
        {'name': 'Ремесло', 'attr': 'Ловкость', 'spec': 'Бальзамировщик'},
        {'name': 'Ремесло', 'attr': 'Ловкость', 'spec': 'Дубильщик'},
        {'name': 'Ремесло', 'attr': 'Ловкость', 'spec': 'Каллиграф'},
        {'name': 'Ремесло', 'attr': 'Ловкость', 'spec': 'Кузнец'},
        {'name': 'Ремесло', 'attr': 'Ловкость', 'spec': 'Плотник'},
        {'name': 'Ремесло', 'attr': 'Ловкость', 'spec': 'Повар'},
        {'name': 'Ремесло', 'attr': 'Ловкость', 'spec': 'Свечник'},
        {'name': 'Стрельба', 'attr': 'Дальний бой', 'spec': 'Арбалеты'},
        {'name': 'Стрельба', 'attr': 'Дальний бой', 'spec': 'Взрывчатка'},
        {'name': 'Стрельба', 'attr': 'Дальний бой', 'spec': 'Инженерное'},
        {'name': 'Стрельба', 'attr': 'Дальний бой', 'spec': 'Ловчее'},
        {'name': 'Стрельба', 'attr': 'Дальний бой', 'spec': 'Луки'},
        {'name': 'Стрельба', 'attr': 'Дальний бой', 'spec': 'Метательное'},
        {'name': 'Стрельба', 'attr': 'Дальний бой', 'spec': 'Пороховое'},
        {'name': 'Стрельба', 'attr': 'Дальний бой', 'spec': 'Пращи'},
        {'name': 'Сценическое искусство', 'attr': 'Проворство', 'spec': 'Акробатика'},
        {'name': 'Сценическое искусство', 'attr': 'Проворство', 'spec': 'Глотание огня'},
        {'name': 'Сценическое искусство', 'attr': 'Проворство', 'spec': 'Жонглирование'},
        {'name': 'Сценическое искусство', 'attr': 'Проворство', 'spec': 'Клоунада'},
        {'name': 'Сценическое искусство', 'attr': 'Проворство', 'spec': 'Пантомима'},
        {'name': 'Сценическое искусство', 'attr': 'Проворство', 'spec': 'Танец'},
        {'name': 'Сценическое искусство', 'attr': 'Проворство', 'spec': 'Хождение по канату'},
        {'name': 'Тайные знаки', 'attr': 'Интеллект', 'spec': 'Бродяги'},
        {'name': 'Тайные знаки', 'attr': 'Интеллект', 'spec': 'Воры'},
        {'name': 'Тайные знаки', 'attr': 'Интеллект', 'spec': 'Гильдия'},
        {'name': 'Тайные знаки', 'attr': 'Интеллект', 'spec': 'Охотники'},
        {'name': 'Тайные знаки', 'attr': 'Интеллект', 'spec': 'Разведчики'},
        {'name': 'Тайные знаки', 'attr': 'Интеллект', 'spec': 'Серый орден'},
        {'name': 'Хождение под парусом', 'attr': 'Проворство', 'spec': 'Баржи'},
        {'name': 'Хождение под парусом', 'attr': 'Проворство', 'spec': 'Волчьи корабли'},
        {'name': 'Хождение под парусом', 'attr': 'Проворство', 'spec': 'Каравеллы'},
        {'name': 'Хождение под парусом', 'attr': 'Проворство', 'spec': 'Когги'},
        {'name': 'Хождение под парусом', 'attr': 'Проворство', 'spec': 'Лодки'},
        {'name': 'Хождение под парусом', 'attr': 'Проворство', 'spec': 'Фрегаты'},
        {'name': 'Язык', 'attr': 'Интеллект', 'spec': 'Боевой арго'},
        {'name': 'Язык', 'attr': 'Интеллект', 'spec': 'Бретонский'},
        {'name': 'Язык', 'attr': 'Интеллект', 'spec': 'Воровской арго'},
        {'name': 'Язык', 'attr': 'Интеллект', 'spec': 'Гильдейский арго'},
        {'name': 'Язык', 'attr': 'Интеллект', 'spec': 'Классический'},
        {'name': 'Язык', 'attr': 'Интеллект', 'spec': 'Кхазалид'},
        {'name': 'Язык', 'attr': 'Интеллект', 'spec': 'Магический'},
        {'name': 'Язык', 'attr': 'Интеллект', 'spec': 'Тилейский'},
    )


# n = NamesOther()
# print(n.get_choice_names())
