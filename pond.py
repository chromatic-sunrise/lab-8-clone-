# TODO Create Pond class here
from event import Event
from player import Player
from typing import override

class Pond(Event):
    # @override
    def encounter(self, player: Player) -> bool: 
        if player.is_thirsty():
            print("You drink from the pond.")
            player.drink()
        else:
            print("You're not thirsty.")
        return False # The pond should continue to exist, so return False.
