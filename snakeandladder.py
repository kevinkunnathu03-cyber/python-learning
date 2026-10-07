import random
player1 = 0
player2 = 0
snake = {99: 54, 70: 55, 52: 42, 25: 2}
ladder = {6: 25, 11: 40, 17: 69, 46: 90}
while True:
    dice1 = random.randint(1, 6)
    input("player1 roll the dies")
    print("dice", dice1)

    if player1+dice1 <= 100:
        player1 += dice1
    if player1 in snake:
        print("snake")
        player1 = snake[player1]
    elif player1 in ladder:
        print("ladder")
        player1 = ladder[player1]
    if player1 == 100:
        print("wins the game")
        break
    print(player1)

    dice2 = random.randint(1, 6)
    input("player2 roll the dies")
    print("dice", dice1)
    if player2+dice2 <= 100:
        player2 += dice2
    if player2 in snake:
        print("snake")
        player2 = snake[player2]
    elif player2 in ladder:
        print("ladder")
        player2 = ladder[player2]
    if player2 == 100:
        print("win the game")
        break
    print(player2)
