import pytest
from input_layer.input_types.compass_directions import CompassDirection

#Test 1 check compass direction values are correct
def test_compass_direction_values():
    assert CompassDirection.NORTH.value == 'N'
    assert CompassDirection.EAST.value == 'E'
    assert CompassDirection.SOUTH.value == 'S'
    assert CompassDirection.WEST.value == 'W'

# Test 2 check error is raised when wrong direction is inputted 

def test_invalid_direction_raises_error():
    with pytest.raises(KeyError):
        CompassDirection['DOWN']  

# Test 3 test to check name access to direction 

def test_direction_access_by_name():
    assert CompassDirection['EAST'] == CompassDirection.EAST