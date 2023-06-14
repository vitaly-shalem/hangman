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

    possible_words = ['becode', 'learning', 'mathematics', 'sessions']  # the list of available words
    lives = 5                                                           # number of allowed turns
    
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
        """Asks player to enter a letter and returns it in upper case"""
        letter = input("Please enter a letter (Only A to Z letters are allowed): ")
        return letter.upper()

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
        # select a word to play and initiate the words lists
        self.word_to_find, self.correctly_guessed_letters = self.select_a_word()
        print("Here is the words to be guessed: " + ' '.join(self.correctly_guessed_letters))
        ask_the_word = False    # changed to True after 1st correct letter
                                # used to ask player to guess the whole word
        # request letters and process the responces, runs 'lives' times or less
        while self.turn_count < self.lives:
            status_message = ""
            # if at least one letter guessed, ask if player wantes to guess the whole word
            if ask_the_word:
                guess_or_not = input("If you know the word, tell us... If not, press enter, and keep playing: ")
                if guess_or_not != "":
                    if ''.join(self.word_to_find) == guess_or_not.upper():
                        self.well_played()
                        break
                    else:
                        print("WRONG!!! Keep playing...")
            # request a lettr
            letter = self.play()
            if not letter.isalpha():
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
                    if not ask_the_word: ask_the_word = True
            else:
                # update wrongly_guessed_letters
                self.wrongly_guessed_letters.append(letter)
                self.error_count += 1
                status_message = "\tYou guessed it WRONG!\n\t"
            self.turn_count += 1
            # print status
            if ask_the_word:
                status_message += "You guessed these letters correctly: "
            else:
                status_message += "You haven't guessed any letters correctly: "
            status_message += ' '.join(self.correctly_guessed_letters)
            status_message += "\n\t"
            status_message += "Wrongly guessed letters: "
            status_message += ", ".join(self.wrongly_guessed_letters)
            status_message += "\n\t"
            status_message += f"You used {self.turn_count} turns out of {self.lives}, and have {self.error_count} errors... Keep playing..."
            print(status_message)
        else:
            # no turns left
            self.game_over()
        