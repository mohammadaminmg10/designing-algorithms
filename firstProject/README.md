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

Sure! Here is the Markdown formatted analysis for the `initialize_matrix` function:

## Time Complexity Analysis

### Function: `initialize_matrix`

### Analysis

1. **Outer Loop**:
   ```python
   for I, row in enumerate(matrix_input):
   ```
   - This loop iterates over each row in the input matrix `matrix_input`.
   - Let `n` be the number of rows in the matrix.

2. **Inner List Comprehension**:
   ```python
   matrix_input[I] = [int(item) if item.isdigit() else item for item in row]
   ```
   - This list comprehension iterates over each item in the current row.
   - Let `m` be the number of items (columns) in each row.
   - The `isdigit()` method and `int()` conversion are both O(1) operations.
   - Therefore, the list comprehension has a time complexity of O(m) for each row.

### Combined Complexity

Since the outer loop runs `n` times and for each iteration, the inner list comprehension runs `m` times, the overall time complexity of the function is the product of these two operations:

O(n) * O(m) = O(n*m)

### Conclusion

The time complexity of the `initialize_matrix` function is O(n*m), where `n` is the number of rows and `m` is the number of columns in the input matrix `matrix_input`.

### Function: `handle_bandits`

### Analysis

1. **Checking `prev_bandit` and `isinstance`**:
   ```python
   if prev_bandit and isinstance(matrix[i][j], int):
   ```
   - The check `prev_bandit` is \( O(1) \) since it's a simple boolean evaluation.
   - The `isinstance(matrix[i][j], int)` function checks if the element at position `[i][j]` is an integer, which is \( O(1) \).

2. **Returning Based on Condition**:
   ```python
   return -matrix[i][j], False
   ```
   - This return statement is \( O(1) \) since accessing an element in a list and returning a tuple are both \( O(1) \) operations.

3. **Checking Equality**:
   ```python
   if matrix[i][j] == '!':
   ```
   - The equality check `matrix[i][j] == '!'` is \( O(1) \).

4. **Returning Based on Second Condition**:
   ```python
   return 0, True
   ```
   - This return statement is \( O(1) \).

5. **Default Return**:
   ```python
   return 0, False
   ```
   - The default return statement is \( O(1) \).

### Combined Complexity

Each operation in the function is a constant time operation, meaning they all have \( O(1) \) complexity.

### Conclusion

The time complexity of the `handle_bandits` function is \( O(1) \).

### Function: `is_valid_move`


### Analysis

1. **Boundary Checks**:
   ```python
   if (i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix))
   ```
   - The checks `i < 0`, `i >= len(matrix)`, `j < 0`, and `j >= len(matrix)` are all constant time operations \( O(1) \).

2. **Matrix Value Check**:
   ```python
   matrix[i][j] == 'X'
   ```
   - Checking if `matrix[i][j] == 'X'` is an \( O(1) \) operation, as it involves a single list access and a comparison.

3. **Previous Position Check**:
   ```python
   prev_i == i and prev_j == j
   ```
   - Checking if `prev_i == i and prev_j == j` is an \( O(1) \) operation since it involves two comparisons.

### Combined Complexity

All operations in the conditional statement are \( O(1) \). Therefore, the `if` statement as a whole is \( O(1) \). The return statements are also \( O(1) \) operations.

### Conclusion

The time complexity of the `is_valid_move` function is \( O(1) \).

### Function: `calculate_gold`

### Analysis

1. **Initialization**:
   ```python
   total_gold = 0
   prev_bandit = False
   ```
   - These are \( O(1) \) operations.

2. **Loop Over Path**:
   ```python
   for (i, j) in path:
   ```
   - This loop iterates over each coordinate in the `path`.
   - Let \( p \) be the length of the path, i.e., the number of coordinates.

3. **Negative Gold Check and Reset**:
   ```python
   if total_gold < 0:
       total_gold = 0
   ```
   - This check and reset operation is \( O(1) \).

4. **Obstacle Check**:
   ```python
   if matrix[i][j] == 'X':
       continue
   ```
   - Checking if `matrix[i][j]` is equal to `'X'` is \( O(1) \).

5. **Handle Bandits**:
   ```python
   penalty, prev_bandit = handle_bandits(matrix, i, j, prev_bandit)
   ```
   - The `handle_bandits` function is called, which has a time complexity of \( O(1) \).

6. **Gold Calculation**:
   ```python
   if isinstance(matrix[i][j], int):
       total_gold += matrix[i][j] + (penalty * 2)
   ```
   - Checking if `matrix[i][j]` is an integer and performing arithmetic operations are \( O(1) \).

### Combined Complexity

