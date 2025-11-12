    # Water Plan

    # Program: Cek Kebutuhan Cairan Tubuh

    # --- Input Data Profil ---
def water_plan():
    while True:
        try:
            nama = input("Masukkan nama: ")
            umur = input("Masukkan umur: ")
            jenis_kelamin = input("Masukkan jenis kelamin (L/P): ")
            berat_badan = float(input("Masukkan berat badan (kg): "))
            tinggi_badan = float(input("Masukkan tinggi badan (cm): "))

            # --- Perhitungan Kebutuhan Cairan ---
            kebutuhan_cairan_ml = 30 * berat_badan
            kebutuhan_cairan_liter = kebutuhan_cairan_ml / 1000

            # Hitung jumlah gelas (1 gelas = 250 ml)
            jumlah_gelas = kebutuhan_cairan_ml / 250

            # --- Pembagian waktu minum ---
            pagi = jumlah_gelas * 0.30
            siang = jumlah_gelas * 0.30
            sore = jumlah_gelas * 0.25
            malam = jumlah_gelas * 0.15

            # --- Output Hasil ---
            print("\n--- Profil Pengguna ---")
            print(f"Nama           : {nama}")
            print(f"Umur           : {umur} tahun")
            print(f"Jenis Kelamin  : {jenis_kelamin}")
            print(f"Berat Badan    : {berat_badan} kg")
            print(f"Tinggi Badan   : {tinggi_badan} cm")

            print("\n--- Hasil Perhitungan ---")
            print(f"Kebutuhan cairan per hari : {kebutuhan_cairan_liter:.2f} liter")
            print(f"Setara dengan             : {jumlah_gelas:.0f} gelas (1 gelas = 250 ml)")

            print("\n--- Rekomendasi Minum Harian ---")
            print(f"Pagi  : {pagi:.0f} gelas (setelah bangun dan sebelum sarapan)")
            print(f"Siang : {siang:.0f} gelas (saat dan setelah makan siang)")
            print(f"Sore  : {sore:.0f} gelas (sebelum makan malam atau olahraga)")
            print(f"Malam : {malam:.0f} gelas (setelah makan malam dan sebelum tidur)")
            break
        except ValueError:
            print("\n‼️Input tidak valid.")
            continue