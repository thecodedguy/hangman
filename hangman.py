import random
wordList = ["aardvark", "baboon", "camel"]

#Choosing a random word from list
chosenWord = random.choice(wordList)
print(chosenWord)       #for testing

#Creating empty list
guessWord = ['_'] * len(chosenWord)

while ('_' in guessWord):

    guess = (input("Guess a letter: ")).lower()    #user input

    #Checking if the guessed word is in the chosenWord
    i = 0
    while i < len(chosenWord):
        if chosenWord[i] == guess:
            guessWord[i] = guess
        
        i += 1
    print(guessWord)





