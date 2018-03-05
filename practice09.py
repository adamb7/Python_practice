import random

nextgame = []
retry = 1

while nextgame != "exit":
    a=random.randint(1,9)
    b=int(input("Guess the number 1-9 :  "))
    while b != a:
        if(b > a):
            print("Given number is too high.")
            retry += 1
            b=int(input("Guess again:  "))
        if(b < a):
            print("Given number is too low.")
            retry += 1
            b=int(input("Guess again:  "))
    print("You guessed it right!")
    print("Number of tries: ", retry)
    retry = 1
    nextgame=input("Want to play again? (type exit if not)  ")
