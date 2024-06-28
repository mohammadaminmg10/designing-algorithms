# Wordle Game

## Project Overview

This project implements a simple version of the Wordle game where the player has to guess a random 4-letter word within 10 attempts. The game provides feedback on each guess, indicating if letters are correct and in the correct position, correct but in the wrong position, or incorrect. Additionally, a backtracking algorithm is used to solve the word if the player fails to guess it within the allowed attempts.

## File Structure

- `generate_word_list()`: Generates a sample list of random 4-letter words.
- `select_random_word(word_list)`: Selects a random word from the generated word list.
- `provide_feedback(selected_word, guess)`: Provides feedback for a guess.
- `backtrack(guesses, feedbacks, word_list)`: Uses backtracking to improve the guessing strategy.
- `is_valid_guess(word, guesses, feedbacks)`: Checks if a guess is valid based on the feedback.
- `play_wordle()`: Main game function that orchestrates the gameplay.

## Function Explanations

### `generate_word_list()`

Generates a list of 4-letter words where each word has all unique letters.

#### Approach:

1. Define a list of sample 4-letter words.
2. Filter the list to include only words with all unique letters.
3. Return the filtered list.

### `select_random_word(word_list)`

Selects and returns a random word from the provided word list using the `random.choice` function.

### `provide_feedback(selected_word, guess)`

Provides feedback for a given guess by comparing it with the selected word.

#### Approach:

1. Initialize an empty list `feedback`.
2. Loop through each letter of the guess:
   - If the letter matches the corresponding letter in the selected word, append '=' to `feedback`.
   - If the letter is in the selected word but in a different position, append '+' to `feedback`.
   - Otherwise, append '-' to `feedback`.
3. Join the `feedback` list into a string and return it.

### `backtrack(guesses, feedbacks, word_list)`

Uses a backtracking algorithm to find the correct word if the player fails to guess it within the allowed attempts.

#### Approach:

1. Check if the last feedback is "====", indicating the correct word is found.
2. Loop through each word in the word list:
   - If the word is a valid guess based on previous guesses and feedbacks, append it to the guesses list.
   - Provide feedback for the guess and append it to the feedbacks list.
   - Recursively call `backtrack` with the updated guesses and feedbacks.
   - If the correct word is found, return it.
   - If not, remove the last guess and feedback and continue.
3. Return `None` if no valid word is found.

### `is_valid_guess(word, guesses, feedbacks)`

Checks if a word is a valid guess based on previous guesses and their feedbacks.

#### Approach:

1. Loop through each previous guess and its corresponding feedback.
2. Provide feedback for the current word against each previous guess.
3. If the feedback does not match the previous feedback, return `False`.
4. Return `True` if all feedbacks match.

### `play_wordle()`

The main function that handles the gameplay.

#### Approach:

1. Generate a word list using `generate_word_list()`.
2. Select a random word using `select_random_word(word_list)`.
3. Initialize the number of attempts and display the game instructions.
4. Loop through the allowed number of attempts:
   - Prompt the player for a guess.
   - Validate the guess to ensure it is a 4-letter word with unique letters.
   - Provide feedback for the guess and display it.
   - Check if the guess is correct; if so, congratulate the player and exit.
5. If the player fails to guess the word, use backtracking to find and display the correct word.
