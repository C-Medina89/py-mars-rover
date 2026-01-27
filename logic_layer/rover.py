from input_layer.input_types.compass_directions import CompassDirection
from input_layer.input_types.instructions import Instruction
from input_layer.input_types.position import Position
from logic_layer.plateau import Plateau


class Rover:
    def __init__(self, position:Position):
        self.position = position


    def turn_right(self):
        # this function changes the rover position by 90 degrees to the right
        direction_mapping = {
            CompassDirection.NORTH: CompassDirection.EAST,
            CompassDirection.EAST: CompassDirection.SOUTH,
            CompassDirection.SOUTH: CompassDirection.WEST,
            CompassDirection.WEST: CompassDirection.NORTH
            
        }
        self.position.direction = direction_mapping[self.position.direction]


        
    def turn_left(self):
        # this function changes the rover position by 90 degrees to the left
        direction_mapping = {
            CompassDirection.NORTH: CompassDirection.WEST,
            CompassDirection.EAST: CompassDirection.NORTH,
            CompassDirection.SOUTH: CompassDirection.EAST,
            CompassDirection.WEST: CompassDirection.SOUTH
            
        }
        self.position.direction = direction_mapping[self.position.direction]



    def next_move(self):
        print(f"Before move: ({self.position.x}, {self.position.y}) facing {self.position.direction}")
        # this function moves the rover one step forward in their current direction
        x = self.position.x
        y = self.position.y

        if self.position.direction == CompassDirection.NORTH:
            y += 1
        elif self.position.direction == CompassDirection.SOUTH:
            y -= 1
        elif self.position.direction == CompassDirection.EAST:
            x += 1
        elif self.position.direction == CompassDirection.WEST:
            x -= 1
        self.position.x = x
        self.position.y = y
        print(f"After move: ({self.position.x}, {self.position.y})")

    def process_instructions(self, instructions, plateau):
        # process a list of instructionns for the rover

        for instruction in instructions:
            if instruction == Instruction.LEFT:
                self.turn_left()
            elif instruction == Instruction.RIGHT:
                self.turn_right()
            elif instruction == Instruction.MOVE:
                print(f"Processing MOVE instruction")
                # store current position
                current_x, current_y =self.position.x, self.position.y

                # calculate new position
                self.next_move()

                # check if new position is within plateau bounds
                if not plateau.is_rover_within_bounds(self.position.x, self.position.y):
                    # revert to previous position if out of bounds
                    self.position.x, self.position.y = current_x, current_y
                    continue
                    # # Raise error
                    # raise ValueError(f"Rover would move out of bounds to ({self.position.x}, {self.position.y})")

                # Check collision with other rovers
                if plateau.is_position_occupied(self.position.x, self.position.y, excluding_rover= self):
                    self.position.x, self.position.y = current_x, current_y
                    continue  
            
            

