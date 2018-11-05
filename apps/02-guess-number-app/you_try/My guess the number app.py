import random

print('-----------------------------')
print('----Guess the Number App-----')
print('-----------------------------')
print()

isspecial_number = random.randint(0, 100)

guess = -1

while guess != isspecial_number:

    guess = int(input("guess the number you tatti! "))

    print("This is your guess and its type: ", end='')
    print(guess, type(guess))

    if guess < isspecial_number:
        print('but it\'s too low tatti')
    elif guess > isspecial_number:
        print('but it\'s too high tatti')
    else:
        print('and, you are the TATTI')


