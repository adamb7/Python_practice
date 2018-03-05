def exc_20(array, num):
    upper_index = len(array)-1
    lower_index = 0
    num_ofelements = len(array)-1

    while num_ofelements > 1:
        middle_index = lower_index + (upper_index - lower_index) // 2
        print("Upper: ", upper_index)
        print("middle: ", middle_index)
        print("lower: ", lower_index)
        if array[middle_index] == num:
            print("Number ok")
            return
        elif array[middle_index] > num:
            upper_index = middle_index
        elif array[middle_index] < num:
            lower_index = middle_index
        else:
            print("Failed")
            return
        num_ofelements = upper_index - lower_index
    if (array[upper_index] == num) or (array[lower_index] == num):
        print("Number ok")
        return
    else:
        print("Number missing")
        return


a = [1, 2, 3, 4, 6]
b = 7
exc_20(a, b)
