# Создайте программу для игры в ""Крестики-нолики""

board = list(map(str, range(1, 10)))


def game_board():
    print('-' * 20)
    for i in range(3):
        for k in range(3):
            print(f"{board[k + i * 3]:^5}", end=" ")
        print(f"\n{'-' * 20}")
    print()


def place_sign(token):
    global board
    while True:
        answer = input(f"Ход игрока {token}. Введите число от 1 до 9.\n ")
        if answer.isdigit() and int(answer) in range(1, 10):
            answer = int(answer)
            pos = board[answer - 1]
            if pos not in (chr(10060), chr(11093)):
                board[answer - 1] = chr(10060) if token == "X" else chr(11093)
                break
            else:
                print(f"Это поле уже занято")
        else:
            print(f"Некорректные данные")


def check_win():
    winning_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    n = [board[x[0]] for x in winning_combinations if board[x[0]] == board[x[1]] == board[x[2]]]
    return n[0] if n else n


def main():
    count = 0
    game_board()
    while True:
        place_sign("O") if count % 2 else place_sign("X")
        game_board()

        if count > 3:
            if check_win():
                print(f"{check_win()} - ПОБЕДА!")
                break
        if count == 8:
            print(f"Ничья!")
            break
        count += 1


main()