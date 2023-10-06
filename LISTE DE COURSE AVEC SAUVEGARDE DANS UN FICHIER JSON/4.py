import json

# Fonction pour charger la liste de courses depuis un fichier JSON
def charger_liste():
    try:
        with open("liste_de_courses.json", "r") as fichier:
            return json.load(fichier)
    except FileNotFoundError:
        return []

# Fonction pour enregistrer la liste de courses dans un fichier JSON
def enregistrer_liste(liste):
    with open("liste_de_courses.json", "w") as fichier:
        json.dump(liste, fichier)

# Fonction principale pour gérer la liste de courses
def gerer_liste():
    liste_de_courses = charger_liste()

    while True:
        print("Liste de courses :")
        for index, item in enumerate(liste_de_courses, start=1):
            print(f"{index}. {item}")

        print("\nOptions :")
        print("1. Ajouter un element")
        print("2. Supprimer un element")
        print("3. Quitter")

        choix = input("Selectionnez une option : ")

        if choix == "1":
            nouvel_element = input("Entrez un nouvel élément : ")
            liste_de_courses.append(nouvel_element)
            enregistrer_liste(liste_de_courses)
            print(f"{nouvel_element} a été ajouté à la liste de courses.")
        elif choix == "2":
            try:
                indice = int(input("Entrez le numéro de l'élément à supprimer : ")) - 1
                if 0 <= indice < len(liste_de_courses):
                    element_supprime = liste_de_courses.pop(indice)
                    enregistrer_liste(liste_de_courses)
                    print(f"{element_supprime} a été supprimé de la liste de courses.")
                else:
                    print("Numéro d'élément invalide.")
            except ValueError:
                print("Veuillez entrer un numéro valide.")
        elif choix == "3":
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")

if __name__ == "__main__":
    print("Bienvenue dans la gestion de liste de courses !")
    gerer_liste()
