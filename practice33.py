my_dict = {"Albert Einstein" : "03/14/1879", "Benjamin Farnklin" : "01/17/1706", "Ada Lovelace": 12/10/1815}

print("Welcome to the birthday dictionary. We know the birthdays of:")
for i in my_dict:
    print(i)
name = input("Who's birthday do you want to look up? ")
if name in my_dict:
    print(name + "'s birthday is " + my_dict[name])
else:
    print("Name not in database.")
