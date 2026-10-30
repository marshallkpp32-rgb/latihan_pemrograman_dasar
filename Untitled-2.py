nilai = int(input("masukkan nilai ujian:"))
pres = int(input("masukkan presensi:"))

if pres >= 75 and nilai>=60:
    print("lulus")
else:
    print("tidak lulus")

if nilai >= 85:
    print("grade a")
elif nilai >= 70:
    print("grade b")
elif nilai >= 60:
    print("grade c")
else:
    print("grade d")