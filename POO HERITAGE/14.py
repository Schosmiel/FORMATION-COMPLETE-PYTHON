#Héritage

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
        #Utilisateur.__init__(self, nom, prenom) #ou ci déssous
        super().__init__(nom, prenom)


      
paul=Junior("Paul", "Durant")

#paul.afficher_projet()
print(paul)

