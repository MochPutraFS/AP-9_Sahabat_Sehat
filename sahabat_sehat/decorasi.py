def decorate():
    decorate = '|                    WELCOME                    |'
    print('='*len(decorate))
    print(decorate)
    print('='*len(decorate))
    print(' '*len(decorate))
    print('|                 SAHABAT SEHAT                 |')
    print('|               this application                |')
    print('|            for control your health            |')
    print('|         == this code fully by ap 9 ==         |')
    print(' '*len(decorate))
    print('='*len(decorate))
    print(' '*len(decorate))
    print('='*len(decorate))

def validasi_menu(ans, angka):
    while True:
        try:
            ans = int(ans)
            if ans < 1 or ans > angka:
                print("❌Menu tidak ada.")
                break
            else:
                return ans
        except ValueError:
            print("‼️input tidak valid.")
            break


def validasi_quiz(angka):
    while True:
        try:
            ans = int(input('berapa soal yang ingin anda kerjakan??\n banyak soal = '))
            if ans < 1 or ans > angka:
                print("❌Soal terlalu banyak.")
                continue
            else:
                return ans
        except ValueError:
            print("‼️input tidak valid.")
            continue

def validasi_tipe_quiz():
    while True:
        try:
            tipe = int(input("\ntipe soal??\n1.Easy level    🟢\n2.Normal level  🟡\n3.Hard level    🔴\n4.⛔stop program\njawaban kamu :"))
            if tipe == 4:
                return tipe
            elif tipe > 30:
                print('soal terlalu banyak.')
                continue
            elif tipe < 1 or tipe > 3 and tipe != 4:
                print("❌pilihan tidak tersedia.")
                continue
            else:
                return tipe

        except ValueError:
            print("‼️input tidak valid.")
            continue

def validasi_user_water():
    while True:
        try:
            ans = int(input('masukkan id pemilik BMI :'))
            return ans

        except ValueError:
            print("‼️input tidak valid.")
            break