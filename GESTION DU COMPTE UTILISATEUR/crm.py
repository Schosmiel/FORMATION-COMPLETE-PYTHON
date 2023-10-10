# Importation de la classe Faker depuis le module faker.
from faker import Faker

# Importation du module pour les expressions régulières.
import re

# Importation du module string pour manipuler les chaînes de caractères.
import string

# Importation de TinyDB, une base de données JSON, et de la fonction where.
from tinydb import TinyDB, where

# Importation de la classe Path depuis le module pathlib pour gérer les chemins de fichiers.
from pathlib import Path

# Définition de la classe User pour représenter un utilisateur.
class User:
    # Création d'une base de données TinyDB nommée "db.json" dans le répertoire du script.
    DB = TinyDB(Path(__file__).resolve().parent / "db.json", indent=4)

    # Méthode spéciale pour afficher une représentation textuelle de l'objet User.
    def __repr__(self):
        return f"User({self.first_name} {self.last_name})"

    # Constructeur de la classe User.
    def __init__(self, first_name: str, last_name: str, phone_number: str = "", address: str = ""):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address

    # Méthode spéciale pour afficher l'utilisateur sous forme de chaîne.
    def __str__(self):
        return f"{self.full_name}\n{self.phone_number}\n{self.address}"

    # Propriété pour obtenir le nom complet de l'utilisateur.
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # Méthode pour obtenir une instance de l'utilisateur depuis la base de données.
    @property
    def db_instance(self):
        return User.DB.get((where("first_name") == self.first_name) & (where("last_name") == self.last_name))

    # Méthode privée pour effectuer des vérifications sur les données de l'utilisateur.
    def _checks(self):
        self._check_phone_number()
        self._check_names()

    # Méthode privée pour vérifier la validité du numéro de téléphone.
    def _check_phone_number(self):
        phone_digits = re.sub(r"[+()\s]*", "", self.phone_number)
        if len(phone_digits) < 10 or not phone_digits.isdigit():
            raise ValueError(f"Numéro de téléphone {self.phone_number} invalide.")

    # Méthode privée pour vérifier que les noms ne contiennent pas de caractères spéciaux ou de chiffres.
    def _check_names(self):
        if not (self.first_name and self.last_name):
            raise ValueError("Le prénom et le nom de famille ne peuvent pas être vides.")
        special_characters = string.punctuation + string.digits
        for character in self.first_name + self.last_name:
            if character in special_characters:
                raise ValueError(f"Nom invalide {self.full_name}.")

    # Méthode pour vérifier si l'utilisateur existe dans la base de données.
    def exists(self):
        return bool(self.db_instance)

    # Méthode pour supprimer l'utilisateur de la base de données.
    def delete(self) -> list[int]:
        if self.exists():
            return User.DB.remove(doc_ids=[self.db_instance.doc_id])
        return []

# Fonction pour enregistrer un utilisateur dans la base de données.
def save(self, validate_data: bool = False) -> int:
    if validate_data:
        self._checks()
    if self.exists():
        return -1
    else:
        return User.DB.insert(self.__dict__)

# Fonction pour obtenir la liste de tous les utilisateurs dans la base de données.
def get_all_users():
    return [User(**user) for user in User.DB.all()]

if __name__ == "__main__":
    # Création d'un objet User appelé "schosmiel".
    schosmiel = User("Schosmiel", "DORFFICK")

    # Suppression de l'utilisateur "Schosmiel" de la base de données et affichage des identifiants supprimés.
    for i in schosmiel.delete():
        print(i)
