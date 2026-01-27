

class Plateau:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width
        self.rovers = []


    def is_rover_within_bounds(self, x: int, y: int)-> bool:
        return 0 <= x <= self.width and 0 <= y <= self.height
    
   