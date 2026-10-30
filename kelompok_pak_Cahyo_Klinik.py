# Sistem Antrean / Reservasi Klinik
# Syarat: perulangan, kondisional, operasi aritmatika, fungsi, struktur data

# Struktur data: dictionary dokter -> kuota & biaya, list antrean berisi dictionary pasien
DOKTER = {
    "umum": {"nama": "dr. Andi", "kuota": 5, "biaya": 50000},
    "gigi": {"nama": "drg. Sari", "kuota": 3, "biaya": 100000},
    "anak": {"nama": "dr. Budi", "kuota": 4, "biaya": 80000},
}
WAKTU_PER_PASIEN = 15  # menit

antrean = []  # list of dict
nomor_terakhir = 0


def jumlah_antrean(poli):
    jumlah = 0
    for p in antrean:  # perulangan
        if p["poli"] == poli:
            jumlah += 1
    return jumlah


def daftar_pasien():
    global nomor_terakhir
    nama = input("Nama pasien : ").strip()
    print("Pilihan poli:")
    for kode, d in DOKTER.items():
        sisa = d["kuota"] - jumlah_antrean(kode)
        print(f"  {kode:<5} - {d['nama']} (sisa kuota: {sisa}, biaya: Rp{d['biaya']:,})")
    poli = input("Pilih poli  : ").strip().lower()

    # kondisional
    if poli not in DOKTER:
        print("Poli tidak ditemukan.")
        return
    if jumlah_antrean(poli) >= DOKTER[poli]["kuota"]:
        print("Maaf, kuota poli ini sudah penuh.")
        return

    nomor_terakhir += 1  # aritmatika
    posisi = jumlah_antrean(poli) + 1
    estimasi = posisi * WAKTU_PER_PASIEN
    antrean.append({"no": nomor_terakhir, "nama": nama, "poli": poli})
    print(f"Berhasil! Nomor antrean: {nomor_terakhir}")
    print(f"Estimasi tunggu: {estimasi} menit | Biaya: Rp{DOKTER[poli]['biaya']:,}")


def tampilkan_antrean():
    if len(antrean) == 0:
        print("Belum ada antrean.")
        return
    print("\n=== DAFTAR ANTREAN ===")
    for p in antrean:
        print(f"No {p['no']:<3} | {p['nama']:<15} | Poli {p['poli']}")


def batal_reservasi():
    try:
        no = int(input("Masukkan nomor antrean yang dibatalkan: "))
    except ValueError:
        print("Nomor harus angka.")
        return
    for p in antrean:
        if p["no"] == no:
            antrean.remove(p)
            print(f"Antrean {p['nama']} dibatalkan.")
            return
    print("Nomor antrean tidak ditemukan.")


def panggil_pasien():
    if not antrean:
        print("Tidak ada pasien dalam antrean.")
        return
    p = antrean.pop(0)  # FIFO
    print(f"Memanggil nomor {p['no']} - {p['nama']} ke poli {p['poli']}")


def menu():
    while True:  # perulangan sampai user keluar
        print("\n=== KLINIK SEHAT ===")
        print("1. Daftar pasien")
        print("2. Lihat antrean")
        print("3. Batalkan reservasi")
        print("4. Panggil pasien berikutnya")
        print("5. Keluar")
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            daftar_pasien()
        elif pilihan == "2":
            tampilkan_antrean()
        elif pilihan == "3":
            batal_reservasi()
        elif pilihan == "4":
            panggil_pasien()
        elif pilihan == "5":
            print("Terima kasih!")
            break
        else:
            print("Menu tidak valid.")


if __name__ == "__main__":
    menu()