- Each iteration of the loop performs a constant amount of work (\( O(1) \)).
- Since the loop runs \( p \) times (once for each coordinate in the path), the overall time complexity of the loop is \( O(p) \).

### Conclusion

The time complexity of the `calculate_gold` function is \( O(p) \), where \( p \) is the length of the path.

### Function: `dynamic_collect_gold`

### Analysis

1. **Initialization**:
   ```python
   n = len(matrix)
   dp = [[0] * n for _ in range(n)]
   path = [[[] for _ in range(n)] for _ in range(n)]
   dp[0][0] = matrix[0][0] if isinstance(matrix[0][0], int) else 0
   path[0][0] = [(0, 0)]
   ```
   - The initialization of `dp` and `path` matrices involves creating two \( n \times n \) matrices, which takes \( O(n^2) \) time.
   - Initializing the starting point is \( O(1) \).

2. **Filling dp and path arrays**:
   ```python
   for i in range(n):
       for j in range(n):
           if i == 0 and j == 0:
               continue

           if isinstance(matrix[i][j], int):
               max_gold_from_above = dp[i - 1][j] if i > 0 else float('-inf')
               max_gold_from_left = dp[i][j - 1] if j > 0 else float('-inf')

               if max_gold_from_above > max_gold_from_left:
                   dp[i][j] = max_gold_from_above + matrix[i][j]
                   path[i][j] = path[i - 1][j] + [(i, j)]
               else:
                   dp[i][j] = max_gold_from_left + matrix[i][j]
                   path[i][j] = path[i][j - 1] + [(i, j)]

           elif matrix[i][j] == '!':
               max_gold_from_above = dp[i - 1][j] if i > 0 else float('-inf')
               max_gold_from_left = dp[i][j - 1] if j > 0 else float('-inf')

               if max_gold_from_above > max_gold_from_left:
                   dp[i][j] = max_gold_from_above
                   path[i][j] = path[i - 1][j] + [(i, j)]
               else:
                   dp[I][j] = max_gold_from_left
                   path[I][j] = path[I][j - 1] + [(I, j)]
   ```
   - The nested loops run \( n \times n \) times.
   - Each iteration of the inner loop involves a constant amount of work (\( O(1) \)) for the gold calculation and path update.
   - Therefore, filling the `dp` and `path` arrays takes \( O(n^2) \) time.

3. **Get the path to the bottom-right corner**:
   ```python
   final_path = path[n - 1][n - 1]
   ```
   - Retrieving the path from `path[n-1][n-1]` is \( O(1) \).

4. **Calculate the total gold collected along the path**:
   ```python
   total_gold = calculate_gold(matrix, final_path)
   ```
   - The `calculate_gold` function has a time complexity of \( O(p) \), where \( p \) is the length of the path.
   - In the worst case, \( p \) can be \( O(n^2) \).

### Combined Complexity

- Initialization: \( O(n^2) \)
- Filling dp and path arrays: \( O(n^2) \)
- Calculating total gold: \( O(n^2) \) (in the worst case)

### Conclusion

The overall time complexity of the `dynamic_collect_gold` function is \( O(n^2) \).

### Function: `greedy_collect_gold`

### Analysis

1. **Initialization**:
   - Initializing variables and data structures like `i`, `j`, `total_gold`, `prev_bandit`, `path`, `visited`, and `backtrack_steps` are all \( O(1) \).

2. **Greedy Approach Loop**:
   - The main loop iterates through the matrix while either `i` or `j` is less than `n - 1`, which could potentially iterate up to \( 2n - 2 \) times in the worst case.
   - Each iteration involves checking potential moves (`down_gold` and `right_gold`) and choosing the better option.
   - Calculating `down_gold` and `right_gold` involves calling `get_gold` which in turn calls `handle_bandits`, both of which are \( O(1) \) operations.
   - Adjusting `total_gold`, updating `backtrack_steps`, and managing `path` and `visited` are \( O(1) \) operations each within the loop.

3. **Backtracking**:
   - When backtracking occurs (if no valid move is found), it pops elements from `backtrack_steps`, adjusts `path`, and recalculates `total_gold`.
   - Backtracking might need to pop several elements, but each operation is \( O(1) \) due to the use of lists and sets.

4. **Calculate Gold Function**:
   - The function calls `calculate_gold`, which has a time complexity of \( O(p) \), where \( p \) is the length of `path`.

### Combined Complexity

- The main loop runs up to \( O(n^2) \) times in the worst case scenario.
- Each iteration of the loop involves \( O(1) \) operations for updating variables and \( O(1) \) operations for `get_gold`, `handle_bandits`, and path management.
- Backtracking operations also contribute \( O(1) \) operations per step.

### Conclusion

The overall time complexity of the `greedy_collect_gold` function is \( O(n^2) \), where \( n \) is the size of the input matrix.