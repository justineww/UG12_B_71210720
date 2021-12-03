counter = 0
berhenti = " "
listNama = [] #[Abel]
listKursi = [] #[2]
cek = 0

while(berhenti.upper!="STOP"):
    nama = str(input("Masukkan nama : "))
    if(nama=="STOP"):
        berhenti = "STOP"
        break
    else:
        n = int(input("Masukkan nomor kursi "+ nama + " : "))
        
        if(len(listKursi)==0):
            listNama.insert(counter,nama)
            listKursi.insert(counter,n)
            counter = counter + 1
        else:
            for i in range(len(listKursi)):
                if(listKursi[i] == n):
                    cek = 0
                    break
                else:
                    cek = 1
            
            if(cek==1):
                listNama.insert(counter,nama)
                listKursi.insert(counter,n)
                counter = counter + 1
            else:
                print("Mohon maaf kursi tersebut telah terisi!")

print()
print("List kursi yang telah terisi: ")

for i in range (counter):
    print("Kursi nomor " + str(listKursi[i]) + " telah diisi oleh " + str(listNama[i]))

