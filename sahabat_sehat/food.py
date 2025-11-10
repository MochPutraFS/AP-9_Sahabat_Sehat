FOODS = [
    {"id": 1,"name": "Nasi putih (100g)", "cal": 130, "protein": 2.7, "carb": 28, "fat": 0.3, "category": "Karbohidrat"},
    {"id": 2,"name": "Nasi merah (100g)", "cal": 111, "protein": 2.6, "carb": 23, "fat": 0.9, "category": "Karbohidrat"},
    {"id": 3,"name": "Roti tawar (1 iris)", "cal": 80, "protein": 3.0, "carb": 14, "fat": 1.0, "category": "Karbohidrat"},
    {"id": 4,"name": "Telur ayam (1 butir, 50g)", "cal": 78, "protein": 6.3, "carb": 0.6, "fat": 5.3, "category": "Protein Hewani"},
    {"id": 5,"name": "Ayam panggang (100g)", "cal": 165, "protein": 31, "carb": 0, "fat": 3.6, "category": "Protein Hewani"},
    {"id": 6,"name": "Ikan tuna (100g)", "cal": 132, "protein": 29, "carb": 0, "fat": 1.0, "category": "Protein Hewani"},
    {"id": 7,"name": "Tahu (100g)", "cal": 76, "protein": 8.1, "carb": 1.9, "fat": 4.8, "category": "Protein Nabati"},
    {"id": 8,"name": "Tempe (100g)", "cal": 192, "protein": 20.3, "carb": 7.6, "fat": 10.8, "category": "Protein Nabati"},
    {"id": 9,"name": "Sapi giling (100g)", "cal": 250, "protein": 26, "carb": 0, "fat": 17, "category": "Protein Hewani"},
    {"id": 10,"name": "Kentang rebus (100g)", "cal": 87, "protein": 2.0, "carb": 20.1, "fat": 0.1, "category": "Karbohidrat"},
    {"id": 11,"name": "Pisang (1 buah, 118g)", "cal": 105, "protein": 1.3, "carb": 27, "fat": 0.3, "category": "Buah"},
    {"id": 12,"name": "Apel (1 buah, 182g)", "cal": 95, "protein": 0.5, "carb": 25, "fat": 0.3, "category": "Buah"},
    {"id": 13,"name": "Susu rendah lemak (200ml)", "cal": 102, "protein": 6.8, "carb": 12, "fat": 2.4, "category": "Produk Susu"},
    {"id": 14,"name": "Yoghurt (plain, 100g)", "cal": 59, "protein": 10, "carb": 3.6, "fat": 0.4, "category": "Produk Susu"},
    {"id": 15,"name": "Keju cheddar (30g)", "cal": 120, "protein": 7, "carb": 0.4, "fat": 10, "category": "Produk Susu"},
    {"id": 16,"name": "Almond (30g)", "cal": 174, "protein": 6.4, "carb": 6.1, "fat": 15.2, "category": "Lemak Sehat"},
    {"id": 17,"name": "Minyak goreng (1 sdm)", "cal": 120, "protein": 0, "carb": 0, "fat": 14, "category": "Lemak"},
    {"id": 18,"name": "Soto ayam (1 mangkuk, 300g)", "cal": 250, "protein": 20, "carb": 10, "fat": 14, "category": "Makanan Campuran"},
    {"id": 19,"name": "Mie instan (1 bungkus)", "cal": 380, "protein": 7, "carb": 50, "fat": 16, "category": "Karbohidrat"},
    {"id": 20,"name": "Salad hijau (100g)", "cal": 15, "protein": 1.4, "carb": 2.9, "fat": 0.2, "category": "Sayur"},
    {"id": 21,"name": "Udang rebus (100g)", "cal": 99, "protein": 24, "carb": 0.2, "fat": 0.3, "category": "Protein Hewani"},
    {"id": 22,"name": "Daging kambing (100g)", "cal": 258, "protein": 25, "carb": 0, "fat": 17, "category": "Protein Hewani"},
    {"id": 23,"name": "Ikan salmon (100g)", "cal": 208, "protein": 20, "carb": 0, "fat": 13, "category": "Protein Hewani"},
    {"id": 24,"name": "Brokoli rebus (100g)", "cal": 35, "protein": 2.4, "carb": 7.2, "fat": 0.4, "category": "Sayur"},
    {"id": 25,"name": "Wortel rebus (100g)", "cal": 35, "protein": 0.8, "carb": 8.2, "fat": 0.2, "category": "Sayur"},
    {"id": 26,"name": "Oatmeal (100g)", "cal": 68, "protein": 2.4, "carb": 12, "fat": 1.4, "category": "Karbohidrat"},
    {"id": 27,"name": "Dada ayam rebus (100g)", "cal": 165, "protein": 31, "carb": 0, "fat": 3.6, "category": "Protein Hewani"},
    {"id": 28,"name": "Nugget ayam (100g)", "cal": 296, "protein": 15, "carb": 18, "fat": 18, "category": "Makanan Olahan"},
    {"id": 29,"name": "Sate ayam (5 tusuk, 100g)", "cal": 270, "protein": 25, "carb": 5, "fat": 16, "category": "Makanan Campuran"},
    {"id": 30,"name": "Sup sayur (1 mangkuk, 250g)", "cal": 90, "protein": 4, "carb": 14, "fat": 2, "category": "Sayur"}
]

def list_foods():
    x = f"|  {'No.':4}   |   {'Nama Makanan':30}   |   {'Kalori':7}  |"
    print('+', '-' * (len(x) - 4), '+')
    print(x)
    print('+', '-' * (len(x) - 4), '+')
    for i, f in enumerate(FOODS, 1):
        print(f"|  {i:4}   |   {f['name'][:30]:30}   |   {f['cal']:7}  |")
    print('+', '-' * (len(x) - 4), '+')

def show_food_detail():
    while True:
        try:
            index = int(input(f"\npilih nomor detail makanan (pilih 0 untuk berhenti) : "))
            if index == 0:
                print('🚫program terminate.')
                break
            elif 0 < index <= len(FOODS):
                f = FOODS[index - 1]
                x = (f"| Protein : {f['protein']:5}g | Karbo: {f['carbs']:5}g | Lemak: {f['fat']:7}g |")
                print("+", "-" * (len(x) - 4), '+')
                print(f"|  Nama   : {f['name']:30}{' ':11}|")
                print(f"|  Kalori : {f['cal']:3} kkal{' ':33}|")
                print("+", "-" * (len(x) - 4), '+')
                print(x)
                print("+", "-" * (len(x) - 4), '+')
            else:
                print('❌id tidak ditemukan.')
                continue
            
        except ValueError:
            print('‼️input tidak valid.')
            continue
