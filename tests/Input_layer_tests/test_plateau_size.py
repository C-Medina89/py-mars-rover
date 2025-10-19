from input_layer.input_types.plateau_size import PlateauSize
import pytest

# Test 1 checks correct plateau size created
def test_plateau_size_creation():
    plateau = PlateauSize(5, 5)
    assert plateau.max_x == 5
    assert plateau.max_y == 5

# Test 2 checks and raises error if invalied input is given

def test_if_invalid_input_is_given_as_plateau_size():
    with pytest.raises(ValueError):
        PlateauSize(5,0)
        
    with pytest.raises(ValueError):
        PlateauSize(5, 0)
    
    with pytest.raises(ValueError):
        PlateauSize(-1, 5)
