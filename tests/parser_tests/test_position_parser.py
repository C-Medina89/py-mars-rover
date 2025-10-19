import pytest
from input_layer.parsers.position_parser import PositionParser
from input_layer.input_types.compass_directions import CompassDirection

# Test1 
def test_position_parses_gives_valid_position():
    parser = PositionParser()
    position = parser.parse_position("1 2 N")
    assert position.x == 1
    assert position.y == 2
    assert position.direction == CompassDirection.NORTH

# Test 2

def test_parse_invalid_direction():
    parser = PositionParser()
    with pytest.raises(ValueError):
        parser.parse_position("1 2 X")

# Test 3

def test_parse_wrong_format():
    parser = PositionParser()
    with pytest.raises(ValueError):
        parser.parse_position("1 2") 
    
    with pytest.raises(ValueError):
        parser.parse_position("1 2 N E")  