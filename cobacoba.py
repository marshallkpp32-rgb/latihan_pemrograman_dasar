a = float(input("masukkan angka pertama: "))
b = float(input("masukkan angka kedua: "))
if a>b:
    print("angka maksimal:", a)
elif b>a:
    print("angka maksimal:", b)
else:
    print("kedua angka sama:", a)
    
import math
print("pilihan:")
print("1. hitung keliling lingkaran")
print("2. hitung luas lingkaran")
pilihan = int(input("masukkan pilihan (1/2): "))
r = float(input("masukkan jari-jari: "))
if pilihan == 1:
    keliling = 2 * math.pi * r
    print("keliling lingkaran:", keliling)
elif pilihan == 2:
    luas = math.pi * r ** 2
    print("luas lingkaran:", luas)
else:
    print("pilihan tidak valid")