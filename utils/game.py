import random

class Hangman:
    def __init__(self):
        self.name = "Hangman game"
        # modified attributes
        self.word_to_find = None                # a list with the letters of the words
        self.correctly_guessed_letters = None   # a list with _ for each letter at start
        self.wrongly_guessed_letters = []       # a list to store wrongly guessed letters
                                                # not used... can be removed?
        self.turn_count = 0                     # to count the turns played
        self.error_count = 0                    # to count errors

    # the list of available words
    possible_words = ['becode', 'learning', 'mathematics', 'sessions', 'grizzly', 'bear', 'artificial', 'intelligence']
    # number of allowed turns
    lives = 5
    
    def select_a_word(self):
        """Selects a random word to be guessed from available list, 
            returns selected word in a list letter by letter,
            and a matching list with an underscore for each letter"""
        word = random.choice(self.possible_words)
        word_list = []
        cgl_list = []
        for l in word:
            word_list.append(l.upper())
            cgl_list.append("_")
        return word_list, cgl_list

    def play(self):
        """Asks player to enter a letter and returns it in upper case
            verifies that the input is indeed one single alphabetical character"""
        letter = ""
        while not letter.isalpha() or len(letter) != 1:
            letter = input("Please enter a letter (Only A to Z letters are allowed): ")
            if letter.upper() in self.wrongly_guessed_letters or letter.upper() in self.correctly_guessed_letters:
                print("Letter " + letter.upper() + " has be used before, pay attention!")
                letter = ""
        return letter.upper()

    def guess_word(self):
        right_guess = False
        keep_playing = False
        word_or_not = input("\t\tIf you know the word, tell us... (If not, press enter): ")
        if word_or_not == "":
            keep_playing = True
        else:
            if ''.join(self.word_to_find) == word_or_not.upper():
                right_guess = True
        return right_guess, keep_playing

    def game_over(self):
        """Terminates the game in case no lives left"""
        message = "Too BAD!!! No turns left... :( Game over..."
        print(message)

    def well_played(self):
        """Ends the game in case the word is guessed"""
        message = f"CONGRATS!!! You found the word: {''.join(self.word_to_find)} in {self.turn_count} turns with {self.error_count} errors!"
        print(message)

    def start_game(self):
        """This is the main method to manage a game instance"""
        # select a random word to play and add the word's data to the lists
        self.word_to_find, self.correctly_guessed_letters = self.select_a_word()
        print("Here is the word to be guessed: " + ' '.join(self.correctly_guessed_letters))
        any_letters_guessed = False     # at least one right guess?
        # ask player to guess a letter and/or the full word (runs 'lives' times or less)
        while self.turn_count < self.lives:
            right_guess = False     # guessed it right this turn?
            status_message = ""
            # request a letter
            letter = self.play()
            # check if the letter is in the word
            if letter in self.word_to_find:
                # update correctly_guessed letters
                for i in range(len(self.word_to_find)):
                    if self.word_to_find[i] == letter:
                        self.correctly_guessed_letters[i] = letter
                # check if the whole word is guessed
                if ''.join(self.word_to_find) == ''.join(self.correctly_guessed_letters):
                    self.well_played()
                    break
                else:
                    status_message = "\tYou guessed it RIGHT!\n\t"
                    right_guess = True
                    if any_letters_guessed == False:
                        any_letters_guessed = True
            else:
                # update wrongly_guessed_letters
                self.wrongly_guessed_letters.append(letter)
                self.error_count += 1
                status_message = "\tYou guessed it WRONG!\n\t"
            self.turn_count += 1
            # create and print status message
            if any_letters_guessed:
                status_message += "You guessed these letters correctly: "
            else:
                status_message += "You haven't guessed any letters correctly: "
            status_message += ' '.join(self.correctly_guessed_letters)
            status_message += "\n\t"
            status_message += "Wrongly guessed letters: "
            status_message += ", ".join(self.wrongly_guessed_letters)
            status_message += "\n\t"
            status_message += f"You used {self.turn_count} turns out of {self.lives}, and have {self.error_count} errors..."
            print(status_message)
            # if it was the right guess and some letters are guessed already, 
            # ask player if he wants to guess the whole word
            if right_guess and any_letters_guessed:
                correct_word, play_further = self.guess_word()
                if correct_word:
                    self.well_played()
                    break
                elif play_further:
                    continue
                else:
                    print("\t\tBAD GUESS!!!")
        else:
            # no turns left
            self.game_over()
