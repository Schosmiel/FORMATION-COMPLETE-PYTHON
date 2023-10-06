employes = {
    "Alice": "Ingénieur",
    "Bob": "Développeur",
    "Charlie": "Designer",
    "David": "Chef de projet",
    "Eva": "Analyste financier",
    "Frank": "Responsable des ventes",
    "Grace": "Ressources humaines",
    "Hugo": "Technicien de maintenance",
    "Ivy": "Marketing",
    "Jack": "Comptable"
}

is_true = True

while is_true:
    prenom = input("Employee : ")

    if prenom.isdigit():
        is_true = False
        print("Entree invalide ! Veuillez recommencer SVP.")
        break

    emploi = employes.get(prenom, "Employee {} est absent !".format(prenom))
    print(emploi)

    choix = input("Voulez-vous continuer ? O / N : ")
    if choix.lower() in ("n", "non"):
        print("A plus tard !")
        is_true = False
    elif choix.lower() in ("o", "oui"):
        is_true = True
    else:
        print("Entree invalide.")
        print("A plus tard !")
        is_true = False
    
