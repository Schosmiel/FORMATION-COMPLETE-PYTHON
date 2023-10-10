import json

fichier = "settings.json"

try:
    with open(fichier, "r") as f:
        settings = json.load(f)
    #print(settings)
except FileNotFoundError:
    print(f"Le fichier '{fichier}' n'a pas été trouvé.")
except json.JSONDecodeError:
    print(f"Erreur de décodage JSON dans le fichier '{fichier}'. Assurez-vous que le fichier est au format JSON valide.")
except Exception as e:
    print(f"Une erreur s'est produite : {e}")

settings["fontSize"]=15

with open(fichier, "w") as f:
    json.dump(settings, f, indent=4)

print()
