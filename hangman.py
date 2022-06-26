import random
import ASCII
import words

print(ASCII.logo)

#Choosing a random word from list
chosenWord = random.choice(words.wordList)
#print(chosenWord)       #for testing

#Creating empty list
guessWord = ['_'] * len(chosenWord)
lives = 6       #lives of user

while ('_' in guessWord and lives != 0):

    guess = (input("Guess a letter: ")).lower()    #user input

    #Checking if the guessed word is in the chosenWord
    i = 0
    flag = False
    while i < len(chosenWord):
        if chosenWord[i] == guess:
            guessWord[i] = guess
            flag = True
        i += 1
    if flag != True:
        lives -= 1
        print("\n\nWrong Guess!!")
    else:
        print("\n\nCorrect Guess!!")
    print(f"\nLives left: {lives}\n" + ASCII.stages[lives])
    print(f"\nWord: {' '.join(guessWord)}\n")
    

if lives == 0:
    print(f"You Lose :(\n\nCorrect word was: {chosenWord}\n\n\n")

if '_' not in guessWord:
    print("You Win !!!\n")




