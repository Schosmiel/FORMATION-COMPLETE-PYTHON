import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()

# Crée la table employees s'elle n'existe pas
c.execute("""
CREATE TABLE IF NOT EXISTS employees(
          prenom text,
          nom text,
          salaire int
)
""")

# Exemples de données à insérer
"""
donnees = [
    {"salaire": 20000, "prenom": "Richard", "nom": "GADJENOU"},
    {"salaire": 25000, "prenom": "Alice", "nom": "DUBOIS"},
    {"salaire": 30000, "prenom": "John", "nom": "SMITH"},
    {"salaire": 28000, "prenom": "Sarah", "nom": "WILLIAMS"},
    {"salaire": 22000, "prenom": "Michael", "nom": "JOHNSON"},
    {"salaire": 26000, "prenom": "Emily", "nom": "BROWN"},
    {"salaire": 31000, "prenom": "Daniel", "nom": "MARTINEZ"},
    {"salaire": 24000, "prenom": "Sophia", "nom": "GARCIA"},
    {"salaire": 27000, "prenom": "James", "nom": "DAVIS"},
    {"salaire": 29000, "prenom": "Olivia", "nom": "RODRIGUEZ"}
]
"""

# Insère les données dans la table
#for donnee in donnees:
#    c.execute("INSERT INTO employees VALUES(:prenom, :nom, :salaire)", donnee)


#d = {"salaire": 50000, "prenom": "Richard", "nom": "GADJENOU"}

# Effectue la mise à jour du salaire pour l'employé spécifié
#c.execute("""
#UPDATE employees SET salaire = :salaire WHERE prenom = :prenom AND nom = :nom """, d)


# Exemple : Supprimer un employé avec le prénom "Richard" et le nom "GADJENOU"
prenom_a_supprimer = "John"
nom_a_supprimer = "SMITH"

# Requête de suppression
c.execute("DELETE FROM employees WHERE prenom = ? AND nom = ?", (prenom_a_supprimer, nom_a_supprimer))



conn.commit()
conn.close()
