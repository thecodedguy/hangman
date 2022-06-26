import random
wordList = ["aardvark", "baboon", "camel"]

#Choosing a random word from list
chosenWord = random.choice(wordList)
print(chosenWord)       #for testing
guess = (input("Guess a letter?: ")).lower()    #user input

#Checking if the guessed word is in the chosenWord
for char in chosenWord:
    if guess == char:
        print("Yes")
    else:
        print("No")



