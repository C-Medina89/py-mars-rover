from input_layer.input_types.instructions import Instruction
import pytest

# test 1 checks instruction values 

def test_instruction_values_are_correct():
    assert Instruction.RIGHT.value == 'R'
    assert Instruction.LEFT.value == 'L'
    assert Instruction.MOVE.value == 'M'


# test 2 raise error when wrong instructions inputed

def test_invalid_instruction_raises_error():
    with pytest.raises(KeyError):
        Instruction['N']  

# test 3 name access to instructions

def test_name_access_to_instructions():
    assert Instruction['RIGHT'] == Instruction.RIGHT

# Test 4 lowercase input test

# def test_access_with_lowercase_input():
#     assert Instruction['l'] == Instruction.LEFT
