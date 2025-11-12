FILE_NAME = 'riwayat.txt'

def hitung_bmi(berat, tinggi):
    try:
        bmi = berat / (tinggi ** 2)
        return bmi
    except ZeroDivisionError:
        return 0

def klasifikasi_bmi(bmi):
    if bmi < 18.5:
        return (1, "Berat Badan Kurang")
    elif 18.5 <= bmi < 24.9:
        return (2, "Berat Badan Normal")
    elif 25.0 <= bmi < 29.9:
        return (3, "Berat Badan Berlebih")
    elif 30.0 <= bmi < 34.9:
        return (4, "Obesitas Kelas I")
    elif 35.0 <= bmi < 39.9:
        return (5, "Obesitas Kelas II")
    else:
        return (6, "Obesitas Kelas III")

def program_bmi():
    print("\n--- Hitung BMI ---")
    entry_id = ""
    bmi_hasil = 0
    berat = 0
    tinggi_cm = 0

    while True:
        try:
            entry_id = input("Masukkan Entry ID: ")
            berat = float(input("Masukkan Berat Badan (kg): "))
            tinggi_cm = float(input("Masukkan Tinggi Badan (cm): "))
            
            tinggi_m = tinggi_cm / 100

            if berat >= 590:
                print("\n Berat melebihi kapasitas manusia normal")
                continue  

            if tinggi_m >= 2.51:
                print("\n Tinggi melebihi kapasitas manusia normal")
                continue              
            
            if berat <= 0 or tinggi_m <= 0:
                print("\n Berat dan Tinggi harus bernilai positif. Silakan coba lagi.")
                continue
            
            # Hitung BMI
            bmi_hasil = hitung_bmi(berat, tinggi_m)

            break
            
        except ValueError:
            print("\n Input tidak valid. Harap masukkan angka untuk berat dan tinggi.")
            continue
        except ZeroDivisionError:
            print("\n Tinggi badan tidak boleh nol. Silakan masukkan ulang.")
            continue

    # Tampilkan hasil
    kode, kategori = klasifikasi_bmi(bmi_hasil)
    
    print("\n--- Hasil Perhitungan BMI ---")
    print(f"Berat Badan: {berat} kg")
    print(f"Tinggi Badan: {tinggi_cm} cm")
    print(f"Nilai BMI Anda: {bmi_hasil:.2f}")
    print(f"Kategori: {kategori}")
    
    if kode > 2:
        print("\n Status ini menunjukkan potensi risiko kesehatan yang meningkat.")
    elif kode == 1:
        print("\n Status ini menunjukkan potensi risiko kesehatan.")
    else:
        print("\n Status ini berada dalam kisaran berat badan yang sehat.")

    return entry_id, bmi_hasil, kategori, kode


def input_history():
    entry_id, bmi, kategori, kode = program_bmi()

    if not entry_id:
        print("‼️ID tidak boleh kosong.")
        return
    if bmi <= 0:
        print("‼️Data BMI tidak valid.")
        return

    existing_ids = set()
    try:
        with open(FILE_NAME, 'r') as f:
            for line in f:
                parts = line.strip().split('|')
                if parts:
                    existing_ids.add(parts[0])
    except FileNotFoundError:
        pass

    while entry_id in existing_ids:
        print(f"ID '{entry_id}' sudah digunakan. Silakan masukkan ID lain.\n❌Data gagal tersimpan")
        entry_id = input("Masukkan ID baru: ").strip()
        if not entry_id:
            print("‼️ID tidak boleh kosong.")
            return

    try:
        with open(FILE_NAME, 'a') as f:
            f.write(f"{entry_id}|{bmi:.2f}|{kategori:20}|{kode}\n")
        print("Data berhasil disimpan.")
    except Exception as e:
        print("Gagal menyimpan data:", e)
