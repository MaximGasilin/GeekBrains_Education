# Задание #0 "От Ивана" - Лото
#
# == Лото ==
#
# Правила игры в лото.
#
# Игра ведется с помощью специальных карточек, на которых отмечены числа, и фишек (бочонков) с цифрами.
#
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
#
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
#
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
#
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
#
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
#
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
#     Если цифра есть на карточке - она зачеркивается и игра продолжается.
#     Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
#     Если цифра есть на карточке - игрок проигрывает и игра завершается.
#     Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
#
# Пример одного хода:
#
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 87     - 14    11
#       16 49    55 88    77
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
#
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать с помощью функции-генератора.
#
# Подсказка: для работы с псевдослучайными числами удобно использовать
# модуль random: http://docs.python.org/3/library/random.html


import random
import sys


class Game:
    # color schemes = (31 - 37)
    players = []
    cool_names = ['Алиса', 'Siri', 'OK Google', 'C3PO', 'R2D2', 'Bender', 'Вертер', '1000111001']

    def __new__(cls, player_count, human_name):
        if player_count < 2:
            print('Игроков должно быть не меньше 2.')
            return None
        else:
            return super().__new__(cls)

    def __init__(self, player_count, human_name):
        colors = list(range(31, 38))
        random.shuffle(colors)
        random.shuffle(self.cool_names)

        for cnt in range(0, player_count - 1):
            new_player = LotoCard(self.cool_names[cnt], 'ИскИн')
            new_player.player_color = colors[cnt]
            self.players.append(new_player)

        new_player = LotoCard(human_name, 'КусокМяса')
        new_player.player_color = colors[player_count - 1]
        self.players.append(new_player)

    def the_showe_must_go_on(self):

        show_game = True

        bochonki = list(range(1, 91))
        random.shuffle(bochonki)
        for player in self.players:
            player.generate_card()

        human_player = self.players[len(self.players) - 1]
        winner = ''

        while len(bochonki) > 0 and winner == '':
            bochka = bochonki.pop(0)

            if show_game:
                print("\033[H\033[J")
                print(f'Новый бочонок: {bochka} (осталось {len(bochonki)})')
                for player in self.players:
                    print(player)

                player_have_number = human_player.have_number(bochka)

                str = ''
                while not (str.upper() == 'N' or str.upper() == 'Y' or str.upper() == 'Q'):
                    str = input('Зачеркнуть цифру? (y/n)')

                if str.upper() == 'Q':
                    sys.exit()
                elif str.upper() == 'Y' and player_have_number:
                    human_player.hide_number(bochka)
                elif str.upper() == 'N' and not player_have_number:
                    pass
                else:
                    print('Вы проиграли')
                    self.players.remove(human_player)
                    show_game = False

            for player in self.players:
                if player.have_number(bochka):
                    player.hide_number(bochka)
                if player.unhidden_count == 0:
                    winner = f'{player.player_name} ({player.player_type})'

        print(f'Победил игрок: {winner}')


class LotoCard:
    def __init__(self, player_name, player_type):
        # Имя игрока
        self.player_name = player_name
        # Тип игрока - компьютер или человек
        self.player_type = player_type
        # Состав карточки. Словарь, ключем является значение использованного в карточке числа,
        # а в "значении" будет находиться
        # 1) Номер строки в карточке
        # 2) Количество пустых полей перед этим числом. (Для быстрого вывода)
        # 3) Статус - "закрыто бочонком" или нет. Чтобы выводить либо число либо знак "--"
        # 4) Возможно еще какие-нибудь необходимые параметры хранить. Не заводить же для этого отдельный класс
        self.card = {}
        # Индекс. Хранит порядок расположения чисел в карточке. Для ускорения вывода на экран.
        # Вроде как индекс в базах данных :-)
        self.card__str__index = []
        # Цвет, которым будут отражаться записи для этого игрока. Класс Game назначит цвет в начале сеанса.
        self.player_color = 37
        # Цвет, которым будут отражаться записи для этого игрока. Класс Game назначит цвет в начале сеанса.
        self.unhidden_count = 0

    def set_card_color(self, color):
        self.player_color = color

    def generate_card(self):
        # Перемешивание номеров и выборка первых 15
        card_content = list(range(1, 91))
        random.shuffle(card_content)
        card_content = card_content[0:15]
        for cnt in range(0, 3):
            # Сотрировка каждой пятерки. Т.е. для каждой строки карточки.
            string_content = sorted(card_content[5 * cnt: 5 * (cnt + 1)])
            self.card__str__index = self.card__str__index + string_content

            # Распределение чисел в каждой строке по 5 случайным местам
            string_places = list(range(1, 10))
            random.shuffle(string_places)
            string_places = sorted(string_places[0:5])

            next_place = 1
            for str_cnt in range(0, 5):
                self.card[string_content[str_cnt]] = (cnt, string_places[str_cnt] - next_place, False)
                # В каждом значении словаря храниться:
                # 1) Номер строки в карточке
                # 2) Количество пустых полей перед этим числом. (Для быстрого вывода)
                # 3) Статус - "закрыто бочонком" или нет. Чтобы выводить либо число либо знак "--"
                next_place = string_places[str_cnt] + 1
        self.unhidden_count = 15

    def have_number(self, number):
        return False if self.card.get(number, False) == False else True

    def hide_number(self, number):
        card_value = self.card.get(number, None)
        if card_value is not None:
            new_card_value = (card_value[0], card_value[1], True)
            self.card[number] = new_card_value
            self.unhidden_count -= 1

    def __convert_value_to_str(self, number):
        card_value = self.card.get(number)
        return '   ' * card_value[1] + f'{number if not card_value[2] else "-":>3}'

    def __str__(self):

        # Окраска надписи цветом игрока
        result = f'\033[{self.player_color}m'

        # Заголовок карточки
        header = f' {self.player_name} ({self.player_type}){" - Вы" if self.player_type == "КусокМяса" else ""} '
        symb_count = round((27 - len(header)) / 2)
        result = result + '\n' + '-' * symb_count + header + '-' * symb_count + '\n'

        # result = result + f'\nИгрок {self.player_name} ({self.player_type}) \n' + '-' * 27 + '\n'

        # Построчный вывод основного тела карточки
        result = result + ''.join(map(self.__convert_value_to_str, self.card__str__index[0:5])) + '\n'
        result = result + ''.join(map(self.__convert_value_to_str, self.card__str__index[5:10])) + '\n'
        result = result + ''.join(map(self.__convert_value_to_str, self.card__str__index[10:15])) + '\n'

        # Подвал карточки
        result = result + '-' * 27

        # Завершение обертки в цвет игрока
        result = result + '\033[00m'

        return result

if __name__ == '__main__':

    str_name = input('Как Вас зовут?: ')
    try:
        int_count = int(input('Сколько игроков будет в игре?: '))
    except ValueError:
        print('Введено неверно значение. Игроком будет 2.')
        int_count = 2

    BigGame = Game(int_count, str_name)
    BigGame.the_showe_must_go_on()
