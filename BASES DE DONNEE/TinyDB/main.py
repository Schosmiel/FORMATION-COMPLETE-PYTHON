from textwrap import indent
from tinydb import Query, TinyDB, where

# Crée ou ouvre la base de données "data.json" avec une indentation de 4 espaces
db = TinyDB("data.json", indent=4)

# Insère des données dans la base de données
db.insert({"Name": "Patric", "Score": 10})

db.insert_multiple([
    {"Name": "Richard", "Score": 100},
    {"Name": "Alice", "Score": 20},
    {"Name": "John", "Score": 45},
    {"Name": "Emily", "Score": 12},
    {"Name": "Michael", "Score": 75},
    {"Name": "Sophia", "Score": 98},
    {"Name": "Daniel", "Score": 33},
    {"Name": "Olivia", "Score": 56},
    {"Name": "James", "Score": 88},
    {"Name": "Sarah", "Score": 62}
])

# Définit une requête (Query) pour effectuer des recherches dans la base de données
User = Query()

# Recherche un utilisateur avec le nom "Patric"
patrick = db.search(User.Name == "Patric")
patrick_unique = db.get(User.Name == "Patric")

# Recherche des utilisateurs avec un score supérieur à 50
high_score = db.search(where("Score") > 50)

# Met à jour le score de "Richard" à 10
db.update({"Score": 10}, User.Name == "Richard")

# Mise à jour de la base de données pour inclure la clé "roles" pour "Richard"
db.upsert({"Name": "Richard", "Score": 50, "roles": ["Senior"]}, User.Name == "Richard")
