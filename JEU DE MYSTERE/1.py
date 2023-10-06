from random import randint

print("JEU DE MYSTERE")
prediction = randint(0, 100)

for i in range(1, 6):
    try:
        a = int(input("Choisissez un nombre : "))
        if prediction == a:
            print("Bravo ! Vous avez gagné.")
            break
        else:
            print("Ouf, devinez encore")
    except ValueError:
        print("Vous avez entré une valeur erronée")
    
    b = 5 - i  # Met à jour le nombre d'essais restants
    print("Il vous reste", b, "essai(s)")

else:
    print("Vous n'avez plus d'essais. Le nombre mystère était", prediction)
