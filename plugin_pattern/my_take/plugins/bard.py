"""Game extension that adds a bard character."""
from dataclasses import dataclass

from plugin_pattern.my_take.plugin_interface import PluginFactory


@dataclass
class Bard:
    name: str
    instrument: str = "flute"

    def make_a_noise(self) -> None:
        print(f"I am {self.name} and I play {self.instrument}. Toss a coin to your witcher")


def initialize(*, plugin_interface: PluginFactory) -> None:
    plugin_interface.register("bard", Bard)
