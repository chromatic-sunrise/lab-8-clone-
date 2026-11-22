# TODO Create Pond class here
from event import Event
from player import Player

class Pond(Event):
    def __init__(self) -> None:
        super().__init__()

    def encounter(self, player: Player) -> bool: 
        if player.is_thirsty():
            print("You drink from the pond.")
            player.drink()
        else:
            print("You're not thirsty.")
        return False # The pond should continue to exist, so return False.
