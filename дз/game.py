import flet as ft

# Глобальные переменные для состояния игры
current_player = "X"
board = [""] * 9  # Изначально все ячейки пустые
game_over = False

def main(page: ft.Page):
    global current_player, board, game_over

    page.title = "Крестики-нолики"
    
    # Создаем сетку для игры
    grid = ft.Column()

    # Создаем кнопки для каждой ячейки
    buttons = []
    for i in range(3):
        row = ft.Row()
        for j in range(3):
            button = ft.ElevatedButton(text=" ", on_click=lambda e, index=i*3+j: make_move(index), width=100, height=100)
            buttons.append(button)
            row.controls.append(button)
        grid.controls.append(row)

    page.add(grid)

    # Функция для обработки хода
    def make_move(index):
        global current_player, board, game_over

        if board[index] == "" and not game_over:
            board[index] = current_player
            buttons[index].text = current_player
            buttons[index].disabled = True
            
            if check_winner():
                page.add(ft.Text(f"Игрок {current_player} выиграл!", size=20))
                game_over = True
            elif "" not in board:
                page.add(ft.Text("Ничья!", size=20))
                game_over = True
            else:
                current_player = "O" if current_player == "X" else "X"

            page.update()

    # Функция для проверки победителя
    def check_winner():
        winning_combinations = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]
        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
                return True
        return False

# Запускаем приложение
ft.app(target=main)