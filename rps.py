# Rock Paper Scissors

print("Welcome to the Game: rock paper scissors")
print("Please input the option in small letters")

player1 = raw_input("Player 1:")    
while (player1 != "rock" and player1 != "paper" and player1 != "scissors"):
    print("This is not a valid object selection")
    print("Please try again!")
    player1 = raw_input("Player 1:")

player2 = raw_input("Player 2:")
while (player2 != "rock" and player2 != "paper" and player2 != "scissors"):
        print("This is not a valid object selection for Player 2")
        print("Please try again!")
        player2 = raw_input("Player 2:")
           
if player1 == "rock" and player2 == "paper":
    print("Player 2 wins")
elif player1 == "rock" and player2 == "scissors":
    print("Player 1 wins")
elif player1 == "paper" and player2 == "scissors":
    print("Player 2 wins")
elif player1 == "paper" and player2 == "rock":
    print("Player 1 wins")
elif player1 == "scissors" and player2 == "rock":
    print("Player 2 wins")
elif player1 == "scissors" and player2 == "paper":
    print("Player 1 wins")
else:
    print("Tie! Everybody wins!")

# exit()
    
