def hangman():
    import random
    #I am importing random to randomly choice any of the keywords below
    secretlist=["world", "apple", "soccer", "phone", "computer", "game", "gym", "water", "shoe", "home"]
    secret_word=random.choice(secretlist)
    #Here is my keywords and the secret word will pick from the secret list randomly
    multiguess = ''
    #this multiguess will be usefull later in the code
    amount = 10
    #the amount is 10 for the tries the user has

    print "Your input needs to be lowercase, one charcter,"
    print "and a letter or else your input will deduct a guess"
    #I wrote this because I couldnt 100% finish my code so I wrote this just to warn the user

    while amount > 0: #I have one set of function which the while loop until the amount(tries)=0
        lose = 0 #this is when the user losses
        for x in secret_word: #if the char is in secret word
            if x in multiguess: #the multiguess is for the spacing
                print x, # i print here with a comma so the letter is placed
            else:
                print "_",  #if it is not the dash will be stayed
                lose += 1
        if lose == 0:  #if player doesnt lose it will brint victory
            print "CONGRATS YOU WIN, THE WORD WAS " + secret_word.upper()
            break
        guess = input(" ~ Guess a character: ") #i start my code now with a ask of input
        if len(guess) != 1: #the rest will just tell the user if it is any of these and print why it is wrong
            print "Need to be one charcter" #also I couldnt use it correctly by commending
        elif guess==guess.upper():
            print "Needs to be lowercase" #lowercase
        multiguess += guess
        if guess not in secret_word:
            amount -= 1
            print "Incorrect You have", + amount, 'more guesses' #this will print if the users char is not in input
            if amount == 0:
                print "You Lose, The word was " + secret_word #this is where the user losses
hangman()
