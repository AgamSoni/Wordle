import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "cherry"] #this list can be changed to a function that pulls random words from the dictionary using wonderwords
    return random.choice(words)

def display_word(word, guessed_letters):
    return ''.join(letter if letter in guessed_letters else '*' for letter in word)

def wordle():
    max_attempts = 6
    secret_word = choose_word()
    guessed_letters = set()

    print("Welcome to Wordle!")
    print("Try to guess the secret word.")
    print(display_word(secret_word, guessed_letters))

    for attempt in range(max_attempts):
        guess = input("Enter your guess: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        guessed_letters.add(guess)

        display = display_word(secret_word, guessed_letters)
        print(display)

        if display == secret_word:
            print(f"Congratulations! You guessed the word: {secret_word}")
            break
        else:
            print(f"Incorrect guesses: {max_attempts - attempt - 1} attempts remaining")

    else:
        print(f"Sorry, you've run out of attempts. The word was: {secret_word}")

if __name__ == "__main__":
    wordle()
