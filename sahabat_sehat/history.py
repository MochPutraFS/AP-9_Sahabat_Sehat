FILE_NAME = 'riwayat.txt'

def show_history():
    print("\n=== Daftar History BMI ===")
    try:
        f = open(FILE_NAME)
        lines = f.readlines()
        f.close()
    except:
        print("‼️Belum ada data.")
        return

    if not lines:
        print("Data kosong.")
        return

    print("-" * 50)
    print("{:<10} {:<10} {:<20} {:<10}".format("ID", "BMI", "Kategori", "kode"))
    print("-" * 50)
    for l in lines:
        data = l.strip().split('|')
        if len(data) == 4:
            print("{:<10} {:<10} {:<10} {:<10}".format(data[0], data[1], data[2], data[3]))
    print("-" * 50)

def delete_history():
    print("\n=== Hapus Data History ===")
    try:
        f = open(FILE_NAME)
        lines = f.readlines()
        f.close()
    except:
        print("‼️Belum ada data.")
        return

    if not lines:
        print("File kosong.")
        return

    show_history()
    target_id = input("Masukkan ID yang ingin dihapus: ").strip()
    if not target_id:
        print("‼️ID tidak boleh kosong.")
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
        print("‼️Gagal menghapus data.")

def return_id():
    try:
        with open(FILE_NAME, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Belum ada data.")
        return

    if not lines:
        print("File kosong.")
        return

    show_history()
    target_id = input("Masukkan ID untuk jadwal workout : ").strip()

    if not target_id:
        print("ID tidak boleh kosong.")
        return

    content = "|".join([line.strip() for line in lines])
    data = content.split('|')

    for i in range(0, len(data), 4):
        if data[i] == target_id:
            try:
                kode = data[i + 3]
                return int(kode)
            except (IndexError, ValueError):
                print("Format data tidak valid.")
                return

    print("ID tidak ditemukan.")
    return







