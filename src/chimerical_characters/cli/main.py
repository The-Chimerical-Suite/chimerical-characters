"""The main command line interface with the application."""

from pathlib import Path
from typer import Typer
from rich import print

from chimerical_characters.data.appdata import load_appdata

from .admin import app as admin_app
from .characters import app as characters_app


app = Typer(no_args_is_help=True)  # invoke_without_command
app.add_typer(admin_app, name="admin")
app.add_typer(characters_app, name="characters")

@app.callback()
def callback():
    """
    Welcome to the command line interface of Chimerical Characters.
    """
    pass

@app.command()
def compendium():
    """
    Read the compendium.
    """
    print("Reading the compendium!")
    compendium, characters = load_appdata()
    print("Compendium: ", compendium)
    print("Characters: ", characters)
