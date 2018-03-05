def draw_tiles(inp_num):
    top = "  ---   "
    mid = "|       "
    bot = "  ---   "
    for i in range(1, inp_num + 1):
        if i == 1 :
            print(top * inp_num)
        print(mid * (inp_num + 1))
        print(mid * (inp_num + 1))
        print(bot * inp_num)


title = int(input("Set game board size: "))
draw_tiles(title)