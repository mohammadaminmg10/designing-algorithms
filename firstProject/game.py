
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


def dynamic_collect_gold(matrix):
    n = len(matrix)

    # Initialize dp and path matrices
    dp = [[0] * n for _ in range(n)]
    path = [[[] for _ in range(n)] for _ in range(n)]

    # Initialize the starting point
    dp[0][0] = matrix[0][0] if isinstance(matrix[0][0], int) else 0
    path[0][0] = [(0, 0)]  # Start with the starting cell in the path

    # Fill dp and path arrays
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue  # Skip the starting point since it's already initialized

            if isinstance(matrix[i][j], int):
                # Calculate max gold collected to reach (i, j) from (i-1, j) or (i, j-1)
                max_gold_from_above = dp[i - 1][j] if i > 0 else float('-inf')
                max_gold_from_left = dp[i][j - 1] if j > 0 else float('-inf')

                if max_gold_from_above > max_gold_from_left:
                    dp[i][j] = max_gold_from_above + matrix[i][j]
                    path[i][j] = path[i - 1][j] + [(i, j)]
                else:
                    dp[i][j] = max_gold_from_left + matrix[i][j]
                    path[i][j] = path[i][j - 1] + [(i, j)]

            elif matrix[i][j] == '!':
                # Handle bandit, just propagate the previous maximum without adding any gold penalty
                max_gold_from_above = dp[i - 1][j] if i > 0 else float('-inf')
                max_gold_from_left = dp[i][j - 1] if j > 0 else float('-inf')

                if max_gold_from_above > max_gold_from_left:
                    dp[i][j] = max_gold_from_above
                    path[i][j] = path[i - 1][j] + [(i, j)]
                else:
                    dp[i][j] = max_gold_from_left
                    path[i][j] = path[i][j - 1] + [(i, j)]

            # Handle blocked cells ('X'), no action needed

    # Get the path to the bottom-right corner
    final_path = path[n - 1][n - 1]

    # Calculate the total gold collected along the path
    total_gold = calculate_gold(matrix, final_path)

    return total_gold, final_path


def greedy_collect_gold(matrix):
    n = len(matrix)
    i, j = 0, 0
    total_gold = 0
    prev_bandit = False
    path = [(i, j)]
    visited = set([(i, j)])
    backtrack_steps = []

    def get_gold(i, j, prev_bandit):
        if matrix[i][j] == 'X':
            return float('-inf'), False
        penalty, current_bandit = handle_bandits(matrix, i, j, prev_bandit)
        if isinstance(matrix[i][j], int):
            return matrix[i][j] + (penalty * 2), current_bandit
        return 0, current_bandit

    penalty, prev_bandit = handle_bandits(matrix, i, j, prev_bandit)
    if isinstance(matrix[i][j], int):
        total_gold += matrix[i][j] + (penalty * 2)

    while i < n - 1 or j < n - 1:
        if total_gold < 0:
            total_gold = 0
        down_gold = right_gold = float('-inf')
        next_move = None

        if i + 1 < n and (i + 1, j) not in visited:
            down_gold, next_bandit_down = get_gold(i + 1, j, prev_bandit)
        if j + 1 < n and (i, j + 1) not in visited:
            right_gold, next_bandit_right = get_gold(i, j + 1, prev_bandit)

        if down_gold > right_gold:
            next_move = (i + 1, j)
            next_bandit = next_bandit_down
            if total_gold >= 0:
                total_gold += down_gold
            backtrack_steps.append((i, j + 1))
        elif right_gold > down_gold:
            next_move = (i, j + 1)
            next_bandit = next_bandit_right
            if total_gold >= 0:
                total_gold += right_gold
            backtrack_steps.append((i + 1, j))
        elif down_gold == right_gold and down_gold != float('-inf'):
            next_move = (i, j + 1)
            next_bandit = next_bandit_right
            if total_gold >= 0:
                total_gold += right_gold
            backtrack_steps.append((i + 1, j))

        if next_move:
            i, j = next_move
            path.append(next_move)
            visited.add(next_move)
            # total_gold += matrix[i][j] if isinstance(matrix[i][j], int) else 0
            prev_bandit = next_bandit
        else:
            # Backtracking
            backtrack_steps_i = 0
            while backtrack_steps:
                i, j = backtrack_steps.pop()
                backtrack_steps_i += 1
                if (i, j) not in visited:
                    break
            else:
                return -1, []  # No possible path

            while backtrack_steps_i > 0:
                path.pop()
                backtrack_steps_i -= 1
            path.append((i, j))
            visited.add((i, j))
            total_gold = calculate_gold(matrix, path)
            prev_bandit = False
            last_cell = path[-1]
            if matrix[last_cell[0]][last_cell[1]] == '!':
                prev_bandit = True

    return total_gold, path
