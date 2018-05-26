def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    l=len(secretWord)
    ll=''
    for i in range(l):
        if secretWord[i] in lettersGuessed:
            ll=ll+secretWord[i]
            
        else:
            ll=ll+'_'
            ll=ll+' '
    #print('\''+ll+'\'')
    return ll
