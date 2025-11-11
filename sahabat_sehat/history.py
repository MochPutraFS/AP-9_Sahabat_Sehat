from sahabat_sehat.BMI import program_bmi
FILE_NAME = 'riwayat.txt'

def input_history():
    print("\n=== Tambah Data History BMI ===")
    entry_id = input("Masukkan ID: ").strip()
    if not entry_id:
        print("ID tidak boleh kosong.")
        return
    bmi, kategori, kode = program_bmi()
    if not bmi or not kategori:
        print("Data tidak lengkap.")
        return

    try:
        f = open(FILE_NAME, 'a')
        f.write(f"{entry_id}|{bmi:.2f}|{kategori:20}\n")
        f.close()
        print("Data berhasil disimpan.")
    except:
        print("Gagal menyimpan data.")

def show_history():
    print("\n=== Daftar History BMI ===")
    try:
        f = open(FILE_NAME)
        lines = f.readlines()
        f.close()
    except:
        print("Belum ada data.")
        return

    if not lines:
        print("File kosong.")
        return

    print("-" * 40)
    print("{:<10} {:<10} {:<10}".format("ID", "BMI", "Kategori"))
    print("-" * 40)
    for l in lines:
        data = l.strip().split('|')
        if len(data) == 3:
            print("{:<10} {:<10} {:<10}".format(data[0], data[1], data[2]))
    print("-" * 40)

def delete_history():
    print("\n=== Hapus Data History ===")
    try:
        f = open(FILE_NAME)
        lines = f.readlines()
        f.close()
    except:
        print("Belum ada data.")
        return

    if not lines:
        print("File kosong.")
        return

    show_history()
    target_id = input("Masukkan ID yang ingin dihapus: ").strip()
    if not target_id:
        print("ID tidak boleh kosong.")
        return

    baru = []
    ditemukan = False
    for l in lines:
        if not l.startswith(target_id + "|"):
            baru.append(l)
        else:
            ditemukan = True

    if not ditemukan:
        print("ID tidak ditemukan.")
        return

    try:
        f = open(FILE_NAME, 'w')
        f.writelines(baru)
        f.close()
        print("Data berhasil dihapus.")
    except:
        print("Gagal menghapus data.")

def ambil_data(input_user):
    try:
        f = open(FILE_NAME)
        lines = f.readlines()
        f.close()
    except:
        print("Belum ada data.")
        return

    if not lines:
        print("File kosong.")
        return

    for l in lines:
        data = l.strip().split('|')
        if data[0] == (input_user-1):
            return data[1]
        else:
            print("ID tidak tidak ada.")