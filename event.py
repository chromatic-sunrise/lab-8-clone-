# TODO Create abstract Event class here. Remember to inherit from ABC and
# decorate abstract methods with @abstractmethod
from abc import ABC, abstractmethod
from player import Player

class Event(ABC):    
    # If our method returns True, it will be removed from the game (set its
    # type to None). Otherwise, False will indicate that it should remain as is.
    @abstractmethod
    def encounter(self, player: Player) -> bool:
        pass
