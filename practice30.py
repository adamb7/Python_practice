import random

word_list = []
with open("sowpods.txt", 'r') as open_file:

        line = open_file.readline()
        while line:
            word_list.append(line.strip())
            line = open_file.readline()
        random.choice(word_list)

