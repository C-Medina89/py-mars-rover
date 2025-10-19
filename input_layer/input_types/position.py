from dataclasses import dataclass
from input_layer.input_types.compass_directions import CompassDirection

@dataclass
class Position:
    x: int
    y: int
    direction: CompassDirection

    def __post_init__(self):
        if self.x < 0 or self.y < 0:
            raise ValueError("Coordinates cannot be negative")
        if not isinstance(self.direction, CompassDirection):
            raise ValueError("Direction must be a CompassDirection")
        
    