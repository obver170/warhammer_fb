
class ListNamesAttr:
    list_names = ['Ближний бой', 'Дальний бой', 'Сила', 'Выносливость', 'Инициатива', 'Проворство', 'Ловкость',
                  'Интеллект', 'Сила воли', 'Харизма']

    def get_choice_names(self):
        # вернуть список из имен (для использования в моделях choice=)
        return ((x, x) for x in self.list_names)
