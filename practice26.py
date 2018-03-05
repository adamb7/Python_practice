example_list1 = [[1,0,2], [1,0,2], [1,0,2]]
example_list2 = [[1,1,1], [2,0,2], [1,0,2]]
example_list3 = [[1,0,2], [0,1,2], [2,0,1]]
example_list4 = [[1,0,2], [0,2,1], [2,0,1]]
example_list5 = [[0,0,2], [0,2,1], [0,0,1]]


def check_result(input_list):
    winner = 0
    for i in range(len(input_list)):
        if input_list[i][0] == input_list[i][1] and input_list[i][0] == input_list[i][2]:
            if input_list[i][0] == 1:
                winner = 1
            elif input_list[i][0] == 2:
                winner = 2
            else:
                pass
            if winner != 0:
                print("Winner in row: Player ", winner)
                return
        if input_list[0][i] == input_list[1][i] and input_list[0][i] == input_list[2][i]:
            if input_list[0][i] == 1:
                winner = 1
            elif input_list[0][i] == 2:
                winner = 2
            else:
                pass
            if winner != 0:
                print("Winner in col: Player ", winner)
                return

        if input_list[0][0] == input_list[1][1] and input_list[0][0] == input_list[2][2]:
            if input_list[0][0] == 1:
                winner = 1
            elif input_list[0][0] == 2:
                winner = 2
            else:
                pass
            if winner != 0:
                print("Winner in diag: Player ", winner)
                return

        if input_list[0][-1] == input_list[1][-2] and input_list[0][-1] == input_list[2][-3]:
            if input_list[0][-1] == 1:
                winner = 1
            elif input_list[0][-1] == 2:
                winner = 2
            else:
                pass
            if winner != 0:
                print("Winner in rev diag: Player ", winner)
                return

    print("No winner")
    return


print("First list")
check_result(example_list1)
print("Second list")
check_result(example_list2)
print("Third list")
check_result(example_list3)
print("Fourth list")
check_result(example_list4)
print("Fifth list")
check_result(example_list5)