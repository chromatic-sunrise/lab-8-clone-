# TODO Create BlueberryBush class here
from event import Event
from player import Player

class BlueberryBush(Event):
    def __init__(self) -> None:
        super().__init__()

    def encounter(self, player: Player) -> bool:
        player.eat()
        print("You chow down on some tasty blueberries.")
        return True # The bush should be removed, so we return True.
