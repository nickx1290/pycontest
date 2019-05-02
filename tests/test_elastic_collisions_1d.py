import pytest

from pycontest import elastic_collisions as ec
from pycontest.utils import momentum, E_kin


# a simple tests for equal masses (balls should exchange velocities)

# using default values of m1 and m2
def test_collision_1d_1_exchange_vel():
    v1_i = 1
    v2_i = -2
    assert ec.collision_1d(v1_i, v2_i) == ec.collision_1d(v2_i, v1_i)[::-1]


def test_collision_1d_conserve_momentum():
    m1 = 12
    v1 = 4
    m2 = 3.0
    v2 = -4.0

    ec.collision_1d()
