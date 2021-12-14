import random

# variables used in the Game.
winner = (6, 6)
message = ["Congratulation, you win!", "Oh, try again later."]
i = 1

# loop for the Dice simulation
while i > 0:
    # Player 1 section
    player1 = input("Player1 (press P): ")
    player1 = player1.upper()
    if player1 == "P":
        reco1 = random.randint(1, 6)
        reco2 = random.randint(1, 6)
        result = reco1, reco2
        print(result)
        if result == (6, 6):
            print(message[0])
            break
        else:
            print(message[1])

    # Player 2 section
    player2 = input("Player2 (press P): ")
    player2 = player2.upper()
    if player1 == "P":
        reco1 = random.randint(1, 6)
        reco2 = random.randint(1, 6)
        result = reco1, reco2
        print(result)
        if result == (6, 6):
            print(message[0])
            break
        else:
            print(message[1])

