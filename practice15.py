a=str(input("Type a sentence: "))
b=a.split()
print("Split Sentence: ",b)
c=[b[len(b)-1-i] for i in range(len(b))]
print("Result: " + " ".join(c))