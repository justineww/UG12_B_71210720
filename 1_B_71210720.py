x = int(input("Masukkan banyak bilangan : "))
hasil = 1

print("Total = ", end = "")

for i in range(1,x+1):
    if(i%7==0):
        hasil = hasil + 0
        print("+ 0", end = " ")
    elif(i%3==0):
        hasil = hasil + (i * -1)
        print("- " + str(i), end = " ")
    elif(i==1):
        print(str(i), end = " ")
    else:
        hasil = hasil + i
        print("+ " + str(i), end = " ")

print("\nHasil perhitungan diatas ialah " + str(hasil))