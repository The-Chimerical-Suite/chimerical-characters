from pathlib import Path
from typing import Annotated, Optional
from typer import Context, Typer, Option, Argument
from rich import print

from chimerical_characters.data.appdata import add_character, delete_all_characters, delete_character, load_characters


app = Typer(no_args_is_help=True)


@app.callback()
def callback():
    """
    Manage your characters.
    """
    pass


@app.command()
def list():
    """List all characters."""
    chars = load_characters()
    for char in chars:
        print(char["name"])


@app.command()
def create(
    name: Annotated[str, Argument(help="The name of your character.")],
    species: Annotated[str, Option(prompt=True, help="The species of your character.")],
    level: Annotated[int, Option(help="The level of your character.")] = 1,
):
    """Create a new character."""
    add_character(name, species)
    print(f"Created character: {name}")


@app.command()
def delete(
    force: Annotated[
        bool,
        Option(
            "--force",
            "-f",
            prompt="Are you sure you want to delete the character?",
            help="Force deletion without confirmation.",
        ),
    ],
    name: Annotated[str, Argument(help="The name of the character to delete.")],
):
    """Delete an existing character."""
    if force:
        delete_character(name)
        print(f"Deleted character: {name}")
    else:
        print("Operation cancelled.")


@app.command()
def delete_all(
    force: Annotated[
        bool,
        Option(
            "--force",
            "-f",
            prompt="Are you sure you want to delete all characters?",
            help="Force deletion without confirmation.",
        ),
    ],
):
    """Delete all existing characters."""
    if force:
        delete_all_characters()
        print("Deleting all characters!")
    else:
        print("Operation cancelled.")
