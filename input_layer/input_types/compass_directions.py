from enum import Enum

class CompassDirection(Enum):
    # Valid compass directions for the mars rover
    NORTH = 'N' or 'n'
    SOUTH = 'S' or 's'
    EAST = 'E' or 'e'
    WEST = 'W' or 'w'