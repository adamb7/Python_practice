import string
import random


def passgen(strength):
    if strength == "weak":
        b = ["password", "snow", "ball", "secret", "123456"]
        password_string = random.choice(b)
    else:
        password_string = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(
            string.digits) + random.choice(string.ascii_uppercase) + random.choice(
            string.ascii_lowercase) + random.choice(string.punctuation)
    return password_string


a = input("How strong your password shoudl be? ")
a = passgen(str(a))
print("Generated password is: ", a)
