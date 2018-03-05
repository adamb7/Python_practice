def fibonacci(length):
    fibolist = [1, 1]
    i = 0
    while i<length-2:
        a = fibolist[i]
        b = fibolist[i+1]
        c = a+b
        fibolist.append(c)
        i+=1
    print(fibolist)
a=int(input("Length of fibonacci array is: "))
fibonacci(a)
