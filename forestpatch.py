# TODO Create ForestPatch class here
from event import Event
from player import Player

class ForestPatch:
    _event: Event | None

    def __init__(self, event: Event | None) -> None:
        self._event = event

    def encounter(self, player: Player) -> None:
        # Can probably replace with "if self._event is Event:" maybe?
        if type(self._event) == Event:
            # If Event.encounter returns True, that signals to this function
            # call here that it should be removed from the game after its
            # encounter.
            if self._event.encounter(player):
                self._event = None
