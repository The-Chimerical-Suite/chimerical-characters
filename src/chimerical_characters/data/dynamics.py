from dataclasses import dataclass
from typing import NamedTuple

from chimerical_characters.data.statics import Background, Class, Creature, Item, Species

class Scores(NamedTuple):
    STR : int
    DEX : int
    CON : int
    INT : int
    WIS : int
    CHA : int


@dataclass
class Level(object):
    hp_on_die : int 
    class_ : str                   # Class identifier
    class_choices : list[str]      # Class Choice identifiers
    species_choices : list[str]    # Species Choice identifiers
    background_choices : list[str] # Background Choice identifiers

@dataclass(kw_only=True, slots=True)
class HP(object):
    now : int
    max : int
    temp : int

@dataclass(kw_only=True, slots=True)
class HD(object):
    now : int
    max : int
    die : int

@dataclass(kw_only=True, slots=True)
class DeathSaves(object):
    successes : int
    failures : int


@dataclass(slots=True)
class Stats(object):
    scores : Scores
    # save_profs : list[str]
    # skill_profs : list[str]
    

    @staticmethod
    def mkmod(score: int):
        """Determines the ability modifier from the ability score."""
        return (score - 10) // 2

@dataclass
class Buff(object):
    scores : Scores

@dataclass(slots=True)
class ArmourProficiency(object):
    light : bool
    medium : bool
    heavy : bool
    shields : bool

@dataclass(slots=True)
class WeaponProficiency(object):
    simple : bool
    martial : bool
    simple_melee : bool
    simple_ranged : bool
    martial_melee : bool
    martial_ranged : bool
    
    club : bool

@dataclass(slots=True)
class SkillProficiency(object):
    Acrobatics : bool
    Animal_Handling : bool
    Arcana : bool
    Athletics : bool
    Deception : bool
    History : bool
    Insight : bool
    Intimidation : bool
    Investigation : bool
    Medicine : bool
    Nature : bool
    Perception : bool
    Performance : bool
    Persuasion : bool
    Religion : bool
    Sleight_of_Hand : bool
    Stealth : bool
    Survival : bool

class Proficiency(object):
    armour : ArmourProficiency
    weapons : WeaponProficiency
    skills : SkillProficiency

class BigCharacter(object):
    """
    A character.
    """
    def __init__(self, name:str, background:Background, species:Species, xp:int, classes:list[Class], base_scores:Scores, creatures=[], inventory=[], levels={}):
        self.name : str = name
        self.background : Background = background
        self.species : Species = species
        self.xp : int = xp
        self.classes : list[Class] = classes
        self.stats : Stats = Stats(base_scores)
        self.creatures : list[Creature] = creatures
        self.inventory : dict[Item, list[Item]] = inventory
        self.levels : dict[int, Level] = levels
        self.hp : HP = HP(now=0, max=0, temp=0)
        self.hd : list[HD] = [HD(now=0, max=0, die=0)]
        self.death_saves : DeathSaves = DeathSaves(successes=0, failures=0)
        self.armour_training : dict


class SmallCharacter(object):
    def __init__(self, name:str, species:Species):
        self.name = name
        self.species = species
