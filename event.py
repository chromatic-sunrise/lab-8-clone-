# TODO Create abstract Event class here. Remember to inherit from ABC and
# decorate abstract methods with @abstractmethod
from abc import ABC, abstractmethod
from player import Player
from coordinates import Coordinates

class Event(ABC):    
    def __init__(self) -> None:
        pass

    # If our method returns True, it will be removed from the game (set its
    # type to None). Otherwise, False will indicate that it should remain as is.
    @abstractmethod
    def encounter(self, player: Player) -> bool:
        pass
