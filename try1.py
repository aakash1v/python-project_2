import random

max_guesses =10
digit_length = 3

def getSecretNumber():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretno = ''
    for i in range(digit_length):
        secretno +=str(numbers[i])

    return secretno
def main():
    print("""I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say: That means:
    Pico        One digit is correct but in the wrong position.
    Fermi       One digit is correct and in the right position.
    Bagels      No digit is correct.""")

    while True: #main loop
        secretnumber= getSecretNumber()
        print('I have thought up a number.')
        print(' You have {} guesses to get it.'.format(max_guesses))
        guessno = 1

        while(guessno<=max_guesses):
            guess = ''
            while len(guess) != digit_length or not guess.isdecimal():
                print("Guess #{}:".format(guessno))
                guess= input("<")

            clues = getClues(guess,secretnumber)
            print(clues)
            guessno +=1

            if guess == secretnumber:
                print("Congratulation you win!..")
                break
            if (guessno >max_guesses):
                print("YOu are runout of guesses..")
                print("The correct number was {}".format(secretnumber))

        #Ask player if he want to play again..
        print("Do you want to play again (yes/no)")
        if not input('>').lower().startswith('y'):
            break
    print("Thank you for playing....")




def getClues(guess,secretno):
    clues = []
    for i in range(len(secretno)):
        if guess[i] == secretno[i]:
            clues.append("Femi")
        elif guess[i] in secretno:
            clues.append("Pico")
    if len(clues) ==0:
        return "Bangles"
    else:
        clues.sort()
        return ''.join(clues)



# If the program is run (instead of imported), run the game:
if __name__ == "__main__":
    main()
            
