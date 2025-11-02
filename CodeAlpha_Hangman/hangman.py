


import random
import string

WORDS = ["python", "hangman", "developer", "dataset", "algorithm"]
MAX_WRONG = 6

HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ==="""
]

def choose_word():
    return random.choice(WORDS)

def display_state(word, guessed_letters, wrong_guesses):
    displayed = " ".join(c if c in guessed_letters else "_" for c in word)
    print(HANGMAN_PICS[wrong_guesses])
    print(f"Word: {displayed}")
    print(f"Guessed: {', '.join(sorted(guessed_letters)) if guessed_letters else '(none)'}")
    print(f"Wrong guesses left: {MAX_WRONG - wrong_guesses}")
    print()

def get_guess(already_guessed):
    while True:
        guess = input("Enter a letter (or full word to guess): ").strip().lower()
        if not guess:
            print("Type something. Anything. A letter, maybe.")
            continue
        if len(guess) == 1:
            if guess not in string.ascii_lowercase:
                print("Only letters a-z. Try again.")
            elif guess in already_guessed:
                print("You already guessed that letter. Try another.")
            else:
                return guess
        else:
            # allow full-word guesses
            if all(ch in string.ascii_lowercase for ch in guess):
                return guess
            else:
                print("Full-word guesses must be letters only. Try again.")

def play():
    word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0

    print("Welcome to Hangman! Guess the word letter by letter or try the whole word.")
    while wrong_guesses < MAX_WRONG:
        display_state(word, guessed_letters, wrong_guesses)
        guess = get_guess(guessed_letters)

        if len(guess) == 1:
            if guess in word:
                guessed_letters.add(guess)
                print(f"Nice — '{guess}' is in the word.")
                # check win
                if all(c in guessed_letters for c in word):
                    print()
                    print("Congratulations — you guessed the word!")
                    print(f"The word was: {word}")
                    break
            else:
                wrong_guesses += 1
                print(f"Sorry — '{guess}' is not in the word.")
        else:
            # full-word guess
            if guess == word:
                print()
                print("Amazing. You guessed the whole word correctly!")
                print(f"The word was: {word}")
                break
            else:
                wrong_guesses += 1
                print(f"Wrong word guess. That's costly.")

    else:
        # loop exhausted: player lost
        display_state(word, guessed_letters, wrong_guesses)
        print("Game over. You were hanged.")
        print(f"The word was: {word}")

def main():
    while True:
        play()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if not again or again[0] != "y":
            print("Thanks for playing. Now go push some code (and do 50 push-ups).")
            break

if __name__ == "__main__":
    main()
