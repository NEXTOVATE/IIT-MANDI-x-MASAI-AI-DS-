# Rules of the "Rock, Paper, Scissors" game are:

# Rock beats Scissors,
# Scissors beat Paper,
# Paper beats Rock,
# Two identical moves are a draw.
# Let's play! You will be given valid moves of two Rock, Paper, Scissors players, and have to return which player won: "Player 1 won!" for player 1, and "Player 2 won!" for player 2. In case of a draw return Draw!.

# Examples:
# "scissors",     "paper"     --> "Player 1 won!"
# "scissors",     "rock"      --> "Player 2 won!"
# "paper",        "paper"     --> "Draw!"

print("Welcome to rock paper seicssors game.")
p1 = input("Player 1 Enter your choice :")
p2 = input("Player 2 Enter your choice :")

print(f"Player 1 choosed {p1} and Player 2 choosed {p2}")

if p1 == p2 :
    print("Draw!")
else:
    if p1 == "rock" and p2 == "paper":
        print("Player 2 win!")
    elif p1 == "rock" and p2 == "scissors":
        print("Player 1 win!")
    elif p1 == "paper" and p2 == "rock":
        print("Player 1 win!")
    elif p1 == "paper" and p2 == "scissors":
        print("Player 2 win!")
    elif p1 == "scissors" and p2 == "rock":
        print("Player 2 win!")
    else:
        print("Player 1 win!")

