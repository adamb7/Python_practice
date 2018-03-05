import random
high_index = 100
low_index = 0
num_guess = random.randint(low_index, high_index)
print("Imagine an integer between 0 and 100....  \n")
guess_count = 0

while True:
    print(num_guess)
    cmp_num = input("Is this the number? (y / n)   ")
    guess_count += 1
    if cmp_num == 'n':
        cmp_num = input ("Is it higher or lower? (h / l)   ")
        if cmp_num == 'h':
            if num_guess != low_index:
                low_index = num_guess
            else:
                low_index += 1
        elif cmp_num == 'l':
            if num_guess != high_index:
                high_index = num_guess
            else:
                high_index -= 1
        else:
            print("Wrong input.")
    elif cmp_num == 'y':
        print("Game over.")
        print("Number of guesses:", guess_count)
        break
    else:
        print("Wrong input.")
    num_guess = random.randint(low_index, high_index)