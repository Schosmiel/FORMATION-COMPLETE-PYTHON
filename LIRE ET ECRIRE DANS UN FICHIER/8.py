from pathlib import Path

chemin=Path.cwd()

chemin=chemin/"fichier_original.txt"

#print(chemin)

# Lire les noms depuis le fichier
with open(chemin, "r") as fichier_noms:
    noms = fichier_noms.read().splitlines()

# Trier les noms en ordre alphabétique
noms_tries = sorted(noms)

# Écrire les noms triés dans un nouveau fichier
with open("fichier_tri.txt", "w") as fichier_noms_tries:
    for nom in noms_tries:
        fichier_noms_tries.write(nom + "\n")

print("Les noms ont été triés et écrits dans fichier_tri.")
