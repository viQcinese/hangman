from list_of_words import WordList

# Introduction and preparations
my_word_list = WordList("word_list.txt")
print("\n***** HANGMAN *****")


# Present a Menu in a Loop
def main_menu():

    # <list> <play> or <quit>
    while True:
        user_input1 = input("\nEnter <list> to check and upgrade your list "
                            "of words\n"
                            "Enter <play> to play the game\n"
                            "Enter <quit> to exit the game\n\n")

        # <list> Read, Write or Erase the list of words
        if user_input1 == "list":
            user_input = input("\nEnter <read> to check your word list\n"
                               "Enter <write> to add new words to your list\n"
                               "Enter <erase> to erase your list of words\n\n")
            if user_input == "read":
                my_word_list.read_words()
            if user_input == "write":
                my_word_list.write_new_word()
            if user_input == "erase":
                my_word_list.erase_list()

        # <play> Call play function
        elif user_input1 == "play":

            # Check if there are words in the list before
            if my_word_list.check_words() is False:
                print("\nYou have to enter some words in the list first!")
                continue
            elif my_word_list.check_words() is True:
                play()

        # <quit> Terminate application
        elif user_input1 == "quit":
            break


# Simulate round of hangman
def play():

    # Prepares 2 lists of letters
    chosen_word = list(my_word_list.select_word())
    if "\n" in chosen_word:
        chosen_word.remove("\n")
    hidden_word = ["-" for letter in chosen_word]
    attempts = 5
    used_letters = []

    # Display round information
    while True:
        print("")
        print("Word: ", end="")
        for letter in hidden_word:
            print(letter, end="")
        print("\nAttempts: " + str(attempts))
        print("Guesses: ", end="")
        for letter in used_letters:
            print(letter, end=" ")

        # Check if already Win/Loose
        if attempts == 0:
            print("\nYou loose!\n")
            break
        win = True
        for position, letter in enumerate(hidden_word):
            if letter == "-":
                win = False
        if win:
            print("\n\nYou WIN!\n")
            break

        # Prompt guess and check if is a single letter
        while True:
            user_guess = input("\n\nEnter a letter: ").lower()
            if len(user_guess) > 1:
                print("\nYou must enter a single letter!")
                continue
            elif len(user_guess) == 1:
                break

        # Check if user guessed right
        used_letters.append(user_guess)
        guess_value = False
        for position, letter in enumerate(chosen_word):
            if user_guess == letter:
                hidden_word[position] = letter
                guess_value = True

        if guess_value is False:
            attempts += -1


main_menu()
