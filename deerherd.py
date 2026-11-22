# TODO Create DeerHerd class here
from event import Event
from player import Player

class DeerHerd(Event):
    def encounter(self, player: Player) -> bool:
        if (not player.is_thirsty()) and (not player.is_hungry()):
            player.win()
            print("You've finished browsing for the day and arrived safely back\
                  at the herd.")
        return False # The deer herd should not disappear, so return False.
