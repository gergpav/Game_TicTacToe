from colorama import Fore, Back, Style


class TicTacToeGame:
    """Класс игры "Крестики-нолики"."""
    def __init__(self):
        """Функция, принимающие значения клеток и их цвета"""
        self.spaced_cell = Back.YELLOW + ' ' + Style.RESET_ALL
        self.cell_x = Fore.RED + 'X' + Style.RESET_ALL
        self.cell_o = Fore.BLUE + 'O' + Style.RESET_ALL


    def draw_board(self, board):
        """Функция отрисовки доски."""
        print('\n')
        # Отрисовка доски через цикл
        for i in range(3):
            print(' | '.join(board[i]))
            print('---------')


    def ask_move(self, player, board):
        """
        Функция, запрашивающая пользователя сделать ход.
        Возвращает данные, записанные игроком.
        """
        # Ввод координаты клетки и отработка ошибок ввода
        while True:
            try:
                x, y = input(f'{player}, enter x and y coordinates (e.g. 0 0): ').strip().split()
                if not (x.isdigit() or y.isdigit()) or len((x, y)) != 2:
                    raise ValueError('Invalid input; please enter the numbers (x and y coordinates).')
                break
            except ValueError as e:
                print(e)
        x, y = int(x), int(y)

        # Проверка введенных игроком координат (занято ли место или нет)
        if (0 <= x <= 2) and (0 <= y <= 2) and (board[x][y] == self.spaced_cell):
            return x, y
        else:
            print('That spot is already taken. Try again.')
            return self.ask_move(player, board)


    def make_move(self, player, board, x, y):
        """Функция, которая воспроизводит ход пользователя на доску."""
        if board[x][y] != self.spaced_cell:
            print('That spot is already taken.')
            return False
        board[x][y] = player
        return True


    def ask_and_make_move(self, player, board):
        """Функция для вызова функций ask_move и make_move."""
        x, y = self.ask_move(player, board)
        self.make_move(player, board, x, y)


    def check_win(self, player, board):
        """Функция, проверяющая, выиграл ли пользователь."""
        # Проверка горизонтально и вертикально через цикл
        for i in range(3):
            if board[i] == [player, player, player]:
                return True
            if board[0][i] == player and board[1][i] == player and board[2][i] == player:
                return True
        # Проверка через диагональ
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            return True
        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            return True
        return False


    def tic_tac_toe(self):
        """Основная функция управления игрой."""
        # Цикл раундов для повторного переигрывания
        while True:
            board = [[self.spaced_cell for i in range(3)] for j in range(3)]
            player = self.cell_x

            # Цикл шагов игроков
            while True:
                self.draw_board(board)
                self.ask_and_make_move(player, board)
                if self.check_win(player, board):
                    print(f'{player} won!')
                    break
                tie_game = False
                for row in board:
                    for cell in row:
                        if cell == self.spaced_cell:
                            tie_game = True
                if not tie_game:
                    print('Draw!')
                    break
                player = self.cell_o if player == self.cell_x else self.cell_x

            # Ввод пользователем ответа на вопрос "Желаете ли вы продолжить игру?" и проверка на правильность ввода
            while True:
                restart = input('\nDo you want to play one more game? (y/n) ')
                try:
                    if restart.lower() not in ['y', 'n']:
                        raise ValueError('Invalid input; please enter "y" for yes or "n" for no.')
                    break
                except ValueError as e:
                    print(e)
            # Проверяет, какой ответ ввел пользователь
            if restart.lower() != 'y':
                print('\nThank you for playing the game!')
                break

if __name__ == '__main__':
    game = TicTacToeGame()
    game.tic_tac_toe()
