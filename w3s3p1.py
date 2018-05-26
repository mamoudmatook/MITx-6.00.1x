def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
   
    # FILL IN YOUR CODE HERE...
    l =len(secretWord)
    for  i in range(l):
         if secretWord[i] not in lettersGuessed:
            return False
         
    
    return True 
