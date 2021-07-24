"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if not terminal(board):
        x_count = 0
        o_count = 0
        for row in board:
            x_count += row.count(X)
            o_count += row.count(O)
        if x_count > o_count:
            return O
        else:
            return X
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_action = set()
    if not terminal(board):
        for i in range(3):
            for j in range(3):
                if board[i][j] is None:
                    possible_action.add((i, j))
        return possible_action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result = copy.deepcopy(board)
    result[action[0]][action[1]] = player(board)
    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check rows
    columns = []
    for row in board:
        x_count = row.count(X)
        o_count = row.count(O)
        if x_count == 3:
            return X
        if o_count == 3:
            return O
    # check colums
    for j in range(len(board)):
        col = [row[j] for row in board]
        columns.append(col)

    for j in columns:
        x_count = j.count(X)
        o_count = j.count(O)
        if x_count == 3:
            return X
        if o_count == 3:
            return O

    # check diagnols
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    if board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O
    if board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X

    # Tie
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    counter = 0
    for row in board:
        counter += row.count(EMPTY)
    if counter == 0:
        return True
    elif winner(board) is not None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current_palyer = player(board)
    if current_palyer == O:
        v = math.inf
        for action in actions(board):
            move = max_value(result(board, action))
            if move < v:
                v = move
                best = action
    else:
        v = -math.inf
        for action in actions(board):
            move = min_value(result(board, action))
            if move > v:
                v = move
                best = action
    return best


def min_value(board):
    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def max_value(board):
    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v
