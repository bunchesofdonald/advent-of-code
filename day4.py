def parse_input(lines):
    draw_order = [int(number) for number in lines[0].strip().split(',')]

    # Boards start on line 3
    boards = []
    current_board = []
    for line in lines[2:]:
        if line:
            current_board.append([int(number) for number in line.split()])
        else:
            boards.append(current_board)
            current_board = []

    return (draw_order, boards)


def board_to_sets(board):
    board_size = len(board[0])
    board_sets = []
    for row in board:
        board_sets.append(set(row))

    for i in range(board_size):
        board_set = set()
        for j in range(board_size):
            board_set.add(board[j][i])

        board_sets.append(board_set)

    return board_sets


def score_all_boards(draw_order, boards):
    board_scores = []
    complete_boards = set()
    called_numbers = set()
    for last_called in draw_order:
        called_numbers.add(last_called)
        for i, board in enumerate(boards):
            if i not in complete_boards and board_complete(called_numbers, board):
                board_scores.append(board_score(board, called_numbers, last_called))
                complete_boards.add(i)

    return board_scores


def board_score(board, called_numbers, last_called):
    board_score = 0
    for row in board:
        for number in row:
            if number not in called_numbers:
                board_score += number

    return board_score * last_called


def board_complete(called_numbers, board):
    board_sets = board_to_sets(board)
    for number_set in board_sets:
        if len(number_set - called_numbers) == 0:
            return True

    return False


if __name__ == "__main__":
    with open('day4.txt') as infile:
        draw_order, boards = parse_input([line.strip() for line in infile.readlines()])

    board_scores = score_all_boards(draw_order, boards)
    print(board_scores[0])
    print(board_scores[-1])
