class Voiture:
    voitureCree=0
    def __init__(self, marque):
        Voiture.voitureCree+=1
        self.marque=marque

Voiture_01=Voiture("Tesla")
Voiture_02=Voiture("Toyota")

Voiture_02.marque="Porche"

print(Voiture_01.marque)
print(Voiture_02.marque)
print(Voiture.voitureCree)

