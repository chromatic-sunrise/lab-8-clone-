# TODO Create BearDen class here
from event import Event
from player import Player

class BearDen(Event):
    _encounter_num: int
    def __init__(self) -> None:
        super().__init__()
        self._encounter_num = 0

    def encounter(self, player: Player) -> bool:
        if self._encounter_num < 1:
            print("Whew, that was close! You almost woke a nearby bear.")
            player.move_back()
            self._encounter_num += 1
        else:
            print("You woke a nearby bear. It's hungry. Game over.")
            player.lose()
        return False # The bear should not be removed from the game.
