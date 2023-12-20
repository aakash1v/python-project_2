import random

Num_digits = 2
Max_guesses = 5

def main():
    print("Bangles , a detective logic game.")
    print("By Al, Sweigart al@inventwithpython.com\n")
    print("I am thinking of a 10 digit number. Try to guess what is it.")
    print("Here are some clew -")
    print("\tWhen i say:        what it's mean:")
    print("\tPico         One digit is correct but in wrong place")
    print("\tFemi         One digit is correct and in right place")
    print("\tBangles      No digit is correct")

    while True: #main game loop.
        secretNum = getSecretNum()
        print('I have thought up a number. ')
        print('You have {} guesses to get it.'.format(Max_guesses))
        
        numGuesses =1

        while numGuesses <= Max_guesses:
            guess = ''
            #     keep looping  until they enter a valid guess:
            while len(guess) != Num_digits or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('>')
                
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses +=1
            
            if guess == secretNum:
                break #They're correct , so break out of this loop.
            if numGuesses > Max_guesses:
                print('You ran out of guesses')
                print('The answer was {}.'.format(secretNum))
                
        #Ask player if they want to play again
        print('Do you want to play again? (yes or no)')
        if not input('>').lower().startswith('y'):
                     break
                    
    print('Thanks for playing !')
    
def getSecretNum():
    """Returns a sting made up of Num_digits unique random digits."""
    numbers = list('0123456789')   #Create a list of digits 0-9
    random.shuffle(numbers) # shuffle them into random order.
    
    #Get the first Num_digits digits in the list for the secret number:
    secretNum = ''
    for i in range(Num_digits):
        secretNum +=str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    """Returns a string with the Pico, fermi, bagels clues for a guess and secret number pair."""
    if guess ==secretNum:
        return 'you got it!'
    
    clues = []
    
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            #A correct digit is in the correct place.
            clues.append('Fermi')
        elif guess[i] in secretNum:
            #A correct digit is in the incorrect place.
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bangles' #There are no correct digits at all.
    else:
        #sort the clues into alphetical order so their original order
        #doesn't give information away.
        clues.sort()
        #Make a single string from the list of string clues.
        return ''.join(clues)

#if the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()

    
    
            
        
