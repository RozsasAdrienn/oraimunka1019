import math
def ot():
    # Kérj be egy [40, 95] intervallumban lévő egész számot (ha nem ebben az intervallumban van, jelezz hibát!), majd írasd ki az első számjegyét!
    szam = int(input("Kérem adjon meg egy 40 és 95 közötti számot!"))
    if szam <40 or szam > 95:
        print("HIBA: nem megflelő szám!")
    else:
        # megoldás1: szöveggé konvertálás, szövegkezelés, nem tanultuk
        szam = str(szam)
        print(szam[0])

        # megoldás2:
        szam = int(szam)
        print(str(int(szam/10)))

        #megoldás3:
        szam = int(szam)
        print(str(math.floor(szam/10)))