from dataclasses import dataclass
"""
class Livre:
    def __init__(self, nom, nombre_de_page, prix):
        self.nom = nom
        self.nombre_de_page = nombre_de_page
        self.prix = prix
livre_HP=Livre("Henry Potter", 300, 10.99)

livre_LOTR=Livre("Le seigneur des angneaux", 400, 13.99)

"""

@dataclass
class Livre:
    nom : str
    nombre_de_page : int
    prix : float
livre_HP=Livre("Henry Potter", 300, 10.99)

livre_LOTR=Livre("Le seigneur des angneaux", 400, 13.99)


print(livre_HP.nom)
print(livre_HP.nombre_de_page)
print(livre_HP.prix)