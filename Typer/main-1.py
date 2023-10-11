# Importez la bibliothèque Typer pour créer une interface en ligne de commande (CLI)
import typer

# Importez les modules nécessaires
from typing import Optional
from pathlib import Path

# Créez une instance de l'application Typer
app = typer.Typer()

# Définissez une commande nommée "run"
@app.command("run")
def main(extension: str,
         directory: Optional[str] = typer.Argument(None, help="Dossier dans lequel vous cherchez."),
         delete: bool = typer.Option(False, help="Supprimez les fichiers trouvés")):
    """
    Afficher les fichiers trouvés avec les extensions données.
    """
    # Si un répertoire est spécifié, créez un objet Path avec ce répertoire, sinon utilisez le répertoire de travail actuel
    if directory:
        directory = Path(directory)
    else:
        directory = Path.cwd()

    # Affiche un message d'information
    print(f"Recherche de fichiers avec l'extension '{extension}' dans le dossier '{directory}'")

    # Vérifiez si le répertoire spécifié existe
    if not directory.exists():
        typer.secho(f"Le dossier '{directory}' n'existe pas", fg=typer.colors.RED)
        raise typer.Exit()
    
    # Utilisez rglob pour rechercher tous les fichiers avec l'extension donnée récursivement dans le répertoire
    files = list(directory.rglob(f"*.{extension}"))
    
    # Si l'option "delete" est activée
    if delete:
        # Si aucun fichier n'est trouvé, affichez un message
        if not files:
            typer.secho("Aucun fichier trouvé avec l'extension spécifiée.", fg=typer.colors.YELLOW)
        else:
            # Demandez confirmation avant de supprimer les fichiers trouvés
            typer.confirm("Voulez-vous vraiment supprimer tous les fichiers trouvés?", abort=True)
            # Parcourez les fichiers et supprimez-les
            for file in files:
                file.unlink()
                typer.secho(f"Suppression du fichier {file}.", fg=typer.colors.RED)
    # Si l'option "delete" est désactivée
    else:
        # Si aucun fichier n'est trouvé, affichez un message
        if not files:
            typer.secho(f"Aucun fichier trouvé avec l'extension '{extension}'.", fg=typer.colors.YELLOW)
        else:
            # Affichez les fichiers trouvés
            typer.secho(f"Fichiers trouvés avec l'extension '{extension}':", bg=typer.colors.BLUE, fg=typer.colors.WHITE)
            for file in files:
                typer.echo(file)

# Définissez une commande "search" pour rechercher des fichiers sans les supprimer
@app.command()
def search(extension: str, directory: Optional[str] = None):
    main(extension=extension, directory=directory, delete=False)

# Définissez une commande "delete" pour rechercher et supprimer des fichiers
@app.command()
def delete(extension: str, directory: Optional[str] = None):
    main(extension=extension, directory=directory, delete=True)

# Exécutez l'application Typer
if __name__ == "__main__":
    app()
