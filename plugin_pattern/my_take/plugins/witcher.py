"""Game extension that adds a bard character."""
from dataclasses import dataclass

from plugin_pattern.my_take.plugin_interface import PluginFactory


@dataclass
class Witcher:
    name: str

    def make_a_noise(self) -> None:
        print(f"I am {self.name}. Autistic witcher screeching")


def initialize(*, plugin_interface: PluginFactory) -> None:
    plugin_interface.register("witcher", Witcher)
