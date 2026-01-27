

class Plateau:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width
        self.rovers = []


    def is_rover_within_bounds(self, x: int, y: int)-> bool:
        return 0 <= x <= self.width and 0 <= y <= self.height
    
    def add_rover(self, rover):
    # add rover to the plateau with boundary validation

      if not self.is_rover_within_bounds(rover.position.x, rover.position.y):
        raise ValueError(f"Rover position ({rover.position.x}, {rover.position.y}) is out of bounds")
      self.rovers.append(rover)
    

    def get_rovers(self):
        return self.rovers