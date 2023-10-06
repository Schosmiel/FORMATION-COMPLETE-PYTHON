#Polymorphisme

class Vehicule:
    def avance(self):
        print("Véhicule démarré")

class Voiture(Vehicule):
    def avance(self):
        super().avance()
        print("La voiture roule")

class Avion(Vehicule):
    def avance(self):
        super().avance()
        print("L'avion vol")

v=Voiture()
a=Avion()
v.avance()
a.avance()