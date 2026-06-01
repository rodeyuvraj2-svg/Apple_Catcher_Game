def clear():
    os.system("cls")

def board():
    clear()

    print("-------------------Game-----------------------------")
    print("\nScore: ",score)
    for i in range(board_size):
        for j in range(board_size):
            if i == player_x and j == player_y:
                print(character[0], end=" ")
            elif i == apple_x and j == apple_y:
                print(apple[0], end=" ")
            else:
                print("- ", end=" ")
        print()
    
def place_apple():
    global apple_x, apple_y

    while True:
        apple_x = random.randint(0,9)
        apple_y = random.randint(0,9)

        if player_x != apple_x or player_y != apple_y:
            break

def auto_play():
    global player_x,player_y

    if player_x > apple_x:
        player_x -= 1
    elif player_x < apple_x:
        player_x += 1
    elif player_y > apple_y:
        player_y -= 1
    elif player_y < apple_y:
        player_y += 1
    else:
        if player_x >9:
            player_x-=1
        else:
            player_x+=1

import random
import os
import time

board_size = 10

player_x = 0
player_y = 0

characters = ["👨","🐰","🐋","🦁"]
character = "👨"
apple = ["🍎"]

score = 0

apple_x = random.randint(0,9)
apple_y = random.randint(0,9)


while True:
    clear()
    print("1. Play\n2. Select Character\n3. Exit")
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        score = 0
        while True:
            board()
            print("Press 't' for exit")
            print("Press 'auto' for Automatically play game")
            move = input("Move: ")

            if player_x == apple_x and player_y == apple_y:
                score += 1
                place_apple()
            
            if move == "w" and player_x > 0:
                player_x -= 1
            elif move == "s" and player_x < 9:
                player_x += 1
            elif move == "a" and player_y > 0:
                player_y -= 1
            elif move == "d" and player_y < 9:
                player_y += 1
            elif move == "auto":
                ticks = int(input("Enter Number of Ticks: "))
                while True:
                    if ticks == 0:
                        break
                    
                    board()
                    print("Press 't' for exit")
                    print("Press 'auto' for Automatically play game")
                    if player_x == apple_x and player_y == apple_y:
                        score += 1
                        place_apple()

                    auto_play()
                    ticks -= 1

                    time.sleep(0.1)
            elif move =="t":
                break
        
    elif ch == 2:
        for i in range(len(characters)):
            print(i+1," ", characters[i])
        ch = int(input("Enter Number :"))

        if ch == 1 :
            character = characters[0]
        elif ch == 2 :
            character = characters[1]
        elif ch == 3 :
            character = characters[2]   
        elif ch == 4 :
            character = characters[3]
        else:
            print("Enter Valid Choice")
            continue

    elif ch == 3:
        print("Thank You for Visiting.")
        break

    else:
        print("Enter Valid Choice")