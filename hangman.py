#import random module
import random as rd

#make hangman pics
HANGMAN_PICS = ["""
 +---+
 O   |
     |
     |
    ===""", """
 +---+
 O   |
 |   |
     |
    ===""", """
 +---+
 O   |
/|   |
     |
    ===""", """
 +---+
 O   |
/|\  |
     |
    ===""", """
 +---+
 O   |
/|\  |
/    |
    ===""", """
 +---+
 O   |
/|\  |
/ \  |
    ==="""]

#create a list of words
words = ["fun", "owl", "jet", "poo", "gin",         
         "jazz", "duke", "lamb", "cosy", "zinc", 
         "grape", "multi", "phase", "quirk", "blaze", 
         "bishop", "bijoux", "hijack", "squash", "humble", 
         "bizzare", "strange", "jujutsu", "tobacco", "acquire", 
         "maximise", "pizzeria", "kamikaze", "junkfood", "chipmunk"]

#create a function to select a random items from the list 'words'
def random_word(word):
    words_index = rd.randint(0, len(word) - 1)
    return word[words_index]

def game_board(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print("Missing letters: ")
    for letters in missedLetters:
        print(letters)
    print()

    blanks = "_" * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter)
        print()
    
# Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.    
def user_guess(alreadyGuessed):
    while True:
        print("Guess a letter:")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("Please enter one letter.")
        elif guess in alreadyGuessed:
            print("You have already guessed this letter. Choose again.")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please enter a letter.")
        else:
            return guess

# This function returns True if the user would like to play again. If not it will return False.
def play_again():
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith("y")

#quick intro to the game
print("""---------------------------------------------------------------------
Good day user! You have landed yourself in a hangman game dimension.

            I will give you a word and you have 5 guesses!

                            GOOD LUCK!
---------------------------------------------------------------------   
""")

missedLetters = ""
correctLetters = ""
secretWord = random_word(words)
gameIsDone = False

while True:
    game_board(missedLetters, correctLetters, secretWord)

    #Let the player put in their guess
    guess = user_guess(missedLetters + correctLetters)

    #Determine if guess was correct or not
    if guess in secretWord:
        correctLetters = correctLetters + guess

        #check if player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print("Yee boi! The secret word is " + secretWord + "! You won!")
            gameIsDone = True

    else:
        missedLetters = missedLetters + guess

        #Check if player has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            game_board(missedLetters, correctLetters, secretWord)
            print("GAME OVER!\nAfter " + 
                  str(len(missedLetters)) + " missed guess(es) and " +
                  str(len(correctLetters)) + " correct guess(es), the word was '"
                  + secretWord + "'" )
            gameIsDone = True

# Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if play_again():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = random_word(words)
        else:
            break





    











    


