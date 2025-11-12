from sahabat_sehat.food import list_foods, show_food_detail, FOODS
from sahabat_sehat.quiz import quiz_Normal, quiz_Easy, quiz_Hard
from sahabat_sehat.decorasi import decorate, validasi_menu, validasi_quiz, validasi_tipe_quiz
from sahabat_sehat.BMI import program_bmi, input_history
from sahabat_sehat.progress import menu_progres
from sahabat_sehat.workout_plan import workout_plan
from sahabat_sehat.history import return_id, show_history, delete_history, return_id
from sahabat_sehat.calory_control import main, display_recommendation, generate_meal_plan, get_calorie_input
from sahabat_sehat.water_plan import water_plan

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
    print('9. 📈Progres Harian')
    print('10. ⛔Keluar')

    ansa = input("Pilih Menu : ")
    pilih = str(validasi_menu(ansa,10))

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
        input_history()

    elif pilih == '4':
        kode = return_id()
        workout_plan(kode)

    elif pilih == '5':
        main()

    elif pilih == '6':
        show_history()

    elif pilih == '7':
        delete_history()

    elif pilih == '8':
        water_plan()
    
    elif pilih == '9':
        menu_progres()

    elif pilih == '10':
        print('program dihentikan.')
        break