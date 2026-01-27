

class Plateau:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width
        self.rovers = []


    def is_rover_within_bounds(self, x: int, y: int)-> bool:
        return 0 <= x <= self.width and 0 <= y <= self.height
    
    def is_position_occupied(self, x: int, y= int, excluding_rover=None)-> bool:
        # check if any rover at given position
        for rover in self.rovers:
            if rover is excluding_rover:
                continue
            if rover.position.x == x and rover.position.y == y:
                return True
        return False
    
    def add_rover(self, rover):
        # Check bounds
        if not self.is_rover_within_bounds(rover.position.x, rover.position.y):
            raise ValueError(f"Rover position ({rover.position.x}, {rover.position.y}) is out of bounds")
        
        if self.is_position_occupied(rover.position.x, rover.position.y, excluding_rover=None):
            raise ValueError(f"Position ({rover.position.x}, {rover.position.y}) is already occupied")

        self.rovers.append(rover)

    def get_rovers(self):
        # get all rovers on the plateau
        return self.rovers