print("\t\tTIC TAC TOE")

first_player = str(input("input the name of first player: "))
second_player = str(input("input the name of second player: "))

print(f"Hi {first_player} and {second_player}, you guys are now enemies.")

first_initial = input(first_player+" choose X or O: ").upper()
second_initial = ""
while first_initial == "X" or "O":
    if first_initial == "X":
        second_initial = "O"
        break
    elif first_initial == "O":
        second_initial = "X"
        break
    else:
        print("give only X or O")
        first_initial = input(first_player+" choose X or O: ").upper()
        continue

box_inputs = [" ", " ", " ", " ", " "," "," "," "," "]

def box_update(box_inputs):
    box = (f"""
                  {box_inputs[0]}   |   {box_inputs[1]}   |   {box_inputs[2]}
                 -------------------
                  {box_inputs[3]}   |   {box_inputs[4]}   |   {box_inputs[5]}
                 -------------------
                  {box_inputs[6]}   |   {box_inputs[7]}   |   {box_inputs[8]}
    """)
    print(box)

def peepoo():
    babushka=0
    box_update(box_inputs)

    player = "X"

    for num in range(10):

        player_input=int(input(f"please make your move {player}: "))

        if box_inputs[player_input] == " ":
            if player == first_initial:
                symbol=first_initial
            else:
                symbol=second_initial
            box_inputs[player_input]=symbol
            box_update(box_inputs)

            if player == "X":
                player = "O"

            else:
                player = "X"

            babushka+=1


        else:
            print("this place is already taken")
            continue


        if babushka>=5:

            if box_inputs[0]==box_inputs[1]==box_inputs[2]:

                if box_inputs[0]=="X":
                    print("GAME OVER <3")
                    if first_initial=="X":
                        print(f"{first_player} wins.")
                    else:
                        print(f"{second_player} wins.")
                    break

                elif box_inputs[0] == "O":
                    print("GAME OVER <3")
                    if first_initial=="O":
                        print(f"{first_player} wins.")
                    else:
                        print(f"{second_player} wins.")
                    break

            elif box_inputs[3]==box_inputs[4]==box_inputs[5]:

                if box_inputs[3] == "X":
                    print("GAME OVER <3")
                    if first_initial == "X":
                        print(f"{first_player} wins.")
                    else:
                        print(f"{second_player} wins.")
                    break

                elif box_inputs[3] == "O":
                    print("GAME OVER <3")
                    if first_initial == "O":
                        print(f"{first_player} wins.")
                    else:
                        print(f"{second_player} wins.")
                    break

            elif box_inputs[6]==box_inputs[7]==box_inputs[8]:

                if box_inputs[6] == "X":
                    print("GAME OVER <3")
                    if first_initial == "X":
                        print(f"{first_player} wins.")
                    else:
                        print(f"{second_player} wins.")
                    break

                elif box_inputs[6] == "O":
                    print("GAME OVER <3")
                    if first_initial == "O":
                        print(f"{first_player} wins.")
                    else:
                        print(f"{second_player} wins.")
                    break

            elif box_inputs[0]==box_inputs[3]==box_inputs[6]:

                if box_inputs[0] == "X":
                    print("GAME OVER <3")
                    if first_initial == "X":
                        print(f"{first_player} wins.")
                    else:
                        print(f"{second_player} wins.")
                    break

                elif box_inputs[0] == "O":
                    print("GAME OVER <3")
                    if first_initial == "O":
                        print(f"{first_player} wins.")
                    else:
                        print(f"{second_player} wins.")
                    break

            elif box_inputs[1]==box_inputs[4]==box_inputs[7]:

                if box_inputs[1] == "X":
                    print("GAME OVER <3")
                    if first_initial == "X":
                        print(f"{first_player} wins.")
                    else:
                        print(f"{second_player} wins.")
                    break

                elif box_inputs[1] == "O":
                    print("GAME OVER <3")
                    if first_initial == "O":
                        print(f"{first_player} wins.")
                    else:
                        print(f"{second_player} wins.")
                    break

            elif box_inputs[2]==box_inputs[5]==box_inputs[8]:

                if box_inputs[2] == "X":
                    print("GAME OVER <3")
                    if first_initial == "X":
                        print(f"{first_player} wins.")
                    else:
                        print(f"{second_player} wins.")
                    break

                elif box_inputs[2] == "O":
                    print("GAME OVER <3")
                    if first_initial == "O":
                        print(f"{first_player} wins.")
                    else:
                        print(f"{second_player} wins.")
                    break

            elif box_inputs[0] == box_inputs[4] == box_inputs[8]:

                if box_inputs[0] == "X":
                    print("GAME OVER <3")
                    if first_initial == "X":
                        print(f"{first_player} wins.")
                    else:
                        print(f"{second_player} wins.")
                    break

                elif box_inputs[0] == "O":
                    print("GAME OVER <3")
                    if first_initial == "O":
                        print(f"{first_player} wins.")
                    else:
                        print(f"{second_player} wins.")
                    break

            elif box_inputs[2] == box_inputs[4] == box_inputs[6]:

                if box_inputs[2] == "X":
                    print("GAME OVER <3")
                    if first_initial == "X":
                        print(f"{first_player} wins.")
                    else:
                        print(f"{second_player} wins.")
                    break

                elif box_inputs[2] == "O":
                    print("GAME OVER <3")
                    if first_initial == "O":
                        print(f"{first_player} wins.")
                    else:
                        print(f"{second_player} wins.")
                    break
        if babushka == 9:
            print("TIE....")
            break

peepoo()

play_again = str(input("Do you wanna play again?: ").lower().strip())
while True:

    if play_again == "yes":
        box_inputs = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        peepoo()
        play_again = str(input("Do you wanna play again?: ").lower().strip())
        continue

    if play_again == "no":
        print("thanks for playing uwu")
        break

    else:
        print("user input not clear")
        play_again = str(input("Do you wanna play again?: ").lower().strip())
        continue