import random

def hangman():
    word = input("Enter a word: ")
    chosen_word = word
    guessed_letters = []
    tries = 5

    print("Welcome to Hangman!")
    print("The word contains", len(chosen_word), "letters.")
    print("_ " * len(chosen_word))

    while tries > 0:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        if guess not in chosen_word:
            tries -= 1
            print("Incorrect guess. You have", tries, "tries left.")
            if tries == 0:
                print("Sorry, you lost! The word was", chosen_word)
                break
        else:
            guessed_letters.append(guess)
            word_progress = ""
            for letter in chosen_word:
                if letter in guessed_letters:
                    word_progress += letter + " "
                else:
                    word_progress += "_ "
            print(word_progress)

            if "_" not in word_progress:
                print("Congratulations, you won!")
                break

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        hangman()
    else:
        print("Thanks for playing!")

hangman()
