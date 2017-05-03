# This is a Guess the Number Game
# Python 2 version
import random

guessesTaken = 0

print 'Hello, what is your name?'
myName = raw_input()

number = random.randint(1,20)
print 'Well, ' + myName + ', I am thinking of a number between 1 and 20.'

for i in range(6):
    print 'Take a guess.'
    guess = raw_input()
    try:
        guess = int(guess)
    except:
        print guess + ' is not a valid entry.'
        continue
    guessesTaken += 1

    if guess < number:
        print 'Your guess is too low.'
    elif guess > number:
        print 'Your guess is too high.'
    elif guess == number:
        guessesTaken = str(guessesTaken)
        print 'Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!'
        quit()

number = str(number)
print 'Sorry, ' + myName + '. The number I was thinking of was ' + number + '.'