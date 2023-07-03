print("Tic-Tac-Toe")
active_game = True
actual_player = 'X'
# create field as list
field = [" ",
             "1","2","3",
             "4","5","6",
             "7","8","9"]
# output field
def field_output():
    print (field[1] + "|" + field[2] + "|" + field[3] )
    print (field[4] + "|" + field[5] + "|" + field[6] )
    print (field[7] + "|" + field[8] + "|" + field[9] )
# game input and input control
def player_input():
    global active_game
    while True:
        movement = input("Enter field: ")
        # premature end of game by player
        if movement == 'q':
            active_game = False
            return
        try:
            movement = int(movement)
        except ValueError:
            print("Enter number between 1 and 9")
        else:
            if movement >= 1 and movement <= 9:
                if field[movement] == 'X' or field[movement] == 'O':
                    print("The field is occuped, choose another one")
                else:
                    return movement
            else:
                print("Number needs to be between 1 and 9")
def change_player():
    global actual_player
    if actual_player == 'X':
        actual_player = 'O'
    else:
        actual_player = 'X'
# control whether a player has won
def control_win():
    # if all 3 fields are equal, the corresponding player has won
    # control on rows
    if field[1] == field[2] == field[3]:
        return field[1]
    if field[4] == field[5] == field[6]:
        return field[4]
    if field[7] == field[8] == field[9]:
        return field[7]
    # control on columns
    if field[1] == field[4] == field[7]:
        return field[1]
    if field[2] == field[5] == field[8]:
        return field[2]
    if field[3] == field[6] == field[9]:
        return field[3]
    # control on diagonals
    if field[1] == field[5] == field[9]:
        return field[5]
    if field[7] == field[5] == field[3]:
        return field[5]
        
def control_if_win():
    if (field[1] == 'X' or field[1] == 'O') \
      and (field[2] == 'X' or field[2] == 'O') \
      and (field[3] == 'X' or field[3] == 'O') \
      and (field[4] == 'X' or field[4] == 'O') \
      and (field[5] == 'X' or field[5] == 'O') \
      and (field[6] == 'X' or field[6] == 'O') \
      and (field[7] == 'X' or field[7] == 'O') \
      and (field[8] == 'X' or field[8] == 'O') \
      and (field[9] == 'X' or field[9] == 'O'):
        return ('undecided')
        
# output actual field
field_output()
while active_game:
    # input active player
    print()
    print ("Player " + actual_player + " is next")
    movement = player_input()
    if movement:
        # field[movement] = 'X'
        field[movement] = actual_player
        # actual field output
        field_output()
        # control if someone has won
        win = control_win()
        if win:
            print ("Player " + win + " won!")
            active_game = False
            break
        # control if its undecided
        undecided = control_if_win()
        if undecided:
            print ("The game ended undecided!")
            active_game = False
        # change player
        change_player()
print() 




