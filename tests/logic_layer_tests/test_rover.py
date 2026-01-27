from input_layer.input_types.instructions import Instruction
from input_layer.input_types.position import Position
from input_layer.input_types.compass_directions import CompassDirection
from logic_layer.rover import Rover
from logic_layer.plateau import Plateau



def test_turn_right_full_rotation():
    rover = Rover(Position(0, 0, CompassDirection.NORTH))
    rover.turn_right()  # N → E
    assert rover.position.direction == CompassDirection.EAST
    rover.turn_right()  # E → S
    assert rover.position.direction == CompassDirection.SOUTH
    rover.turn_right()  # S → W
    assert rover.position.direction == CompassDirection.WEST
    rover.turn_right()  # W → N
    assert rover.position.direction == CompassDirection.NORTH



def test_turn_left_full_rotation():
    rover = Rover(Position(0, 0, CompassDirection.NORTH))
    rover.turn_left()  # N → W
    assert rover.position.direction == CompassDirection.WEST
    rover.turn_left()  # W → S
    assert rover.position.direction == CompassDirection.SOUTH
    rover.turn_left()  # S → E
    assert rover.position.direction == CompassDirection.EAST
    rover.turn_left()  # E → N
    assert rover.position.direction == CompassDirection.NORTH



def test_move_in_all_directions():
    # Test North
    rover = Rover(Position(2, 2, CompassDirection.NORTH))
    rover.next_move()
    assert rover.position.x == 2 and rover.position.y == 3
    
    # Test South
    rover = Rover(Position(2, 2, CompassDirection.SOUTH))
    rover.next_move()
    assert rover.position.x == 2 and rover.position.y == 1
    
    # Test East
    rover = Rover(Position(2, 2, CompassDirection.EAST))
    rover.next_move()
    assert rover.position.x == 3 and rover.position.y == 2
    
    # Test West
    rover = Rover(Position(2, 2, CompassDirection.WEST))
    rover.next_move()
    assert rover.position.x == 1 and rover.position.y == 2

def test_rover_processes_instructions():
    plateau = Plateau(5, 5)
    rover = Rover(Position(1, 2, CompassDirection.NORTH))
    instructions = [Instruction.LEFT, Instruction.MOVE, Instruction.LEFT, 
                    Instruction.MOVE, Instruction.LEFT, Instruction.MOVE, 
                    Instruction.LEFT, Instruction.MOVE, Instruction.MOVE]
    
    rover.process_instructions(instructions, plateau)
    
    assert rover.position.x == 1
    assert rover.position.y == 3
    assert rover.position.direction == CompassDirection.NORTH