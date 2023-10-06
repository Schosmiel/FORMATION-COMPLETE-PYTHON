while True:
    try:
        t=float(input("nombre 1 :"))
        b=float(input("nombre 2 :"))
        res=t+b
        print(t, "+", b, "=", round(res))
        break
    except ValueError:
        print("Stisie invtlide !")
    