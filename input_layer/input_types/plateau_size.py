from dataclasses import dataclass

@dataclass
class PlateauSize:
    max_x: int
    max_y: int

    def __post_init__(self):
         if self.max_x <= 0 or self.max_y <= 0:
            raise ValueError("Plateau dimensions must not be negative")


