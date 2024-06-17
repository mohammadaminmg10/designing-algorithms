"""
Worlde Game

Author: Amir Mahmoudian
Date: 2024-06-12

Description: This program is a simple implementation of the Wordle game. The player has to guess a 4-letter word
with non-repeating letters in 10 attempts. The program provides feedback for each guess in the form of '=' for correct
letter in correct position, '+' for correct letter in wrong position, and '-' for incorrect letter. If the player fails
to guess the word in 10 attempts, the program uses backtracking to find the word.

The time complexity of the backtracking algorithm is O(n!), where n is the number of words in the sample list.
"""

# Import necessary libraries
import random


# Generate a sample list of random 4-letter words
def generate_word_list():
    words = ["bark", "dart", "fast", "grip", "hint", "jolt", "leap", "mask", "nest",
             "pact", "quip", "rust", "silk", "tamp", "vase", "wave", "yarn", "zinc",
             "bump", "dusk", "fist", "golf", "hike", "jazz", "lend", "mash", "nail",
             "palm", "quiz", "rung", "sift", "tank", "vest", "wisp", "yelp", "zero",
             "bulk", "dive", "fume", "goat", "hail", "jade", "lure", "mild", "navy"]
    return [word for word in words if len(set(word)) == 4]


# Select a random word from the sample list
def select_random_word(word_list):
    return random.choice(word_list)


# Provide feedback for a guess
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


# Backtracking function to improve guessing strategy
def backtrack(guesses, feedbacks, word_list):
    if feedbacks and feedbacks[-1] == "====":
        return guesses[-1]

    for word in word_list:
        if is_valid_guess(word, guesses, feedbacks):
            guesses.append(word)
            feedback = provide_feedback(selected_word, word)
            feedbacks.append(feedback)
            result = backtrack(guesses, feedbacks, word_list)
            if result is not None:
                return result
            guesses.pop()
            feedbacks.pop()

    return None


# Check if the guess is valid based on the feedback
def is_valid_guess(word, guesses, feedbacks):
    for guess, feedback in zip(guesses, feedbacks):
        if provide_feedback(word, guess) != feedback:
            return False
    return True


# Main game function
def play_wordle():
    word_list = generate_word_list()
    global selected_word  # Declare selected_word as global for backtracking to access it
    selected_word = select_random_word(word_list)
    attempts = 10

    print("Welcome to Wordle! Guess the 4-letter word. You have 10 attempts.")
    print(
        "Feedback: '=' means correct letter in correct position, '+' means correct letter in wrong position, '-' means incorrect letter.")

    guesses = []
    feedbacks = []

    for attempt in range(attempts):
        guess = input(f"Attempt {attempt + 1}: ").strip().lower()

        if len(guess) != 4 or len(set(guess)) != 4:
            print("Invalid guess. Make sure it is a 4-letter word.")
            continue

        feedback = provide_feedback(selected_word, guess)
        print(f"Feedback: {feedback}")

        guesses.append(guess)
        feedbacks.append(feedback)

        if feedback == "====":
            print("Congratulations! You've guessed the word correctly.")
            return

    # Use backtracking to find the word if the player has failed in 10 attempts
    print("Trying to solve with backtracking...")
    solution = backtrack(guesses, feedbacks, word_list)
    if solution:
        print(f"Backtracking found the word: {solution}")
    else:
        print(f"Sorry, you've used all your attempts. The correct word was: {selected_word}")


play_wordle()
