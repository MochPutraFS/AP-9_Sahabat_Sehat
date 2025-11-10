import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "data", "foods.json")

def load_foods():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

FOODS = load_foods()

def list_foods():
    x = f"|  {'No.':4}   |   {'Nama Makanan':30}   |   {'Kalori':7}  |"
    print('+', '-' * (len(x)-4), '+')
    print(x)
    print('+', '-' * (len(x)-4), '+')
    for i, f in enumerate(FOODS, 1):
        print(f"|  {i:4}   |   {f['name']:30}   |   {f['cal']:7}  |")
    print('+', '-' * (len(x)-4), '+')

def show_food_detail():
    while True:
        try:
            index = int(input(f"\npilih nomor detail makanan (pilih 0 untuk berhenti) : "))
            if index == 0:
                print('🚫program terminate.')
                break
            elif index > 0 and index <= len(FOODS):
                f = FOODS[index - 1]
                x = (f"| Protein : {f['protein']:5}g | Karbo: {f['carb']:5}g | Lemak: {f['fat']:7}g |")
                print("+", "-" * (len(x) - 4), '+')
                print(f"|  Nama   : {f['name']:30}{' ':11}|")
                print(f"|  Kalori : {f['cal']:3} kkal{' ':33}|")
                print("+", "-" * (len(x) - 4), '+')
                print(x)
                print("+", "-" * (len(x) - 4), '+')
            elif index <0 or index > len(FOODS):
                print('❌id tidak ditemukan.')
                continue

        except ValueError:
            print('‼️input tidak valid.')
            continue