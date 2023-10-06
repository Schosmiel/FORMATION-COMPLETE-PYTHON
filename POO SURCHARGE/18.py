class Vehicule:
    def avance(self):
        print("Le véhicule démarre")
 
class Voiture(Vehicule):
    def roule(self):
        super().avance()
        print("La voiture roule")
 
class Avion(Vehicule):
    def vol(self):
        super().avance()
        print("L'avion vol")