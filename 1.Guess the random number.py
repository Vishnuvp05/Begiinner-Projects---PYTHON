import random
def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess!=random_number:
        guess=int(input(f"Enter your guess number between 1 to {x}: "))
        if guess>random_number:
            print('Your guess is too high')
        elif guess<random_number:
            print("Your guess is too low")
    print("Your guess is correct")

guess(20)
