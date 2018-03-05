import random
def list_process(list_name):
    list_output=list(set(list_name))
    return list_output
def generate_list():
    y = [random.randint(1,20) for i in range(1,10)]
    return y
a = generate_list()
print("First list: ",a)
a=list_process(a)
print("Minus dupes: ",a)