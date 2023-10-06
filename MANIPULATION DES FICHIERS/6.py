from pathlib import Path

p=Path("nom_du_dossier\\Demande.pdf")


lien_vers_le_fichier=p.parent
nom = p.name
nom_brut_du_fichier=p.stem
suff=p.suffix
subdivision=p.parts

print("\n")
print("Dossier parent : ", lien_vers_le_fichier, "\n")
print("Nom du fichier : ",nom, "\n")
print("Index du fichier : ",nom_brut_du_fichier, "\n")
print("Suffix di fichier : ",suff, "\n")
print("Chaque subdivision :",subdivision, "\n")
print("\n")





