"""
Basic example showing how to create objects from fata using dynamic factory with
register/unregister methods.
"""

import json
from dataclasses import dataclass

from plugin_pattern.before.character import GameCharacter


@dataclass
class Sorcerer:
    name: str

    def make_a_noise(self) -> None:
        print(f"It's {self.name}. Sorcerer noises!!!")


@dataclass
class Wizard:
    name: str

    def make_a_noise(self) -> None:
        print(f"It's {self.name}. Wizard noises!!!")


@dataclass
class Witcher:
    name: str

    def make_a_noise(self) -> None:
        print(f"It's {self.name}. Witcher noises!!!")


def main() -> None:
    """Creates game characters"""
    with open("level.json", "r") as file:
        data = json.load(file)

        characters: list[GameCharacter] = []
        for item in data["characters"]:
            item_copy = item.copy()
            character_type = item_copy.pop("type")
            if character_type == "sorcerer":
                characters.append(Sorcerer(**item_copy))
            elif character_type == "wizard":
                characters.append(Wizard(**item_copy))
            elif character_type == "witcher":
                characters.append(Witcher(**item_copy))

        for character in characters:
            print(character, end="\t")
            character.make_a_noise()


if __name__ == '__main__':
    main()
