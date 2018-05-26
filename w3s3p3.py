def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    l=len(lettersGuessed)
    ss=string.ascii_lowercase
    for i in range(l):
        if lettersGuessed[i] in ss:
            ss=ss.replace(lettersGuessed[i],'')
    
    return ss
