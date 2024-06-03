def initialize_matrix(n, matrix_input):
    matrix = []
    for row in matrix_input:
        matrix.append([int(cell) if cell.isdigit() else cell for cell in row.split()])
    return matrix


def handle_bandits(matrix, i, j, bandit_tracker):
    """
    Handles the bandit logic for the given cell.

    Parameters:
    matrix (list of list of int/str): The n x n matrix.
    i (int): The row index.
    j (int): The column index.
    bandit_tracker (list of list of bool): The bandit presence tracker.

    Returns:
    int: The penalty (negative gold) due to bandits.
    """
    if i > 0 and matrix[i - 1][j] == '!':
        bandit_tracker[i][j] = not bandit_tracker[i - 1][j]
    if j > 0 and matrix[i][j - 1] == '!':
        bandit_tracker[i][j] = not bandit_tracker[i][j - 1]
    if bandit_tracker[i][j] and isinstance(matrix[i][j], int):
        return -matrix[i][j]
    return 0


def is_valid_move(matrix, i, j, prev_i, prev_j):
    """
    Checks if the move to the given cell is valid.

    Parameters:
    matrix (list of list of int/str): The n x n matrix.
    i (int): The row index.
    j (int): The column index.

    Returns:
    bool: True if the move is valid, False otherwise.
    """
    if (i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix) or matrix[i][j] == 'X' or
            (prev_i == i and prev_j == j)):
        return False
    return True


def calculate_gold(matrix, path):
    """
    Calculates the total gold collected along a given path.

    Parameters:
    matrix (list of list of int/str): The n x n matrix.
    path (list of tuple): The path taken as a list of (i, j) coordinates.

    Returns:
    int: The total gold collected.
    """
    total_gold = 0
    bandit_tracker = [[False] * len(matrix) for _ in range(len(matrix))]

    for idx, (i, j) in enumerate(path):
        if matrix[i][j] == 'X':
            continue
        penalty = handle_bandits(matrix, i, j, bandit_tracker)
        if isinstance(matrix[i][j], int):
            total_gold += matrix[i][j] + penalty

    return total_gold


def greedy_collect_gold(matrix):
    pass

def dp_collect_gold(matrix):
    pass
