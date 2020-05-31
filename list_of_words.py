import random


# Word list for Hangman game
class WordList():
    def __init__(self, target_file):
        self.target_file = target_file

    # Write new words
    def write_new_word(self):
        while True:
            with open(self.target_file, "a") as file_object:
                user_input = input("\nEnter a word for you list "
                                   "('quit' to exit): ").lower()
                if user_input != "quit":
                    file_object.write(user_input + "\n")
                else:
                    break

    # Read list
    def read_words(self):
        print("")
        try:
            with open(self.target_file, "r") as file_object:
                for line in file_object:
                    print("- " + line.strip())
        except FileNotFoundError:
            print("Try to write some words first!")

    # Erase list
    def erase_list(self):
        try:
            with open(self.target_file, "w") as file_object:
                file_object.write("")
                print("\nYour list was erased")
        except FileNotFoundError:
            print("Try to write some words first!")

    # Select a random word from the list
    def select_word(self):
        with open(self.target_file, "r") as file_object:
            lines = file_object.readlines()
        return lines[random.randint(0, len(lines) - 1)]

    # Check if list is empty
    def check_words(self):
        try:
            with open(self.target_file, "r") as file_object:
                lines = file_object.readlines()
                if len(lines) == 0:
                    return False
                elif len(lines) > 0:
                    return True
        except FileNotFoundError:
            return False
