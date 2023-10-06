"""
### Pour lire le contenu d'un fichier
chemin= r"fichier.txt"


with open(chemin, 'r') as f:
    contenu=f.read()
    print(contenu)

"""
### Pour copier à l'interieur d'un fichier

chemin = "chemin_vers_le fichier//fichier.txt"

contenu="""
Apprendre un petit peu chaque jour est une méthode efficace. 
Des études ont montré que les participants qui ont établi une
routine d'apprentissage sont plus susceptibles d'atteindre 
leurs objectifs. Programmez-vous du temps pour apprendre et 
recevez des rappels grâce à votre planificateur d'apprentissage.
"""

try:
    with open(chemin, "w") as f:
        f.write(contenu)
    print("Le fichier a été créé et le texte a été écrit avec succès.")
except IOError as e:
    print(f"Une erreur s'est produite : {e}")

    


    