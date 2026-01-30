from enum import Enum

class Instruction(Enum):
    # Valid movement instructions for the mars rover
    LEFT = 'L' or 'l'
    RIGHT = 'R' or 'r'
    MOVE = 'M' or 'm'