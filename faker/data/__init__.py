from enum import Enum

NAMES = [
    "Liam",
    "Emma",
    "Noah",
    "Olivia",
    "Ava",
    "Elijah",
    "Sophia",
    "Mason",
    "Isabella",
    "Logan",
    "Mia",
    "James",
    "Charlotte",
    "Benjamin",
    "Amelia",
    "Lucas",
    "Harper",
    "Henry",
    "Evelyn",
    "Alexander"
]


class Sex(str, Enum):
    M = "male"
    F = "Female"

    @classmethod
    def __iter__(cls):
        return iter(cls.__members__.values())


class Race(str, Enum):
    Human = "Human"
    Elf = "Elf"
    Dwarf = "Dwarf"
    Orc = "Orc"
    Gnome = "Gnome"
    Halfling = "Halfling"
    Dragonborn = "Dragonborn"
    Tiefling = "Tiefling"
    HalfElf = "Half-Elf"
    HalfOrc = "Half-Orc"
    Goblin = "Goblin"
    Troll = "Troll"
    Giant = "Giant"
    Vampire = "Vampire"
    Werewolf = "Werewolf"
    Mermaid_Merman = "Mermaid/Merman"
    Fairy = "Fairy"
    Centaur = "Centaur"
    Minotaur = "Minotaur"
    Satyr = "Satyr"

    @classmethod
    def __iter__(cls):
        return iter(cls.__members__.values())
