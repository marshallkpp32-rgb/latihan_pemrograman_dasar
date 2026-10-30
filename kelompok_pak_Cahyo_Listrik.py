# Kalkulator Hemat Listrik

# Tarif contoh per kWh (silakan sesuaikan dengan tarif PLN terbaru)
TARIF = {
    "R1-900": 1352,
    "R1-1300": 1444.70,
    "R1-2200": 1444.70,
}
HARI_PER_BULAN = 30


def hitung_kwh(daya_watt, jam_per_hari, hari=HARI_PER_BULAN):
    return daya_watt * jam_per_hari * hari / 1000


def hitung_biaya(kwh, tarif):
    return kwh * tarif


def input_angka(pesan):
    while True:  # perulangan sampai input valid
        try:
            nilai = float(input(pesan))
            if nilai < 0:
                print("Tidak boleh negatif.")
                continue
            return nilai
        except ValueError:
            print("Masukkan angka yang valid.")


def pilih_golongan():
    print("Golongan tarif:")
    for g, t in TARIF.items():
        print(f"  {g} (Rp{t:,.0f}/kWh)")
    while True:
        g = input("Pilih golongan: ").strip().upper()
        if g in TARIF:
            return g
        print("Golongan tidak ada.")


def beri_saran(perangkat, total_kwh):
    print("\n=== SARAN HEMAT ===")
    if total_kwh > 200:
        print("Pemakaian tinggi (>200 kWh/bulan). Kurangi pemakaian perangkat boros.")
    elif total_kwh > 100:
        print("Pemakaian sedang. Masih bisa dihemat.")
    else:
        print("Pemakaian hemat, pertahankan!")

    terboros = max(perangkat, key=lambda p: p["kwh"])
    persen = terboros["kwh"] / total_kwh * 100
    print(f"Perangkat terboros: {terboros['nama']} ({persen:.1f}% dari total).")
    if terboros["jam"] > 8:
        print(f"Coba kurangi jam pakai {terboros['nama']} (sekarang {terboros['jam']:.0f} jam/hari).")


def main():
    print("=== KALKULATOR HEMAT LISTRIK ===")
    golongan = pilih_golongan()
    tarif = TARIF[golongan]

    perangkat = []  # list of dict
    while True:
        nama = input("\nNama perangkat (kosongkan untuk selesai): ").strip()
        if nama == "":
            if len(perangkat) == 0:
                print("Minimal masukkan 1 perangkat.")
                continue
            break
        daya = input_angka("Daya (watt)      : ")
        jam = input_angka("Pemakaian (jam/hari): ")
        kwh = hitung_kwh(daya, jam)
        perangkat.append({"nama": nama, "daya": daya, "jam": jam, "kwh": kwh})

    print("\n=== RINCIAN ===")
    total_kwh = 0
    for p in perangkat:
        biaya = hitung_biaya(p["kwh"], tarif)
        total_kwh += p["kwh"]
        print(f"{p['nama']:<15} {p['kwh']:>7.2f} kWh  Rp{biaya:>10,.0f}")

    total_biaya = hitung_biaya(total_kwh, tarif)
    print("-" * 40)
    print(f"{'TOTAL':<15} {total_kwh:>7.2f} kWh  Rp{total_biaya:>10,.0f} / bulan")

    beri_saran(perangkat, total_kwh)


if __name__ == "__main__":
    main()
