import random

# Word list
words = ["apple", "banana", "cherry", "date", "elderberry"]

def hangman():
    word = random.choice(words)
    word_length = len(word)
    display = ["_"] * word_length
    incorrect_guesses = 6
    guessed_letters = []

    print("Welcome to Hangman Challenge!")
    print("Guess a letter!")

    while incorrect_guesses > 0 and "_" in display:
        guess = input("Enter your guess: ").lower()

        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in guessed_letters:
            print("You already guessed this letter.")
        elif guess not in word:
            incorrect_guesses -= 1
            guessed_letters.append(guess)
            print(f"Incorrect! {incorrect_guesses} attempts remaining.")
        else:
            for i in range(word_length):
                if word[i] == guess:
                    display[i] = guess
            guessed_letters.append(guess)

        print(" ".join(display))
        print(f"Guessed letters: {', '.join(guessed_letters)}")

    if "_" not in display:
        print("Congratulations! You won!")
    else:
        print(f"Game over! The word was {word}.")

if __name__ == "__main__":
    hangman()




 