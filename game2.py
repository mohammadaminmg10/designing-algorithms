"""
Wordle Game

Author: Amir Mahmoudian
Date: 2024-06-12

Description: This program is a simple implementation of the Wordle game. The player inputs a 4-letter word with non-repeating letters,
and the program attempts to guess the word in the fewest steps possible. The program provides feedback for each guess in the form of '=' for correct
letter in correct position, '+' for correct letter in wrong position, and '-' means incorrect letter. If the program fails
to guess the word, it uses backtracking to find the word.

The time complexity of the backtracking algorithm is O(n!), where n is the number of words in the sample list.
"""

# Import necessary libraries
import itertools


def provide_feedback(selected_word, guess):
    feedback = []
    for i in range(4):
        if guess[i] == selected_word[i]:
            feedback.append('=')
        elif guess[i] in selected_word:
            feedback.append('+')
        else:
            feedback.append('-')
    return ''.join(feedback)


def backtrack(guesses, feedbacks, remaining_words):
    if feedbacks and feedbacks[-1] == "====":
        return guesses[-1]

    for word in remaining_words:
        if is_valid_guess(word, guesses, feedbacks):
            guesses.append(word)
            feedback = provide_feedback(selected_word, word)
            feedbacks.append(feedback)
            result = backtrack(guesses, feedbacks, remaining_words)
            if result is not None:
                return result
            guesses.pop()
            feedbacks.pop()

    return None


def is_valid_guess(word, guesses, feedbacks):
    for guess, feedback in zip(guesses, feedbacks):
        if provide_feedback(word, guess) != feedback:
            return False
    return True


# Main game function
def play_wordle():
    global selected_word  # Declare selected_word as global for backtracking to access it

    # Get the word from the user
    selected_word = input("Please enter a 4-letter word with non-repeating letters: ").strip().lower()

    if len(selected_word) != 4 or len(set(selected_word)) != 4:
        print("Invalid word. Make sure it is a 4-letter word with non-repeating letters.")
        return

    print("The algorithm will now try to guess the word in the fewest steps possible.")
    print(
        "Feedback: '=' means correct letter in correct position, '+' means correct letter in wrong position, '-' means incorrect letter.")

    # Generate all possible 4-letter words with non-repeating letters
    possible_letters = 'abcdefghijklmnopqrstuvwxyz'
    possible_words = [''.join(word) for word in itertools.permutations(possible_letters, 4)]

    guesses = []
    feedbacks = []

    attempts = 0
    while attempts < 10 and possible_words:
        possible_words.sort(key=lambda word: len(set(word)), reverse=True)

        guess = possible_words.pop(0)
        feedback = provide_feedback(selected_word, guess)
        print(f"Attempt {attempts + 1}: Guess: {guess}, Feedback: {feedback}")

        guesses.append(guess)
        feedbacks.append(feedback)
        attempts += 1

        if feedback == "====":
            print("The algorithm guessed the word correctly.")
            return

        # Filter possible words based on feedback
        possible_words = [word for word in possible_words if is_valid_guess(word, guesses, feedbacks)]

    # Use backtracking to find the word if the algorithm has failed in 10 attempts
    print("Trying to solve with backtracking...")
    solution = backtrack(guesses, feedbacks, possible_words)
    if solution:
        print(f"Backtracking found the word: {solution}")
    else:
        print(f"Sorry, the algorithm couldn't guess the word. The correct word was: {selected_word}")


play_wordle()
