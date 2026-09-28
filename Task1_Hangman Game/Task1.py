import random

# List of 5 predefined words
words = ["python", "computer", "program", "keyboard", "developer"]

# Randomly select a word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
incorrect_guesses = 6

print("================================")
print("       WELCOME TO HANGMAN")
print("================================")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.\n")

# Main game loop
while incorrect_guesses > 0:

    # Display the word with guessed letters
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print("Incorrect guesses left:", incorrect_guesses)

    # Check if player has guessed the complete word
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 Congratulations!")
        print("You guessed the word:", word)
        break

    # Get user's guess
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.\n")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter. Try another one.\n")
        continue

    # Add guess to guessed letters
    guessed_letters.append(guess)

    # Check whether guess is correct
    if guess in word:
        print("✓ Correct guess!\n")
    else:
        incorrect_guesses -= 1
        print("✗ Wrong guess!\n")

# If player runs out of guesses
if incorrect_guesses == 0:
    print("\n================================")
    print("           GAME OVER")
    print("================================")
    print("The word was:", word)