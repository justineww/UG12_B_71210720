x = int(input("Input: "))
print("Output: ")
for i in range(x):
    for j in range(x-i-1):
        print(" ",end="   ")
    for j in range(x):
        if j == 0 or i == (x-1) or i == j:
            print("*", end= "   ")
        else:
            print(end="    ")
    print()