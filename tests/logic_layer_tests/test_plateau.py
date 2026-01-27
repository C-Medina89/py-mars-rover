from input_layer.input_types.plateau_size import PlateauSize
from input_layer.input_types.position import Position
from input_layer.input_types.compass_directions import CompassDirection
from logic_layer.plateau import Plateau
from logic_layer.rover import Rover
import pytest

# Test 1 checks if the inputted position is within or out of bounds
def test_position_within_bounds():
    plateau = Plateau(5, 5)
    assert plateau.is_rover_within_bounds(0, 0) == True
    assert plateau.is_rover_within_bounds(5, 5) == True
    assert plateau.is_rover_within_bounds(6, 5) == False
    assert plateau.is_rover_within_bounds(5, 6) == False

def test_add_rover_to_plateau():
    plateau = Plateau(5, 5)
    rover = Rover(Position(1, 2, CompassDirection.NORTH))
    plateau.add_rover(rover)
    assert rover in plateau.get_rovers()

def test_is_position_occupied():
    plateau = Plateau(5, 5)
    rover1 = Rover(Position(1, 2, CompassDirection.NORTH))
    rover2 = Rover(Position(1, 2, CompassDirection.EAST))  # Same position
    plateau.add_rover(rover1)
    assert plateau.is_position_occupied(1, 2) == True
    assert plateau.is_position_occupied(3, 3) == False

def test_cannot_add_rover_out_of_bounds():
    plateau = Plateau(5, 5)
    rover = Rover(Position(10, 10, CompassDirection.NORTH))  # Out of bounds
    with pytest.raises(ValueError):
        plateau.add_rover(rover)

def test_cannot_add_rover_on_occupied_position():
    plateau = Plateau(5, 5)
    rover1 = Rover(Position(1, 2, CompassDirection.NORTH))
    rover2 = Rover(Position(1, 2, CompassDirection.EAST))  # Same position
    plateau.add_rover(rover1)
    with pytest.raises(ValueError):
        plateau.add_rover(rover2)