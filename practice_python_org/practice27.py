game_list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def print_board():
    print(game_list[0])
    print(game_list[1])
    print(game_list[2])


def check_boardisfull():
    stop = 1
    for i in range(len(game_list)):
        if 0 in game_list[i]:
            stop = 0
            return stop
    return stop


repeat_trig = 1

while check_boardisfull() == 0:
    while repeat_trig == 1:
        user_draw = input("Player 1, pick a tile row,col: ")
        first_char, second_char = user_draw.split(',')
        if game_list[int(first_char)][int(second_char)] == 0:
            game_list[int(first_char)][int(second_char)] = 'X'
            repeat_trig = 0
        else:
            print("That tile is not empty!")
            print_board()
            repeat_trig = 1
    repeat_trig = 1
    print_board()

    if check_boardisfull() == 1:
        break
    while repeat_trig == 1:
        user_draw = input("Player 2, pick a tile row,col: ")
        first_char, second_char = user_draw.split(',')
        if game_list[int(first_char)][int(second_char)] == 0:
            game_list[int(first_char)][int(second_char)] = 'O'
            repeat_trig = 0
        else:
            print("That tile is not empty!")
            print_board()
            repeat_trig = 1
    repeat_trig = 1
    print_board()
print("Game over")