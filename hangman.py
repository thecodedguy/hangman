import random
wordList = ["aardvark", "baboon", "camel"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#Choosing a random word from list
chosenWord = random.choice(wordList)
print(chosenWord)       #for testing

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
        print(f"\nWrong Choice!!\nLives left: {lives}\n" + stages[lives])
    print(f"{' '.join(guessWord)}")
    

if lives == 0:
    print("You lose")

if '_' not in guessWord:
    print("You Win")




