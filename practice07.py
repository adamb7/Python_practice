a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
evenlist = []

evenlist = [ a[index] for index in range(len(a)) if( a[index] %2 == 0 ) ]

print(evenlist)
