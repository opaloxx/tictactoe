# функция оценки выигрышности текущей позиции для игрока who
def check_score(board, who):
    win_comb = [
        [board[0], board[1], board[2]],  # 1 ряд
        [board[3], board[4], board[5]],  # 2 ряд
        [board[6], board[7], board[8]],  # 3 ряд
        [board[0], board[3], board[6]],  # 1 столбик
        [board[1], board[4], board[7]],  # 2 столбик
        [board[2], board[5], board[8]],  # 3 столбик
        [board[0], board[4], board[8]],  # диагональ
        [board[2], board[4], board[6]],  # диагональ
    ]
    for i in win_comb:
        if i.count(who) == 3:
            return 10
        elif i.count("o" if who == "x" else "x") == 3:
            return -10
    return 0  # ничья


def minimax(board, who, depth=9, is_my_turn=False):
    score = check_score(board, who)
    if score == 10 or score == -10 or depth == 0:
        return score * depth

    if is_my_turn:
        best_score = -100
        for i in range(9):
            if board[i] == "-":
                board[i] = who
                best_score = max(best_score, minimax(board, who, depth - 1, False))
                board[i] = "-"
        return best_score
    else:
        best_score = 100
        for i in range(9):
            if board[i] == "-":
                board[i] = "o" if who == "x" else "x"
                best_score = min(best_score, minimax(board, who, depth - 1, True))
                board[i] = "-"
        return best_score


def main():
    board = []
    for i in range(3):
        row = input().split()
        board.append(row[0])
        board.append(row[1])
        board.append(row[2])
    player = input()

    best_val = -100
    best_move = -1
    for i in range(9):
        if board[i] == "-":
            board[i] = player
            val = minimax(board, player)
            board[i] = "-"
            if val > best_val:
                best_val = val
                best_move = i

    board[best_move] = player
    print()
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])


if __name__ == "__main__":
    main()
