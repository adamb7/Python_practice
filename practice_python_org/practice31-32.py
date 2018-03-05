import random


def gen_word():
    word_list = []
    with open("sowpods.txt", 'r') as open_file:
        line = open_file.readline()
        while line:
            word_list.append(line.strip())
            line = open_file.readline()
    return random.choice(word_list)


def draw_hangman(arg):

    if(arg == 1):
        print("   _   ")
        print(" /   \ ")
        print(" \ _ / ")
    if (arg == 2):
        print("   _   ")
        print(" /   \ ")
        print(" \   / ")
        print("   |   ")
        print("   |   ")
        print("   |   ")
    if (arg == 3):
        print("   _   ")
        print(" /   \ ")
        print(" \   / ")
        print("   |   ")
        print("  /|   ")
        print(" / |   ")
    if (arg == 4):
        print("   _   ")
        print(" /   \ ")
        print(" \   / ")
        print("   |   ")
        print("  /|\  ")
        print(" / | \ ")
    if (arg == 5):
        print("   _   ")
        print(" /   \ ")
        print(" \   / ")
        print("   |   ")
        print("  /|\  ")
        print(" / | \ ")
        print("  /    ")
        print("  /    ")
        print(" _|    ")
        print("       ")
    if (arg == 6):
        print("   _   ")
        print(" /   \ ")
        print(" \   / ")
        print("   |   ")
        print("  /|\  ")
        print(" / | \ ")
        print("  / \  ")
        print("  / \  ")
        print(" _| |_ ")
        print("       ")
    return


cont = 'y'
while cont == 'y':
    hang_word = gen_word().lower()
    print(hang_word)
    disp = list("_" * len(hang_word))
    print("Welcome to hangman!")
    num_list = []
    guess_list= []
    j = 0
    while j < 6 and '_' in disp:
        print(''.join(disp))
        a = input("Guess your letter: ")
        if a in hang_word:

            for i, k in enumerate(hang_word):
                if k == a:
                    num_list.append(i)
            for m in num_list:
                disp[m] = a
            del num_list[:]

        else:
            print("Incorrect!")
            if a in guess_list:
                print("You already guessed that letter!")
            else:
                print("Bad guesses: ")
                guess_list.append(a)
                j += 1
            print(guess_list)
            #print("Number of tries left: ", 6 - j)
            draw_hangman(j)

    if j == 6:
        print("Game over!")
    else:
        print(''.join(disp))
        print("Well done!")
    cont = input("Would you like to another game? y / n  ")

print("Goodbye!")