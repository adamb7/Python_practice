import requests


url = 'http://www.practicepython.org/assets/Training_01.txt'
r = requests.get(url)
r_html = r.text
with open("pelda.txt", 'w') as open_file:
    open_file.write(r_html)

sun_dict = {}
with open("pelda.txt", 'r') as read_file:
    line = read_file.readline()
    while line:
        line = line.strip()
        line_data = line[3:].split('/')[0]
        if line_data in sun_dict:
            sun_dict[line_data] += 1
        else:
            sun_dict[line_data] = 1

        line = read_file.readline()

print(sun_dict)