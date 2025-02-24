from dataclasses import dataclass
from json import dump, load, JSONDecoder, JSONEncoder
from pathlib import Path

from chimerical_characters.utils import get_app_dir

APPDATA = get_app_dir("chimerical")


def load_appdata():  # -> tuple[Compendium, Characters]:
    with (APPDATA / "compendium.json").open() as f:
        compendium = load(f)
    with (APPDATA / "characters.json").open() as f:
        characters = load(f)
    return compendium, characters


def load_characters():
    with (APPDATA / "characters.json").open() as f:
        characters: list = load(f)
    return characters


def write_characters(new_characters: list[dict]):
    with (APPDATA / "characters.json").open("w") as f:
        dump(new_characters, f)


def add_character(name: str, species: str):
    characters: list = load_characters()
    if name not in [char["name"] for char in characters]:
        new_char = make_character(name=name, species=species)
        characters.append(new_char)
    write_characters(characters)


def delete_character(name: str):
    characters: list = load_characters()
    new_characters = list(filter(lambda char: char["name"] != name, characters))
    write_characters(new_characters)


def delete_all_characters():
    write_characters([])


def make_character(*, name: str, species: str) -> dict:
    return {"name": name, "species": species}


if __name__ == "__main__":
    print("STARTING...")
    compendium, characters = load_appdata()
    print("FINISHED!")
    print("Compendium:")
    print(compendium)
    print("Characters:")
    print(characters)
