import string
import time 
import random 



y = str(input("------------------------------------------------------------------------" 
"             \nzadejte A pro zadání délku hesla nebo B pro manuální zadání délku hesla:... ")).upper()

if y == "A":
    délka = int(input("------------------------------" \
    "                   \nzadejte prosím délku heslo:... "))
    while délka > 10:
        print(f"tato délka ---{délka}---není možná zvolit ")
        délka = int(input("------------------------------" \
    "                   \nzadejte prosím délku heslo:... "))
        
    if délka <= 10:
        cisla = string.digits
        temp = random.sample(cisla, délka)
        heslo = "".join(temp)
        print(f"\nVygenerované heslo: {heslo}")



        # --- ZDE ZAČÍNÁ HÁDÁNÍ HESLA ---
        pocet_pokusu = 0
        start_time = time.time()
        print("\nSpouštím hádání hesla...")
        while True:
            pocet_pokusu += 1
            # Vygeneruje náhodný tip z proměnné 'all' o délce 'délka'
            pokus = "".join(random.choice(cisla) for _ in range(délka))

            # Průběžný výpis každých 50 000 pokusů
            if pocet_pokusu % 50000 == 0:
                print(f"Pokus #{pocet_pokusu:,}: zkouším '{pokus}'")

    
                # Když se tip shoduje s vygenerovaným heslem
                if pokus == heslo:
                    trvani = time.time() - start_time
                    print("\n" + "=" * 35)
                    print(f"🎉 Heslo úspěšně uhodnuto: {pokus}")
                    print(f"Počet pokusů: {pocet_pokusu:,}")
                    print(f"Čas: {trvani:.2f} sekund")
                    print("=" * 35)
                    break

elif y == "B":
    moje_heslo = (input("zadej svoje heslo: "))
    print("zadává se manuální hledání hesla od 1 -> n...")
    time.sleep(5)


    cisla = string.digits
    tip = len(moje_heslo)
    pokus = "".join(random.choice(cisla) for _ in range(tip)) 
        
    temp = random.sample(cisla, tip)

            # --- ZDE ZAČÍNÁ HÁDÁNÍ HESLA ---
    pocet_pokusu = 0
    start_time = time.time()
    print("\nSpouštím hádání hesla...")
    while True:
        pocet_pokusu += 1


        if pocet_pokusu % 10000 == 0:
            print(f"Pokus #{pocet_pokusu:,}: zkouším '{pokus}'")
            pokus = "".join(random.choice(cisla) for _ in range(tip)) 

            # Když se tip shoduje s vygenerovaným heslem
            if pokus == moje_heslo:
                trvani = time.time() - start_time
                print("\n" + "=" * 35)
                print(f"🎉 Heslo úspěšně uhodnuto: {pokus}")
                print(f"Počet pokusů: {pocet_pokusu:,}")
                print(f"Čas: {trvani:.2f} sekund")
                print("=" * 35)
                break