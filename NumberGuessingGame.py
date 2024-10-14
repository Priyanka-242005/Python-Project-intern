import random

def generate_random_number(start=1, end=100):
    return random.randint(start, end)


def get_player_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            return guess
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def check_guess(guess, correct_number):
    if guess < correct_number:
        return "Too low!"
    elif guess > correct_number:
        return "Too high!"
    else:
        return "Correct!"


def play_game():
    random_number = generate_random_number()
    attempts = 10
    print("Welcome to the 'Guess the Number' game!")
    print(f"I have picked a number between 1 and 100. You have {attempts} attempts to guess it.")

    while attempts > 0:
        guess = get_player_guess()
        result = check_guess(guess, random_number)
        
        if result == "Correct!":
            print(result)
            print(f"Congratulations! You guessed the number in {10 - attempts + 1} attempts.")
            break
        else:
            attempts -= 1
            print(f"{result} You have {attempts} attempts remaining.")
        
        if attempts == 0:
            print(f"Game Over! The number was {random_number}.")


play_game()



o/p:-C:\Users\LENOVO\Desktop\PythonProject intern>py NumberGuessingGame.py
Welcome to the 'Guess the Number' game!
I have picked a number between 1 and 100. You have 10 attempts to guess it.
Enter your guess: 76
Too high! You have 9 attempts remaining.
Enter your guess: 89
Too high! You have 8 attempts remaining.
Enter your guess: 3
Too low! You have 7 attempts remaining.
Enter your guess: 78
Too high! You have 6 attempts remaining.
Enter your guess: