# Gold Collection and Wordle Game Project

## Project Overview

This project contains two distinct algorithms designed for different purposes:

1. **Gold Collection Algorithm**: Aims to maximize gold collection in a matrix grid using dynamic programming and greedy approaches.
2. **Wordle Game**: A simple version of the Wordle game where the player guesses a 4-letter word, with feedback provided on each guess and a backtracking solution if all attempts are exhausted.

### Gold Collection Algorithm

- **Dynamic Programming Approach (`dynamic_collect_gold`)**: Uses a dynamic programming technique to find the optimal path in the matrix that maximizes gold collection.
- **Greedy Approach (`greedy_collect_gold`)**: Uses a greedy algorithm to collect gold by always choosing the next move with the highest immediate reward, including backtracking for validation.

### Wordle Game

- **Gameplay (`play_wordle`)**: Allows the player to guess a random 4-letter word within 10 attempts, providing feedback for each guess.
- **Backtracking Solution**: If the player fails to guess the word within the allowed attempts, a backtracking algorithm attempts to find the correct word.
