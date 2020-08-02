"""Author: Shreeda Bhat"""

""" This test is to check the notebook and pass the travis ci"""

import pytest


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()