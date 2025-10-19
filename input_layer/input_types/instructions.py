from enum import Enum

class Instruction(Enum):
    # Valid movement instructions for the mars rover
    LEFT = 'L'
    RIGHT = 'R'
    MOVE = 'M'