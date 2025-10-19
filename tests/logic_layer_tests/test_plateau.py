from input_layer.input_types.plateau_size import PlateauSize
from input_layer.input_types.position import Position
from input_layer.input_types.compass_directions import CompassDirection
from logic_layer.plateau import Plateau

# Test 1 checks if the inputted position is within or out of bounds
def test_position_within_bounds():
    plateau = Plateau(5, 5)
    assert plateau.is_rover_within_bounds(0, 0) == True
    assert plateau.is_rover_within_bounds(5, 5) == True
    assert plateau.is_rover_within_bounds(6, 5) == False
    assert plateau.is_rover_within_bounds(5, 6) == False