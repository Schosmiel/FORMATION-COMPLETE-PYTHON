from pathlib import Path
from PIL import Image

from rembg import remove

#Pour indique le chemin courant de l'image
chemin=Path.cwd()

#Concatenez le chemin avec le nom de l'image
chemin=chemin/"images.jpg"


# Chemin d'entrée et de sortie
input_path = chemin
output_path = "output.png"

# Ouvrir l'image d'entrée
with Image.open(input_path) as input_image:
    # Supprimer l'arrière-plan
    output_image = remove(input_image)

    # Enregistrer l'image de sortie
    output_image.save(output_path)

print(f"L'image a été traitée avec succès et enregistrée sous {output_path}.")
