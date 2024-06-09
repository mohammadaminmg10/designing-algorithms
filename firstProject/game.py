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
            total_gold += matrix[i][j] + (penalty * 2)

    return total_gold


def dynamic_collect_gold(matrix, i=0, j=0, prev_bandit=False, memo=None):
    if memo is None:
        memo = {}
    n = len(matrix)

    # Base case: If out of bounds or blocked cell
    if i >= n or j >= n or matrix[i][j] == 'X':
        return float('-inf')

    # Base case: If reached the bottom-right corner
    if i == n - 1 and j == n - 1:
        if isinstance(matrix[i][j], int):
            return matrix[i][j]
        else:
            return 0

    # Check if the subproblem has been solved
    if (i, j, prev_bandit) in memo:
        return memo[(i, j, prev_bandit)]

    # Handle the current cell's bandit logic
    penalty, current_bandit = handle_bandits(matrix, i, j, prev_bandit)

    # Calculate gold for current cell
    if isinstance(matrix[i][j], int):
        current_gold = matrix[i][j]
    else:
        current_gold = 0

    # Recur for the right and down moves
    gold_right = dynamic_collect_gold(matrix, i, j + 1, current_bandit, memo)
    gold_down = dynamic_collect_gold(matrix, i + 1, j, current_bandit, memo)

    # Apply the penalty to the gold from the next move
    most_next_gold = max(gold_right, gold_down)
    if current_bandit and most_next_gold != float('-inf'):
        most_next_gold -= penalty

    # Calculate the total gold for the current cell
    total_gold = current_gold + most_next_gold

    # Adjust the gold for bandit penalties
    if current_bandit and total_gold != float('-inf'):
        next_cell_value = matrix[i + 1][j] if i < n - 1 else matrix[i][j + 1]
        if isinstance(next_cell_value, int):
            total_gold -= next_cell_value

    # Store the result in memoization dictionary
    memo[(i, j, prev_bandit)] = total_gold

    return total_gold


def greedy_collect_gold(matrix):
    """
    Calculates the maximum gold that can be collected by following a greedy strategy.

    Args:
    `matrix` (list of list of int/str): The n x n matrix.

    Returns:
    `int`: The maximum gold that can be collected. Returns `-1` if the greedy strategy is not possible.
    """
    n = len(matrix)
    i, j = 0, 0
    total_gold = 0
    prev_bandit = False

    # Handle the starting cell (0, 0)
    penalty, prev_bandit = handle_bandits(matrix, i, j, prev_bandit)
    if isinstance(matrix[i][j], int):
        total_gold += matrix[i][j] + penalty

    while i < n - 1 or j < n - 1:
        down_gold = right_gold = float('-inf')
        next_move = None

        # Check the down move
        if i + 1 < n and matrix[i + 1][j] != 'X':
            penalty, next_bandit_down = handle_bandits(matrix, i + 1, j, prev_bandit)
            down_gold = (matrix[i + 1][j] if isinstance(matrix[i + 1][j], int) else 0) + (penalty*2)
            down_move = (i + 1, j)
        
        # Check the right move
        if j + 1 < n and matrix[i][j + 1] != 'X':
            penalty, next_bandit_right = handle_bandits(matrix, i, j + 1, prev_bandit)
            right_gold = (matrix[i][j + 1] if isinstance(matrix[i][j + 1], int) else 0) + (penalty*2)
            right_move = (i, j + 1)

        # Determine the best move
        if down_gold > right_gold and down_gold > 0:
            next_move = down_move
            total_gold += down_gold
            prev_bandit = next_bandit_down
        elif right_gold >= down_gold and right_gold > 0:
            next_move = right_move
            total_gold += right_gold
            prev_bandit = next_bandit_right
        
        if next_move:
            i, j = next_move
        else:
            # If no valid move is found, we are at an impassable point
            total_gold = -1
            break

    return total_gold
