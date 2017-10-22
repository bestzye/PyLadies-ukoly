n = int(input("Zadej pocet radku:"))
for radek in range (1,n):
    if radek == 1 or radek == n-1:
        for znamenko in range (6):
            print ("X", end="")
    else:
        print ("X    X", end="")
    print()
