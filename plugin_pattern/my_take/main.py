"""
Basic example showing how to create objects from fata using dynamic factory with
register/unregister methods.
"""

import json

from plugin_pattern.my_take.character import GameCharacter
from plugin_pattern.my_take.plugin_interface import PluginFactory


def main() -> None:
    """Creates game characters"""
    plugin_interface = PluginFactory()
    # read data from JSON file
    with open("plugins.json", "r") as file:
        data = json.load(file)

        # load the plugins
        plugin_interface.load_plugins(data["plugins"])

        # create the characters
        characters: list[GameCharacter] = [plugin_interface.create(item) for item in data["characters"]]

        for character in characters:
            print(character, end="\t")
            character.make_a_noise()


if __name__ == "__main__":
    main()
