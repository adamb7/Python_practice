def draw_tiles(inp_num):
    top = "  ---   "
    mid = "|       "
    bot = "  ---   "
    for i in range(1, inp_num + 1):
        if i == 1:
            print(top * inp_num)
        print(mid * (inp_num + 1))
        print(mid * (inp_num + 1))
        print(bot * inp_num)


def check_result(input_list):
    winner = 0
    for i in range(len(input_list)):
        if input_list[i][0] == input_list[i][1] and input_list[i][0] == input_list[i][2]:
            if input_list[i][0] == 'X':
                winner = 1
            elif input_list[i][0] == 'O':
                winner = 2
            else:
                pass
            if winner != 0:
                print("Winner in row: Player ", winner)
                return winner
        if input_list[0][i] == input_list[1][i] and input_list[0][i] == input_list[2][i]:
            if input_list[0][i] == 'X':
                winner = 1
            elif input_list[0][i] == 'O':
                winner = 2
            else:
                pass
            if winner != 0:
                print("Winner in col: Player ", winner)
                return winner

        if input_list[0][0] == input_list[1][1] and input_list[0][0] == input_list[2][2]:
            if input_list[0][0] == 'X':
                winner = 1
            elif input_list[0][0] == 'O':
                winner = 2
            else:
                pass
            if winner != 0:
                print("Winner in diag: Player ", winner)
                return winner

        if input_list[0][-1] == input_list[1][-2] and input_list[0][-1] == input_list[2][-3]:
            if input_list[0][-1] == 'X':
                winner = 1
            elif input_list[0][-1] == 'O':
                winner = 2
            else:
                pass
            if winner != 0:
                print("Winner in rev diag: Player ", winner)
                return winner

    return winner


def print_board():
    top = "  ---   "
    midl = "| "
    midr = " |"
    bot = "  ---   "
    for i in range(0, 3):
        if i == 0:
            print(top * 3)
        print(midl, game_list[i][0], midr, midl, game_list[i][1], midr, midl, game_list[i][2], midr)
        print(bot * 3)


def check_boardisfull():
    stop = 1
    for i in range(len(game_list)):
        if 0 in game_list[i]:
            stop = 0
            return stop
    return stop


game_list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
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
    if check_result(game_list) == 1 or check_result(game_list) == 2:
        break

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
    if check_result(game_list) == 1 or check_result(game_list) == 2:
        break
print("Game over")
