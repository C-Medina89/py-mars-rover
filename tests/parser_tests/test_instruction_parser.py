from input_layer.parsers.instruction_parser import InstructionParser
from input_layer.input_types.instructions import Instruction


# Test 1 checks the parse instructions method with simple instructions
def test_parse_instructions_simple():
    parser = InstructionParser()
    result = parser.parse_instructions("LMR")
    assert result == [Instruction.LEFT, Instruction.MOVE, Instruction.RIGHT]

# Test 2 checks if invalid instructions are ignored

def test_ignores_invalid_instructions():
    parser = InstructionParser()
    result = parser.parse_instructions("LBMVR")
    assert result == [Instruction.LEFT, Instruction.MOVE, Instruction.RIGHT]

# Test 3 checks if lowercase characters are inputted and takes them as instructions

def test_lowercase_instructions():
    parser = InstructionParser()
    result = parser.parse_instructions("lmr")
    assert result == [Instruction.LEFT, Instruction.MOVE, Instruction.RIGHT]