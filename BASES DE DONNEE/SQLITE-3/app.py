import sqlite3



conn = sqlite3.connect("database.db")
c=conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS employee(
          prenom text,
          nom text
)
""")
#d={"prenom": "paul", "nom": "Dupond"}
#c.execute("INSERT INTO employee VALUES(:prenom, :nom)", d )


d={"a": "paul"}
c.execute("SELECT * FROM employee WHERE prenom=:a", d)

donnee=c.fetchall()

print(f"{donnee}")

conn.commit()
conn.close()

