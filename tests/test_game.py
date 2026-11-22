# mypy: ignore-errors

# Acknowledgements
# author: Matt Kenison (<matthew.kenison@oregonstate.edu>), CS 162
# edited by: Alexander Guyer (<guyera@oregonstate.edu>), CS 162


def test_forest_patches_are_populated_with_proper_events_1_pt() -> None:
    """ (1 pt) for the forest patches in the forest being populated with the proper events in the proper places as described """
    from bearden import BearDen
    from blueberrybush import BlueberryBush
    from deerherd import DeerHerd
    from event import Event
    from forestpatch import ForestPatch
    from pond import Pond
    import main

    forest = main.create_forest()

    assert isinstance(forest[0][0]._event, BlueberryBush), 'After executing forest = create_forest(), expected forest[0][0]._event (top left event) to be a BlueberryBush instance, but it isn\'t'
    assert isinstance(forest[4][4]._event, BlueberryBush), 'After executing forest = create_forest(), expected forest[4][4]._event (bottom right event) to be a BlueberryBush instance, but it isn\'t'
    assert isinstance(forest[0][4]._event, Pond), 'After executing forest = create_forest(), expected forest[0][4]._event (top right event) to be a Pond instance, but it isn\'t'
    assert isinstance(forest[4][0]._event, DeerHerd), 'After executing forest = create_forest(), expected forest[4][0]._event (bottom left event) to be a DeerHerd instance, but it isn\'t'

    bear_den_count = 0
    for row in forest:
        for patch in row:
            if isinstance(patch._event, BearDen):
                bear_den_count += 1
    assert bear_den_count == 3, 'After executing forest = create_forest(), expected exactly three of the forest patches in the forest to have bear dens'
