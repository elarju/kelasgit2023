#Soal no 1
print("Program bilangan bulat 1 hingga n")
n = int(input("Masukkan bilangan bulat: "))
for i in range(n):
  print(i+1)
  
#Soal no 2
print("Program bilangan ganjil 1 hingga n")
n = int(input("Masukkan bilangan bulat: "))
for i in range(n+1):
  if(i%2 == 0):
    continue
  else:
    print(i)
	
#Soal no 3
print("Program mengecek bilangan ganjil 1 hingga n")
n = int(input("Masukkan bilangan bulat: "))
def cek_ganjil(bilangan):
    if bilangan % 2 != 0:
        print(f"{bilangan} adalah bilangan ganjil")

for i in range(n):
    cek_ganjil(i+1)