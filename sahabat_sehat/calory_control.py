import random
from sahabat_sehat.food import FOODS

MIN_CALORIES = 1500
MAX_CALORIES = 2500
TOLERANCE = 100 

def get_calorie_input():
    """
    Meminta input kalori dari user dan memvalidasi rentangnya.
    """
    while True:
        try:
            print(f"\nMasukkan batas kalori harian yang Anda inginkan (antara {MIN_CALORIES} dan {MAX_CALORIES} Kkal):")
            cal_input = input(">> ")
            target_calories = int(cal_input)

            if target_calories < MIN_CALORIES or target_calories > MAX_CALORIES:
                print(f"\n❌ Input kalori **{target_calories} Kkal** di luar rentang yang disarankan.")
                print(f"   Mohon masukkan nilai antara **{MIN_CALORIES}** hingga **{MAX_CALORIES} Kkal** untuk menjaga keseimbangan gizi.")
            else:
                return target_calories
        except ValueError:
            print("\n❌ Input tidak valid. Mohon masukkan angka bilangan bulat saja.")
        except EOFError:
            print("\nInput dibatalkan.")
            return None

def generate_meal_plan(target_calories):
    """
    Menghasilkan rencana makan acak yang mendekati target kalori.
    """
    recommended_foods = []
    current_calories = 0
    available_foods = list(FOODS)

    print("\n⏳ Mencari kombinasi makanan terbaik secara acak...")
    
    while current_calories < target_calories:
        if not available_foods:
            print("❗ Semua makanan telah direkomendasikan.")
            break

        food_choice = random.choice(available_foods)
        
        available_foods.remove(food_choice)

        if current_calories + food_choice['cal'] > target_calories + TOLERANCE:
            continue 

        recommended_foods.append(food_choice)
        current_calories += food_choice['cal']

        if target_calories - current_calories <= TOLERANCE and current_calories >= target_calories - TOLERANCE:
             break

    return recommended_foods, current_calories

def display_recommendation(foods, total_cal, target_cal):
    """
    Menampilkan hasil rekomendasi makanan.
    """
    print("\n" + "="*50)
    print("✨ Rekomendasi Rencana Makanan Harian Anda ✨")
    print(f"Target Kalori Harian: **{target_cal} Kkal**")
    print(f"Total Kalori Rencana: **{total_cal} Kkal**")
    print("-" * 50)
    
    if not foods:
        print("Tidak dapat membuat rencana makan yang memadai dengan kalori yang tersedia.")
        return

    total_protein = sum(f['protein'] for f in foods)
    total_carb = sum(f['carb'] for f in foods)
    total_fat = sum(f['fat'] for f in foods)
    tcal = sum(f['cal'] for f in foods)

    print("## 🍽️ Detail Makanan yang Direkomendasikan:")
    for f in foods:
        x = (f"| Protein : {f['protein']:5}g | Karbo: {f['carb']:5}g | Lemak: {f['fat']:7}g |")
        print("+", "-" * (len(x) - 4), '+')
        print(f"|  Nama   : {f['name']:30}{' ':11}|")
        print(f"|  Kalori : {f['cal']:3} kkal{' ':33}|")
        print("+", "-" * (len(x) - 4), '+')
        print(x)
        print("+", "-" * (len(x) - 4), '+')

    print("\n## 📊 Total Makronutrien:")
    print(f"* Protein: **{total_protein:.1f} g**")
    print(f"* Karbohidrat: **{total_carb:.1f} g**")
    print(f"* Lemak: **{total_fat:.1f} g**")
    print(f"{tcal}")
    
    print("="*50)
    print(f"Catatan: Rencana ini mendekati target Anda ({target_cal} Kkal).")
    print("Ini adalah contoh rencana acak. Untuk rencana yang lebih spesifik, pertimbangkan pembagian waktu makan.")
    
def main():
    target_calories = get_calorie_input()

    if target_calories is None:
        return

    recommended_foods, total_calories = generate_meal_plan(target_calories)
    display_recommendation(recommended_foods, total_calories, target_calories)

