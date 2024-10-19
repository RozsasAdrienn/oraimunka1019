def wod():
    # Írd ki az első 10 Woodal számot!
    # https: // hu.wikipedia.org / wiki / Woodall - sz % C3 % A1mok
    print("Woodal számok: ", end="")
    n= 1
    db=0
    while db<10:
        if n>0:
            wn= n*pow(2,n)-1
            if db != 9:
                print(str(wn)+", ", end="")
            else:
                print(str(wn))
            db += 1
        n=n+1
