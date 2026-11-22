# mypy: ignore-errors

# Acknowledgements
# author: Matt Kenison (<matthew.kenison@oregonstate.edu>), CS 162
# edited by: Alexander Guyer (<guyera@oregonstate.edu>), CS 162


import conftest

def test_mypy_1_pt() -> None:
    """ (1 pt) mypy passes validation in --strict mode """
    cmd = conftest.Console("mypy --exclude 'test' --strict . ", timeout=30)
    assert "Success: no issues found" in cmd, "mypy validation failed"

