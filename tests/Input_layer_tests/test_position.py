from input_layer.input_types.position import Position
from input_layer.input_types.compass_directions import CompassDirection
import pytest


# Test 1 check if position stores values given
def test_position_stores_values():
    pos = Position(2, 4, CompassDirection.SOUTH)
    assert pos.x == 2
    assert pos.y == 4
    assert pos.direction == CompassDirection.SOUTH

# Test 2 checks negative integers raise error
def test_position_negative_coordinates():
    with pytest.raises(ValueError):
        Position(-1, 2, CompassDirection.WEST)
    
    with pytest.raises(ValueError):
        Position(1, -2, CompassDirection.EAST)

# Test 3 checks input compass direction and raises error if invalid 

def test_input_position_for_invalid_direction():
    with pytest.raises(ValueError):
        Position(3, 1, "UP")