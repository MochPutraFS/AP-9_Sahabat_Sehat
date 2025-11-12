Onii-chan~ Ais bisa buatkan versi **README.md lengkap** dengan dokumentasi tiap fitur, contoh penggunaan, dan contoh output dari aplikasi **Sahabat Sehat**. Berikut contohnya:

```markdown
# Sahabat Sehat 🏋️‍♂️💧🍎

**Sahabat Sehat** adalah aplikasi Python berbasis terminal yang membantu pengguna mengontrol kesehatan mereka. Aplikasi ini mencakup fitur untuk memantau BMI, rencana makanan, workout, kebutuhan cairan, dan progres harian.

---

## Fitur Utama

### 1. Lihat Makanan 🍱
Menampilkan daftar makanan beserta detail nutrisi:
- Kalori (kkal)
- Protein (g)
- Karbohidrat (g)
- Lemak (g)

**Contoh:**
```

|  No.    |   Nama Makanan                  |   Kalori  |
+--------------------------------------------------+
|  1      |   Nasi putih (100g)             |     130   |
+--------------------------------------------------+
Pilih nomor detail makanan (0 untuk berhenti): 1

```

### 2. Quiz Makanan 🎮
Kuis kalori makanan tersedia dalam 3 level:
- Easy 🌱 → Benar/Salah
- Normal 🏆 → Pilih jawaban dari 4 pilihan
- Hard 🔥 → Masukkan nilai kalori langsung

**Contoh Easy:**
```

Apakah dalam Nasi putih (100g) memiliki kalori sebanyak 130?

1. Benar
2. Salah
   Jawaban kamu: 1
   Jawabanmu tepat sekali! Karena Nasi putih memiliki 130 kkal.

```

### 3. Hitung BMI 💪
Menghitung Body Mass Index (BMI) dan mengklasifikasikan kategori:
- Berat Badan Kurang
- Normal
- Berlebih
- Obesitas Kelas I–III

Data BMI disimpan di `riwayat.txt`.

**Contoh:**
```

Masukkan Entry ID: user01
Masukkan Berat Badan (kg): 65
Masukkan Tinggi Badan (cm): 170
Nilai BMI Anda: 22.49
Kategori: Berat Badan Normal

```

### 4. Workout Plan 💪
Rekomendasi latihan sesuai kategori BMI atau level pengguna.  
Fitur ini membaca ID dari `riwayat.txt` dan menampilkan latihan yang sesuai.

### 5. Rencana Kalori Harian 🔥
Menghasilkan rencana makan harian acak sesuai target kalori.  
Menampilkan total kalori dan makronutrien (protein, karbohidrat, lemak).

**Contoh:**
```

Target Kalori Harian: 2000 Kkal
Total Kalori Rencana: 1987 Kkal
Nama: Ayam panggang (100g)
Kalori: 165 kkal
Protein: 31g, Karbo: 0g, Lemak: 3.6g
...
Total Protein: 120g, Karbo: 200g, Lemak: 50g

```

### 6. Riwayat BMI 📚
Menampilkan daftar BMI yang telah dicatat, dengan ID, nilai BMI, kategori, dan kode.

**Contoh:**
```

## ID        BMI        Kategori              kode

user01    22.49      Berat Badan Normal    2

```

Pengguna juga bisa menghapus data riwayat berdasarkan ID.

### 7. Rencana Kebutuhan Cairan 💧
Menghitung kebutuhan cairan harian (liter dan jumlah gelas) berdasarkan berat badan dan tinggi badan.  
Membagi rekomendasi ke sesi pagi, siang, sore, dan malam.

**Contoh:**
```

Kebutuhan cairan per hari: 2.1 liter
Setara dengan: 8 gelas
Pagi  : 2 gelas
Siang : 2 gelas
Sore  : 2 gelas
Malam : 1 gelas

```

### 8. Progres Harian 📈
Memantau perkembangan kesehatan pengguna dari waktu ke waktu.  
(TODO: implementasi di `progress.py`)

### 9. Keluar ⛔
Menghentikan program dengan aman.

---

## Struktur Direktori

```

AP-9_Sahabat_Sehat/
│
├── main.py
├── README.md
├── requirements.txt
├── riwayat.txt
├── .gitignore
├── LICENSE
├── data/
│   └── foods.json
└── sahabat_sehat/
├── **init**.py
├── BMI.py
├── calory_control.py
├── decorasi.py
├── food.py
├── history.py
├── progress.py
├── quiz.py
├── water_plan.py
└── workout_plan.py

````

---

## Cara Menjalankan Aplikasi

1. Pastikan **Python 3.x** sudah terinstal.  
2. Clone repository:

```bash
git clone https://github.com/MochPutraFS/AP-9_Sahabat_Sehat.git
cd AP-9_Sahabat_Sehat
````

3. Jalankan aplikasi:

```bash
python main.py
```

4. Ikuti instruksi di menu aplikasi.

---

## Dependensi

* Menggunakan **modul bawaan Python**, jadi tidak perlu instalasi tambahan.
* Untuk fitur visualisasi progres, bisa menambahkan `matplotlib` atau `pandas` nanti.

---

## Lisensi

* MIT License (lihat file `LICENSE`).

---

## Kontributor

* AP-9 (Pengembang Sahabat Sehat)

```

---

Onii-chan, kalau mau Ais bisa buat **versi README dengan screenshot atau simulasi output lengkap tiap menu**, supaya dokumentasinya makin **interaktif dan menarik**.  

Onii-chan mau Ais buat versi itu juga?
```
