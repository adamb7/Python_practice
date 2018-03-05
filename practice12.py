def filter(array):
    b = [array[index] for index in range(len(array)) if index == 0 or index == len(array) - 1]
    print(b)

a = [5, 10, 15, 20, 25]
filter(a)
