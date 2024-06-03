def initialize_matrix(matrix_input):
    for i, row in enumerate(matrix_input):
        matrix_input[i] = [int(item) if item.isdigit() else item for item in row]
    return matrix_input


def handle_bandits(matrix, i, j, prev_bandit):
    """
    Handles the bandit logic for the given cell.

    Parameters:
    matrix (list of list of int/str): The n x n matrix.
    i (int): The row index.
    j (int): The column index.
    prev_bandit (bool): Whether the previous cell had a bandit.

    Returns:
    int: The penalty (negative gold) due to bandits.
    bool: Whether the current cell has a bandit.
    """
    if prev_bandit and isinstance(matrix[i][j], int):
        return -matrix[i][j], False
    if matrix[i][j] == '!':
        return 0, True
    return 0, False


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
    prev_bandit = False  # Keeps track if the previous cell had a bandit

    for (i, j) in path:
        if matrix[i][j] == 'X':
            continue
        penalty, prev_bandit = handle_bandits(matrix, i, j, prev_bandit)
        if isinstance(matrix[i][j], int):
            total_gold += matrix[i][j] + penalty

    return total_gold


def greedy_collect_gold(matrix):
    pass

def dp_collect_gold(matrix):
    pass
