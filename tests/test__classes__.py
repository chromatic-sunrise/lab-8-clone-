# mypy: ignore-errors

# Acknowledgements
# author: Matt Kenison (<matthew.kenison@oregonstate.edu>), CS 162
# edited by: Alexander Guyer (<guyera@oregonstate.edu>), CS 162


from abc import ABC

import pytest

def test_event_class_exists_with_encounter_method_1_5_pts() -> None:
    """ (1.5 pts) for the `Event` class existing in event.py, being
    abstract, and having an abstract encounter method. """
    from event import Event

    assert issubclass(Event, ABC), 'Expected Event class to inherit from ABC, but it doesn\'t'
    assert hasattr(Event, 'encounter'), 'Expected Event class to have encounter method, but it doesn\'t'
    assert hasattr(Event.encounter, '__isabstractmethod__'), \
        "Event.encounter() must be decorated as an @abstractmethod, but it isn\'t"

def test_pond_class_is_implemented_1_pt() -> None:
    """ (1 pt) for the `Pond` class existing in pond.py,
    inheriting from the `Event` class, and implementing all
    inherited abstract methods. """
    from event import Event
    from pond import Pond
    from player import Player
    assert issubclass(Pond, Event), 'Expected Pond class to inherit from Event class, but it doesn\'t'
    try:
        pond = Pond()
        pond.encounter(Player())
    except Exception as e:
        pytest.fail(f"pond.encounter(player) did not execute successfully: {e}")


def test_blueberrybush_class_is_implemented_1_pt() -> None:
    """ (1 pt) for the `BlueberryBush` class existing in blueberrybush.py, inheriting from the `Event` class, and implementing all inherited abstract methods. """
    from event import Event
    from blueberrybush import BlueberryBush
    from player import Player
    assert issubclass(BlueberryBush, Event), 'Expected BlueberryBush class to inherit from Event class, but it doesn\'t'
    try:
        blueberry_bush = BlueberryBush()
        blueberry_bush.encounter(Player())
    except Exception as e:
        pytest.fail(f"blueberry_bush.encounter(player) did not execute "
                    f"successfully: {e}")


def test_deerherd_class_is_implemented_1_pt() -> None:
    """ (1 pt) for the `DeerHerd` class existing in deerherd.py, inheriting from the `Event` class, and implementing all inherited abstract methods. """
    from event import Event
    from deerherd import DeerHerd
    from player import Player
    assert issubclass(DeerHerd, Event), 'Expected DeerHerd class to inherit from Event class, but it doesn\'t'
    try:
        deer_herd = DeerHerd()
        deer_herd.encounter(Player())
    except Exception as e:
        pytest.fail(f"deer_herd.encounter(player) did not execute "
                    f"successfully: {e}")


def test_bearden_class_exists_1_pt() -> None:
    """ (1 pt) for the `BearDen` class existing in bearden.py, inheriting from the `Event` class, and implementing all inherited abstract methods. """
    from event import Event
    from bearden import BearDen
    from player import Player
    assert issubclass(BearDen, Event), 'Expected BearDen class to inherit from Event class, but it doesn\'t'
    try:
        bear_den = BearDen()
        bear_den.encounter(Player())
    except Exception as e:
        pytest.fail(f"bear_den.encounter(player) did not execute "
                    f"successfully: {e}")


def test_forestpatch_class_exists_with_event_attribute_1_5_pts() -> None:
    """ (1.5 pts) for the `ForestPatch` class existing in forestpatch.py with a private attribute of type `Event | None`. """
    from event import Event
    from forestpatch import ForestPatch

    assert '_event' in ForestPatch.__annotations__, 'Expected ForestPatch class to have _event attribute, but it doesn\'t'
    assert ForestPatch.__annotations__['_event'] == (Event | None), 'Expected ForestPatch class\'s _event attribute to have the type Event | None, but it doesn\'t'
