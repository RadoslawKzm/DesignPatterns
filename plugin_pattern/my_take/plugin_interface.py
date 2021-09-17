"""A simple plugin loader"""
from __future__ import annotations
import importlib
from typing import Callable, Any, Type

from plugin_pattern.my_take.character import GameCharacter


class PluginFactory:
    """A plugin has a single function called initialize"""

    characters: dict[str, Callable[..., GameCharacter]] = {}

    @staticmethod
    def initialize(*, plugin_interface: Type[PluginFactory]) -> None:
        """Initialize the plugin"""

    @staticmethod
    def import_module(name: str) -> PluginFactory:
        return importlib.import_module(name)  # type: ignore

    @classmethod
    def load_plugins(cls, plugins: list[str]) -> None:
        """Load the plugins defined in the plugins list."""
        for plugin_name in plugins:
            plugin = cls.import_module(plugin_name)
            plugin.initialize(plugin_interface=cls)

    @classmethod
    def register(cls, character_type: str, character_class: Callable[..., GameCharacter]) -> None:
        cls.characters[character_type] = character_class

    @classmethod
    def unregister(cls, character_type: str) -> None:
        """Unregister a game character type"""
        cls.characters.pop(character_type, None)

    @classmethod
    def create(cls, arguments: dict[str, Any]) -> GameCharacter:
        """Create a game character of a specific type, given a dictionary of arguments"""
        character_type = arguments.pop("type")
        if character_class := cls.characters.get(character_type, None):
            return character_class(**arguments)
        raise ValueError(f"Unknown character type {character_type}") from None
