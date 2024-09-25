import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from my_lib.my_functions import *


def test_add():
    assert add(2, 5) == 7