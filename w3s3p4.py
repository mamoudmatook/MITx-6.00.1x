def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    lettersGuessed=[]
     letterGuessed=''
    mistakesMade=0
    guessed=False
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print("-------------")
    while mistakesMade<8 and gussed=False:
        print('You have'+ 8-mistakesMade +'guesses left.')
	    print('Available letters: +' getAvailableLetters(lettersGuessed))
        letterGuessed = input(str("Please guess a letter: "))
        if letterGuessed in secretWord and not in lettersGussed:
            lettersGussed.append(letterGussed)
            print('Good guess: '+ getGuessedWord(secretWord,lettersGussed))
        elif letterGuessed in lettersGussed:
            print('Oops! You\'ve already guessed that letter: '+ getGuessedWord(secretWord,lettersGussed))
        else:
            print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord,lettersGussed))
            mistakesMade=mistakesMade+1
        print("-------------")
        
        if isWordGuessed(secretWord,lettersGusesed):
            print('Congratulations, you won!')
        elif mistakesMade==8:
            print('Sorry, you ran out of guesses. The word was else.')
            
        
            
    
    
    

