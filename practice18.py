import random


def check_num(rand_list, given_list):
    cow_count = 0
    bull_count = 0

    for j in range(len(rand_list)):
        for i in range(len(given_list)):
            if rand_list[j] == given_list[i]:
                if j == i:
                    cow_count += 1
                else:
                    bull_count += 1
            i += 1
        j += 1

    return cow_count, bull_count


def split_num(f):
    num_list = [int(i) for i in str(f)]
    return num_list


def rand_gen():
    first = 0
    second = 0
    third = 0
    fourth = 0
    while (first == second) or (first == third) or (first == fourth) or (second == third) or (second == fourth) or (third == fourth):
        first = random.randint(1, 9)
        second = random.randint(0, 9)
        third = random.randint(0, 9)
        fourth = random.randint(0, 9)
    y = int(first * 1000 + second * 100 + third * 10 + fourth)
    return y


if __name__ == "__main__":
    a = rand_gen()
    a_list = split_num(a)
    b_list = [0, 0, 0, 0]
    try_count = 0
    print("Rand number: ", a)
    print("Splitted rand number: ", a_list)

    while a_list != b_list:
        b = int(input("Enter a number: "))
        b_list = split_num(b)
        # print("Splitted given number: ", b_list)
        cows, bulls = check_num(a_list, b_list)
        print("Cows: ", cows)
        print("Bulls: ", bulls)
        try_count += 1

    print("You guessed right!")
    print("Number of tries: ", try_count)
