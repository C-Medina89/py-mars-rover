from input_layer.input_types.instructions import Instruction
from input_layer.input_types.position import Position
from input_layer.input_types.compass_directions import CompassDirection
from logic_layer.rover import Rover

# Test 1 checks if the inputted position is within or out of bounds

def test_rover_turn_right():
    rover = Rover(Position(2, 3, CompassDirection.NORTH))
    rover.turn_right()
    assert rover.position.direction == CompassDirection.EAST



def test_rover_turn_left():
    rover = Rover(Position(2, 3, CompassDirection.EAST))
    rover.turn_left()
    assert rover.position.direction == CompassDirection.NORTH



def test_rover_next_move():
    rover = Rover(Position(1, 2, CompassDirection.SOUTH))
    rover.next_move()
    assert rover.position.x == 1
    assert rover.position.y == 1
    assert rover.position.direction == CompassDirection.SOUTH