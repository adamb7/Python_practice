def check_num(number,divisor):
    while divisor <= (number / 2):
        if (number % divisor == 0):
            print("Given number is not prime.")
            break
        else:
            divisor += 1
    if(divisor > number/2):
        print("Given number is prime")

num= int(input("Choose a number: "))
div = 2
check_num(num,div)