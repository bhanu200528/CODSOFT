import random , sys

print("ROCK , PAPER  , SCISSOR")
win = 0
loss = 0
tie = 0

while True :
    print("%s Wins , %s Losses , %s Ties \n" %(win , loss , tie))
    while True :
        print("Enter your move : (R)ock , (P)aper , (S)cissor or (Q)uit ")
        player_move = input()
        if player_move == 'q':
            sys.exit()
        if player_move == 'r' or player_move == 'p' or player_move == 's' :
            break
        print("Enter one of these : r , p , s or q")

    if player_move == 'r':
        print("Rock versus . . .")
    elif player_move == 'p':
        print("Paper versus . . .")
    elif player_move == 's':
        print("Scissor versus . . .")
    random_num = random.randint(1,3)
    if random_num == 1 :
        com_move = 'r'
        print('Rock')
    elif random_num == 2:
        com_move = 'p'
        print("Paper")
    elif random_num == 3:
        com_move = 's'
        print("Scissor")
    
    if player_move == com_move :
        print("It is tie ")
        tie = tie + 1
    elif player_move == 'r' and com_move == 's' :
        print("You won")
        win = win + 1
    elif player_move == 'p' and com_move == 'r' :
        print("You won")
        win = win + 1
    elif player_move == 's' and com_move == 'p' :
        print("You won")
        win = win + 1
    elif com_move == 'r' and player_move == 's' :
        print("You loss")
        loss = loss + 1
    elif com_move == 'p' and player_move == 'r' :
        print("You loss")
        loss = loss + 1
    elif com_move == 's' and player_move == 'p' :
        print("You loss")
        loss = loss + 1