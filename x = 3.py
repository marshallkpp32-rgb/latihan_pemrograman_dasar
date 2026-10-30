print("\n IF AND OR")
x = 3
if(x % 2 == 1) and (x == 3):
    print("x adalah bilangan ganjil")
print("\n conntoh lain")
umur = int(input("Masukkan umur ;"))
lulus = input("masukkan kategori;")
if umur >= 17 and lulus:
    print("boleh kuliah", lulus)
else:
    print("bekerja")
print("\n NESTED IF")
username = input("masukkan username;")
password = int(input("masukkan password;"))
aktif = True
if username == "rino":
    if password == "12345":
       if not aktif:
           print("akun tidak aktif")
       else:
        print("login berhasil")
    else:
       print("password salah")
else:
   print("username salah")
