import random
import string


def generate_password(length, use_uppercase, use_numbers, use_symbols):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Secure Password Generator")
    length = int(input("Enter password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    
    password = generate_password(length, use_uppercase, use_numbers, use_symbols)
    print("Generated Password:", password)
    
    copy_to_clipboard = input("Copy to clipboard? (y/n): ").lower() == 'y'
    if copy_to_clipboard:
        pyperclip.copy(password)
        print("Password copied to clipboard.")


if __name__ == "__main__":
    main()



o/p:-C:\Users\LENOVO\Desktop\PythonProject intern>py RandomPasswordGenerator.py
Secure Password Generator
Enter password length: 7
Include uppercase letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): y
Generated Password: E,e!;p9
Copy to clipboard? (y/n): n