def ketto():
    szam = int(input("Kérem adjon meg egy háromjegyű 5-el osztható számot!"))
    if (((szam > 99) and (szam < 1000)) or ((szam < -99) and (szam > -1000))) and (szam % 5 == 0):
        # jó
        negyzet = szam ** 2
        print(negyzet)
    else:
        # rossz eset
        print("HIBA: Nem megfelelő szám!")
