x = input("Input: ")
y = len(x)
print("Output: ")
for i in range(y):
    for j in range(y-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(x[j],end="")
    print()
for i in range(1,y):
    for h in range(i):
        print(" ",end="")
    for h in range(y-1):
        print(x[h],end="")
    print()