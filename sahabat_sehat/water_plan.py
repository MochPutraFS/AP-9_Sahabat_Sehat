    # Water Plan

    # Program: Cek Kebutuhan Cairan Tubuh

    # --- Input Data Profil ---

def nama():
    while True:
        try:
            nama =input("Masukkan nama: ")
            tidak_boleh = '1234567890!@#$%^&*()-=[];{}|_+?<>,.:'
            if nama in tidak_boleh:
                print("❌nama tidak valid")
                continue
            else:
                return nama
        except ValueError:
            print("‼️input tidak valid.")
            continue

def umur():
    while True:
        try:
            umur =int(input("Masukkan umur: "))
            if umur > 116:
                print("❌umur tidak valid")
                continue
            else:
                return umur
        except ValueError:
            print("‼️input tidak valid.")
            continue

def jenis_kelamin():
    while True:
        try:
            nama =input("Masukkan jenis kelamin (L/P): ")
            boleh = 'LPlp'
            if nama not in boleh:
                print("❌jenis kelamin tidak valid")
                continue
            else:
                return nama
        except ValueError:
            print("‼️input tidak valid.")
            continue

def berat_badan():
    while True:
        try:
            berat_badan =int(input("Masukkan berat badan: "))
            if berat_badan > 590:
                print("❌berat badan tidak valid")
                continue
            else:
                return berat_badan
        except ValueError:
            print("‼️input tidak valid.")
            continue

def tinggi_badan():
    while True:
        try:
            berat_badan =int(input("Masukkan tinggi badan: "))
            if berat_badan > 231:
                print("❌tinggi badan tidak valid")
                continue
            else:
                return berat_badan
        except ValueError:
            print("‼️input tidak valid.")
            continue

def water_plan():
    n = nama()
    u = umur()
    j = jenis_kelamin()
    b = berat_badan()
    t = tinggi_badan()

    # --- Perhitungan Kebutuhan Cairan ---
    kebutuhan_cairan_ml = 30 * b
    kebutuhan_cairan_liter = kebutuhan_cairan_ml / 1000

    # Hitung jumlah gelas (1 gelas = 250 ml)
    jumlah_gelas = kebutuhan_cairan_ml / 250

    # --- Pembagian waktu minum ---
    pagi = jumlah_gelas * 0.30
    siang = jumlah_gelas * 0.30
    sore = jumlah_gelas * 0.25
    malam = jumlah_gelas * 0.15

    # --- Output Hasil ---
    print("--- Profil Pengguna ---")
    print(f"Nama           : {n}")
    print(f"Umur           : {u} tahun")
    print(f"Jenis Kelamin  : {j}")
    print(f"Berat Badan    : {b} kg")
    print(f"Tinggi Badan   : {t} cm")

    print("--- Hasil Perhitungan ---")
    print(f"Kebutuhan cairan per hari : {kebutuhan_cairan_liter:.2f} liter")
    print(f"Setara dengan             : {jumlah_gelas:.0f} gelas (1 gelas = 250 ml)")

    print("--- Rekomendasi Minum Harian ---")
    print(f"Pagi  : {pagi:.0f} gelas (setelah bangun dan sebelum sarapan)")
    print(f"Siang : {siang:.0f} gelas (saat dan setelah makan siang)")
    print(f"Sore  : {sore:.0f} gelas (sebelum makan malam atau olahraga)")
    print(f"Malam : {malam:.0f} gelas (setelah makan malam dan sebelum tidur)")
