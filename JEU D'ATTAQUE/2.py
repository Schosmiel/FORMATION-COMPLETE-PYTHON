import random

# Définition des personnages
hero = {
    "name": "Héros",
    "health": 100,
    "attack": 20
}

enemy = {
    "name": "Ennemi",
    "health": 80,
    "attack": 15
}

# Fonction pour afficher l'état des personnages
def show_status():
    print(f"{hero['name']}: PV = {hero['health']} / PA = {hero['attack']}")
    print(f"{enemy['name']}: PV = {enemy['health']} / PA = {enemy['attack']}")

# Boucle de jeu
while hero['health'] > 0 and enemy['health'] > 0:
    show_status()
    print("\nQue voulez-vous faire ?")
    print("1. Attaquer")
    print("2. Prendre une potion")
    choice = input("Choisissez une action (1/2) : ")

    if choice == '1':
        # Attaque du héros
        hero_damage = random.randint(10, hero['attack'])
        enemy['health'] -= hero_damage
        print(f"Vous avez infligé {hero_damage} points de dégâts à l'ennemi!")

        # Attaque de l'ennemi
        enemy_damage = random.randint(5, enemy['attack'])
        hero['health'] -= enemy_damage
        print(f"L'ennemi vous a infligé {enemy_damage} points de dégâts!")

    elif choice == '2':
        # Prendre une potion
        potion_health = random.randint(15, 30)
        hero['health'] += potion_health
        print(f"Vous avez pris une potion et récupéré {potion_health} PV!")

    else:
        print("Choix invalide. Choisissez 1 ou 2.")

# Vérification des conditions de fin
if hero['health'] <= 0:
    print("Vous avez perdu! L'ennemi a gagné.")
else:
    print("Félicitations! Vous avez vaincu l'ennemi!")

print("Fin du jeu.")
