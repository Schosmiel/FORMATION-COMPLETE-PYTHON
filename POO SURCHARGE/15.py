#Surcharge

projets=["pr_GameOfTrone", "Harry Potter", "pr_Avenger"]

class Utilisateur:
    def __init__(self, nom, prenom):
        self.nom=nom
        self.prenom=prenom
    def __str__(self):
        return f"Utilisateur {self.nom} {self.prenom}"
    
    def afficher_projet(self):
        for projet in projets:
            print(projet)


class Junior(Utilisateur):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)



    def afficher_projet(self):
        for projet in projets:
            if not projet.startswith("pr_"):
                print(projet)
      
paul=Junior("Paul", "Durant")
paul.afficher_projet()


