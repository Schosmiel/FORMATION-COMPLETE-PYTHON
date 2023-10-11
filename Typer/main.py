from ast import Delete
from click import Abort, echo
import typer

app = typer.Typer()

def main(delete: bool = typer.Option(False, help="Supprime les fichiers trouvés"), extension: str = typer.Argument("txt", help="Extension à chercher")):
    """
    Affiche les fichiers trouvés avec leurs données.
    """
    #extension = typer.echo(f"Recherche des fichiers avec l'extension {extension}")
    typer.echo(f"Recherche des fichiers avec l'extension {extension}")
    if delete:
        typer.echo("Suppression des fichiers.")

    """
    if delete:
        typer.confirm("Souhaitez-vous vraiment supprimer le fichier ?", abort=True)

    print("Suppression des fichiers")
    """

@app.command("search")
def search_py():
    # Vous pouvez implémenter la logique pour la commande search_py ici
    main(delete=True, extension="py")

@app.command("delete")
def delete_py():
    # Vous pouvez implémenter la logique pour la commande delete_py ici
    main(delete=False, extension="py")

if __name__ == "__main__":
    app()
