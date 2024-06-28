# Gold Collection Algorithm

## Project Overview

This project implements two algorithms to maximize the collection of gold from a matrix grid. The grid contains integers representing gold amounts, 'X' for blocked cells, and '!' for bandits. The two algorithms employed are:

1. **Dynamic Programming Approach (`dynamic_collect_gold`)**
2. **Greedy Approach (`greedy_collect_gold`)**

## File Structure

- `initialize_matrix(matrix_input)`: Initializes the matrix by converting string representations of integers to actual integers.
- `handle_bandits(matrix, i, j, prev_bandit)`: Handles bandit logic, imposing penalties where applicable.
- `is_valid_move(matrix, i, j, prev_i, prev_j)`: Checks the validity of a move.
- `calculate_gold(matrix, path)`: Calculates total gold collected along a specified path.
- `dynamic_collect_gold(matrix)`: Implements the dynamic programming approach to collect the maximum gold.
- `greedy_collect_gold(matrix)`: Implements the greedy approach to collect gold with backtracking.

## Function Explanations

### `dynamic_collect_gold(matrix)`

The `dynamic_collect_gold` function uses dynamic programming to find the optimal path that maximizes gold collection from the top-left to the bottom-right of the matrix.

#### Approach:

1. **Initialization**: 
    - A `dp` matrix is created to store the maximum gold collectible to each cell.
    - A `path` matrix keeps track of the paths leading to each cell.
  
2. **Fill `dp` and `path` matrices**:
    - Iterate through each cell in the matrix.
    - For each cell, compute the maximum gold collectible from the cell above or the cell to the left.
    - Update the `dp` and `path` matrices accordingly.
        - If moving from above results in more gold, update `dp[i][j]` to `dp[i-1][j] + matrix[i][j]` and extend the path from above.
        - If moving from the left results in more gold, update `dp[i][j]` to `dp[i][j-1] + matrix[i][j]` and extend the path from the left.
  
3. **Bandit Handling**:
    - If a bandit ('!') is encountered, propagate the previous maximum without adding any gold penalty.
  
4. **Calculate Total Gold**:
    - Using the `calculate_gold` function, compute the total gold collected along the optimal path found in the `path` matrix.

### `greedy_collect_gold(matrix)`

The `greedy_collect_gold` function uses a greedy algorithm to collect gold by always choosing the next move with the highest immediate gold reward. It includes backtracking to ensure valid paths.

#### Approach:

1. **Initialization**:
    - Start from the top-left corner and initialize total gold collected and the path.
  
2. **Greedy Collection**:
    - For each cell, calculate the potential gold for moving down or right.
    - Choose the direction with the higher gold reward.
    - If both directions yield the same reward, prefer moving right.
        - Calculate potential gold for the next move using `get_gold` function.
        - Update total gold and path based on the chosen move.
  
3. **Bandit and Block Handling**:
    - Apply penalties for cells with bandits using `handle_bandits`.
    - Skip blocked cells ('X').
  
4. **Backtracking**:
    - If a dead-end is reached (no valid moves), backtrack to the previous cell and attempt an alternative path.
        - Use a stack (`backtrack_steps`) to keep track of cells to backtrack to.
        - If backtracking leads to a new path, recalculate the total gold and update the path.
