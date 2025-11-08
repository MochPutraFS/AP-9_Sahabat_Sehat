from food import list_foods, show_food_detail
from quiz import quiz_Normal,quiz_Easy, quiz_Hard
from decorasi import decorate, validasi_menu, validasi_quiz, validasi_tipe_quiz
from food import FOODS

decorate()
while True:
    print('\nMenu:')
    print('1. 🍱Lihat makanan')
    print('2. 🍕Quiz makanan')
    print('3. 💪Hitung BMI')
    print('4. 💪workout plan')
    print('5. 🔥Rencana kalori harian')
    print('6. 📚Lihat riwayat BMI')
    print('7. 📚Bersihkan riwayat BMI')
    print('8. 💧Rencana kebutuhan cairan')
    print('9. ⛔Keluar')

    ansa = input("Pilih Menu : ")
    pilih = str(validasi_menu(ansa,8))

    if pilih == '1':
        list_foods()
        show_food_detail()

    elif pilih == '2':
        tipe = validasi_tipe_quiz()
        if tipe == 4:
            continue
        num = validasi_quiz(len(FOODS))
        if tipe == 1:
            quiz_Easy(num)
        elif tipe == 2:
            quiz_Normal(num)
        elif tipe == 3:
            quiz_Hard(num)
    elif pilih == '3':
        pass

    elif pilih == '4':
        pass

    elif pilih == '5':
        pass

    elif pilih == '6':
        pass

    elif pilih == '7':
        pass

    elif pilih == '8':
        pass

    elif pilih == '9':
        print('program dihentikan.')
        break