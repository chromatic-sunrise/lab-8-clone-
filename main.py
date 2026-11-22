# TODO: implement create_forest to instantiate and populate your forest
from forestpatch import ForestPatch
from player import Player
from coordinates import Coordinates
# Event imports:
from event import Event
from bearden import BearDen
from blueberrybush import BlueberryBush
from deerherd import DeerHerd
from pond import Pond
# random
import random

def event_list(bear_num: int, none_num: int) -> list[ForestPatch]:
    patches: list[ForestPatch] = []
    for _ in range(bear_num):
        patches.append(ForestPatch(BearDen))
    for _ in range(none_num):
        patches.append(ForestPatch(None))
    random.shuffle(patches)
    return patches

def create_forest() -> list[list[ForestPatch]]:
    forest: list[list[ForestPatch]] = []
    patches = event_list(3,19)
    for i in range(5):
        row_i: list[ForestPatch] = []
        for j in range(5):
            if (i,j) == (4,0):
                row_i.append(ForestPatch(DeerHerd))
            elif (i,j) == (0,0) or (i,j) == (4,4):
                row_i.append(ForestPatch(BlueberryBush))
            elif (i,j) == (0,4):
                row_i.append(ForestPatch(Pond))
            else:
                row_i.append(patches.pop(0))
        forest.append(row_i)
    return forest

def main() -> None:
    # TODO Remove `pass` below, and write your main function here.
    # Remember to obey the course's style and design guide. Don't put too
    # much code here.
    forest = create_forest()
    player = Player()

if __name__ == '__main__':
    main()
