import pytest
from input_layer.parsers.plateau_parser import PlateauParser

# Test 1

def test_parse_plateau_position_gives_valid_plateau_size():
    parser = PlateauParser()
    plateau = parser.parse_plateau("5 5")
    assert plateau.max_x == 5
    assert plateau.max_y == 5

# Test 2

def test_parse_plateau_position_with_wrong_number_of_input_parts():
    parser = PlateauParser()
    with pytest.raises(ValueError):
        parser.parse_plateau("5")
    
    with pytest.raises(ValueError):
        parser.parse_plateau("5 7 5")

# Test 3

def test_parse_plateau_position_with_non_number_sizes():
    parser = PlateauParser()
    with pytest.raises(ValueError):
        parser.parse_plateau("five 5")
    
    with pytest.raises(ValueError):
        parser.parse_plateau("5 five")

# Test 4

def test_parse_plateau_position_with_negative_input_sizes():
    parser = PlateauParser()
    with pytest.raises(ValueError):
        parser.parse_plateau("-5 5")