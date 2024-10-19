def beolvas():
    oldal = float(input("Add meg a háromszög oldalát!"))
    return oldal

def hat():
    a = beolvas()
    b = beolvas()
    c = beolvas()

    if (a > 0 and b > 0 and c > 0):
        # jó
        if a<c+b and c<a+b and b<a+c:
            print("A háromszög megszerkeszthető.")
        else:
            print("A háromszög nem megszerkeszthető.")
    else:
        print("HIBA: Nem megfelelő bemenő adatok!")
