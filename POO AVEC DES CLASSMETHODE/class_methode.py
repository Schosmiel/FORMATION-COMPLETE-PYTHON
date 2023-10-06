class Voiture:
    voiture_cree=0
    def __init__(self, marque, vitesse, prix):
        Voiture.voiture_cree +=1
        self.marque= marque
        self.vitesse=vitesse
        self.prix=prix


    @classmethod
    def lamborghini(cls):
        return cls(marque="Lamborghini", vitesse=250, prix=500000)  

    @classmethod
    def porche(cls):
        return cls(marque="Porche", vitesse=200, prix=180000)
    
    @staticmethod
    def afficher_voiture_creer():
        print(f"Vous avez {Voiture.voiture_cree} dans votre garage.")
    
lambo=Voiture.lamborghini()
poch=Voiture.porche()
print(poch.vitesse)

Voiture.afficher_voiture_creer()