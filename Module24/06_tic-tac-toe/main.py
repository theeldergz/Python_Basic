class Cell:
    def __init__(self, index=0, empty=True, sym=' '):
        self.index = index
        self.empty = empty
        self.sym = sym

    def change_symbol(self, new_symbol):
        self.sym = new_symbol
        self.empty = False


class Board:
    def __init__(self):
        self.board_list = [Cell(i) for i in range(10)]

    def create_board(self):
        self.board_list = [Cell(i) for i in range(10)]

    def symbol_list(self):
        sym_list = [sym for i in range(1, 10) for sym in self.board_list[i].sym]
        return sym_list

    def clear_bord(self):
        self.board_list.clear()

    def show_board(self):
        for i in range(1, 11):
            if i == 1 or i == 4 or i == 7:
                print()
                print('-' * 13, end='')
                print()
                print(self.board_list[i].sym, end='')
            elif i == 10:
                print()
                print('-' * 13, end='')
            else:
                print('  |  ', end='')
                print(self.board_list[i].sym, end='')
        print()

    def board_template(self):
        for i in range(1, 11):
            if i == 1 or i == 4 or i == 7:
                print()
                print('-' * 13, end='')
                print()
                print(self.board_list[i].index, end='')
            elif i == 10:
                print()
                print('-' * 13, end='')
            else:
                print('  |  ', end='')
                print(self.board_list[i].index, end='')
        print()


class Player:
    def __init__(self, name, points=0):
        self.name = name
        self.points = points

    def cell_choice(self, symbol, choice_cell):
        choice_cell.change_symbol(symbol)

    def count(self):
        self.points += 10

    def points_info(self):
        print(f'\nТекущий счет игрока {self.name}: {self.points}')


class Game:
    ZERO = '◯'
    PLUS = "✖"

    def __init__(self):
        self.win_conditions = []
        self.board = Board()

        name_player_1 = input("Привет 1 игрок, введи имя: ")
        self.player_1 = Player(name_player_1)
        name_player_2 = input("Привет 2 игрок, введи имя: ")
        self.player_2 = Player(name_player_2)

        print(f"\n{name_player_1} твоими будут символы: {self.PLUS}\n{name_player_2}"
              f"твоими будут символы: {self.ZERO}")
        print('\n↓↓↓ Так выглядит расположение и индекс клеток на поле ↓↓↓')
        self.board.board_template()

    def one_round(self, player, symbol):
        symbol_list = self.board.symbol_list()
        while True:
            if ' ' not in symbol_list:
                return None

            choice = int(input(f'\nИгрок {player.name} просьба ввести номер клетки: '))
            print(self.board.board_list[choice].sym)

            if (self.ZERO == self.board.board_list[choice].sym) or (self.PLUS == self.board.board_list[choice].sym):
                print('Клетка занята!')
                continue
            else:
                player.cell_choice(symbol, self.board.board_list[choice])
                self.win_conditions = [
                    [self.board.board_list[1].sym, self.board.board_list[2].sym, self.board.board_list[3].sym],
                    [self.board.board_list[4].sym, self.board.board_list[5].sym, self.board.board_list[6].sym],
                    [self.board.board_list[7].sym, self.board.board_list[8].sym, self.board.board_list[9].sym],
                    [self.board.board_list[1].sym, self.board.board_list[4].sym, self.board.board_list[7].sym],
                    [self.board.board_list[2].sym, self.board.board_list[5].sym, self.board.board_list[8].sym],
                    [self.board.board_list[3].sym, self.board.board_list[6].sym, self.board.board_list[9].sym],
                    [self.board.board_list[1].sym, self.board.board_list[5].sym, self.board.board_list[9].sym],
                    [self.board.board_list[3].sym, self.board.board_list[5].sym, self.board.board_list[7].sym]
                ]
                self.board.board_list[choice].change_symbol(symbol)
                self.board.show_board()

                for sub_list in self.win_conditions:
                    if (self.PLUS == sub_list[0]) and (self.PLUS == sub_list[1]) and (self.PLUS == sub_list[2]):
                        player.count()
                        print(f'\nУРА! ПОБЕДИЛ ИГРОК: {player.name}\nНАБРАНО ОЧКОВ: {player.points}')
                        return True

                    elif (self.ZERO == sub_list[0]) and (self.ZERO == sub_list[1]) and (self.ZERO == sub_list[2]):
                        player.count()
                        print(f'\nУРА! ПОБЕДИЛ ИГРОК: {player.name}\nНАБРАНО ОЧКОВ: {player.points}')
                        return True

                else:
                    return False

    def one_game(self):
        self.board.clear_bord()
        self.board.create_board()

        while True:
            flag_1 = self.one_round(self.player_1, self.PLUS)
            if flag_1:
                return True
            elif flag_1 is None:
                print('\nНИЧЬЯ!')
                return False

            flag_2 = self.one_round(self.player_2, self.ZERO)
            if flag_2:
                return True
            elif flag_2 is None:
                print('\nНИЧЬЯ!')
                return False

    def playing(self):
        while True:
            self.one_game()
            self.player_1.points_info()
            self.player_2.points_info()
            is_continue = int(input('\nНажмите 1 чтобы сыграть еще раз!'
                                    '\nНажмите 2 чтобы выйти '))
            if is_continue == 1:
                continue
            elif is_continue == 2:
                input('Нажмите любую клавишу...')
                break


z = Game()
z.playing()
