happy_array = []
prime_array = []


def process_file(filename):
    with open(filename, 'r') as open_file:
        array = list(open_file.readlines())

    for i in range(len(array)):
        array[i] = array[i].strip()
    print(array)
    return array

prime_array = process_file("primenumbers.txt")
happy_array = process_file("happynumbers.txt")
common_array = []

for i in range(len(prime_array)):
    if prime_array[i] in happy_array:
        common_array.append(prime_array[i])

print(common_array)
