import random
from food import FOODS

def quiz_Normal(n):
    questions = random.sample(FOODS, n)
    score = 0

    print("\n=== 🎮Quiz Normal Level🏆 ===")

    for i, q in enumerate(questions):
        name = q['name']
        correct = q['cal']

        choices = [correct]
        while len(choices) < 4:
            c = random.choice(FOODS)['cal']
            choices.append(c)
        random.shuffle(choices)

        print(f"{i+1}. Berapa kalori dalam {name}?")
        for j, opt in enumerate(choices):
            print(f"   {j+1}. {opt} kkal")

        try:
            ans = int(input("Jawaban kamu (1-4): "))
            if ans < 1 or ans > 4:
                print("‼️Pilihan tidak valid\n❌Jawaban kamu otomatis salah.")
                continue
        except ValueError:
            print("⚠️Masukkan angka 1-4.")
            continue

        if choices[ans - 1] == correct:
            print("Benar!")
            score += 1
        else:
            print(f"Salah. Jawaban benar: {correct} kkal.")

    print(f"\nSkor akhir kamu: {score}/{n}")

def quiz_Easy(n):
    print("\n=== 🎮Quiz Easy Level🌱 ===")
    questions = random.sample(FOODS, n)
    score = 0

    for j,p in enumerate(questions):
        name = p['name']
        correct = p['cal']
        choices = [correct]
        while len(choices) < 2:
            c = random.choice(FOODS)['cal']
            choices.append(c)
        random.shuffle(choices)
        print(f'\napakah dalam {name} memiliki kalori sebanyak {choices[0]}??')
        print('1.Benar')
        print('2.Salah')
        try:
            ans = int(input("Jawaban kamu : "))
            if ans < 1 or ans > 2:
                print("‼️Pilihan tidak valid\n❌Jawaban kamu otomatis salah.")
                continue
        except ValueError:
            print("⚠️Input tidak valid.")
            continue

        if choices[ans - 1] == correct:
            print(f"Jawabanmu tepat sekali!\nkarena {name} memiliki {correct} kkal.")
            score += 1
        else:
            if choices[ans - 1] != correct:
                choices[ans - 1] = "SALAH"
                print(f"Jawaban yang tepat adalah : {choices[ans - 1]} \nkarena {name} memiliki {correct} kkal.")
    print(f"\nSkor akhir kamu: {score}/{n}")

def quiz_Hard(n):
    questions = random.sample(FOODS, n)
    score = 0

    print("\n=== 🎮Quiz Hard Level🔥 ===")

    for i, q in enumerate(questions):
        name = q['name']
        correct = q['cal']

        print(f"{i+1}. Berapa banyak kalori dalam {name}?")

        try:
            ans = int(input("Jawaban kamu (kkal) : "))
        except ValueError:
            print("⚠️Masukkan angka Jawaban kamu otomatis salah.")
            continue

        if ans == correct:
            print("Benar!")
            score += 1
        else:
            print(f"Salah. Jawaban benar: {correct} kkal.")

    print(f"\nSkor akhir kamu: {score}/{n}")
