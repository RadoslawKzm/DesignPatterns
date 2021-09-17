"""
Basic example showing how to create objects from fata using dynamic factory with
register/unregister methods.
"""

import json
from dataclasses import dataclass

from plugin_pattern.after import factory, loader


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
    # register a couple of character types
    factory.register("sorcerer", Sorcerer)
    factory.register("wizard", Wizard)
    factory.register("witcher", Witcher)

    # read data from JSON file
    with open("level.json", "r") as file:
        data = json.load(file)

        # load the plugins
        loader.load_plugins(data["plugins"])

        # create the characters
        characters = [factory.create(item) for item in data["characters"]]

        for character in characters:
            print(character, end="\t")
            character.make_a_noise()


if __name__ == '__main__':
    main()
