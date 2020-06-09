from random import randint
import sys
answer = randint(int(sys.argv[1]), int(sys.argv[2]))


while True:
    try:
        guess = int(input('guess a number between 1 and 10:  '))

        if 0 < guess < 11:
            if guess == answer:
                print('you won')
                break
            else:
                print('sorry bro')
                continue
        else:
            print('hey, I told between 1 and 10')
            continue
    except ValueError:
        print('enter a number')
        continue
