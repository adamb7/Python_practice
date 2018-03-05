a = input("First number: ")
b = input("Second number: ")
c = input("Third number: ")

if a >= b:
    if a >= c:
        print(a)
    else:
        print(c)
elif b >= c:
    print(b)
else:
    print(c)