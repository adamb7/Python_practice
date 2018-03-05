newgame = "y"


while newgame is "y":

    player = input("Player1 choose rock,paper,scissors:  ")
    while (player != "rock") and (player != "paper") and (player != "scissors"):
        player = input("Player1 choose rock,paper,scissors:  ")
    player2 = input("Player2 choose rock,paper,scissors:  ")
    while (player2 != "rock") and (player2 != "paper") and (player2 != "scissors"):
        player2 = input("Player1 choose rock,paper,scissors:  ")

    if(player == player2):
        print("Tie!")

    elif(player == "rock" and player2 == "scissors") or (player == "paper" and player2 == "rock") or (player == "scissors" and player2 == "paper"):
        print("Player1 wins!")
    else:
        print("Player2 wins!")

    newgame=input("Do you want to start a new game? (y/n)  ")
