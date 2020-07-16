user_input = list("          ")


print("""
---------
| """ + user_input[0] + " " + user_input[1] + " " + user_input[2] + " |")
print("| " + user_input[3] + " " + user_input[4] + " " + user_input[5] + " |")
print("| " + user_input[6] + " " + user_input[7] + " " + user_input[8] + " |")
print("---------")

field = [[user_input[0], user_input[1], user_input[2]],
         [user_input[3], user_input[4], user_input[5]],
         [user_input[6], user_input[7], user_input[8]]]


# implement user movement starts here 

valid_symbols = {1, 2, 3, " "}

game_state = "Game not finished"
while game_state == "Game not finished" :

    turn = 1
    err = 0

    while turn != 0:
        movement_input = input()


        for char in movement_input:
            if not char.isdigit() and char != " ":
                print("You should enter numbers!")


        user_movement_x, user_movement_y = movement_input.split(" ") #implement error handling if more than 2 coordinates are entered!

        user_movement_x = int(user_movement_x)
        user_movement_y = int(user_movement_y)

        if user_movement_x > 3 or user_movement_y > 3:
            print("Coordinates should be from 1 to 3!")
        else:

            if field[3 - user_movement_y][user_movement_x -1] != " ":
                print("This cell is occupied! Choose another one!")
            else:
                field[3 - user_movement_y][user_movement_x -1] = "X"
                turn = 0

    print("""
---------
| """ + field[0][0] + " " + field[0][1] + " " + field[0][2] + " |")
    print("| " + field[1][0] + " " + field[1][1] + " " + field[1][2] + " |")
    print("| " + field[2][0] + " " + field[2][1] + " " + field[2][2] + " |")
    print("---------")


    countX = 0
    countO = 0
    count_empty = 0
    winner = ""
    impossible = 0


    # check amount of X, O and blank
    for check in field:
        if check == "X":
            countX = countX + 1
        elif check == "O":
            countO = countO + 1
        else:
            count_empty = count_empty + 1

    for y in range(len(field)):
        if field[y][0] == field [y][1] and field[y][1] == field[y][2] and field[y][1] != " ":
            if winner != "":
                impossible = 1

            winner = field[y][0]


        elif field[0][y] == field[1][y] and field [1][y] == field[2][y] and field[1][y] != " ":
            if winner != "":
                impossible = 1

            winner = field[0][y]

    if field[0][0] == field[1][1] and field[1][1] == field[2][2] and field[0][0] != " ":
        if winner != "":
            impossible = 1

        winner = field[2][2]
    elif field[0][2] == field [1][1] and field [1][1] == field[2][0] and field[0][2] != " ":
            if winner != "":
                impossible = 1

            winner = field[1][1]


    if winner != "" and impossible == 0:
        game_state = (winner + " wins")
    elif impossible == 1 or (countX > countO + 1) or (countO > countX + 1):
        game_state = "Impossible"
    elif count_empty > 0:
        game_state = ("Game not finished")
    elif count_empty == 0:
        game_state = "Draw"


print(game_state)




