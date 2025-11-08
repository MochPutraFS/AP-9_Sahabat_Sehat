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
        return (3, "Berat Badan Berlebih (Pre-obesitas)")
    elif 30.0 <= bmi < 34.9:
        return (4, "Obesitas Kelas I")
    elif 35.0 <= bmi < 39.9:
        return (5, "Obesitas Kelas II")
    else:
        return (6, "Obesitas Kelas III")

def program_bmi():
    print("cek BMI")
    
    while True:
        try:
            berat = float(input("Masukkan Berat Badan (kg): "))
            tinggi_cm = float(input("Masukkan Tinggi Badan (cm): "))
            
            tinggi_m = tinggi_cm / 100
            
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
    print(f"Nilai BMI Anda: **{bmi_hasil:.2f}**")
    print(f"Kategori: **{kategori}**")
    
    if kode > 2:
        print("\n*Status ini menunjukkan potensi risiko kesehatan yang meningkat.*")
    elif kode == 1:
        print("\n*Status ini menunjukkan potensi risiko kesehatan.*")
    else:
        print("\n*Status ini berada dalam kisaran berat badan yang sehat.*")


program_bmi()