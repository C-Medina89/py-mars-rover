from input_layer.input_types.instructions import Instruction
from input_layer.input_types.position import Position
from input_layer.input_types.compass_directions import CompassDirection
from logic_layer.plateau import Plateau
from logic_layer.rover import Rover


def test_rovers_move_sequentially():
    # test rovers move one at a time not simultaneously
    plateau = Plateau(5,5)

    # Rover 1 starts at (1, 2) facing North
    rover1 = Rover(Position(1, 2, CompassDirection.NORTH))
    plateau.add_rover(rover1)
    
    # Rover 2 starts at (3, 3) facing East  
    rover2 = Rover(Position(3, 3, CompassDirection.EAST))
    plateau.add_rover(rover2)
    
    # Process rover1 instructions first
    rover1.process_instructions([Instruction.MOVE, Instruction.MOVE], plateau)
    assert rover1.position.x == 1
    assert rover1.position.y == 4
    
    # Then process rover2 instructions
    rover2.process_instructions([Instruction.MOVE, Instruction.MOVE], plateau)
    assert rover2.position.x == 5
    assert rover2.position.y == 3

def test_second_rover_cannot_move_into_first_rovers_old_position():
    #Test that a rover can't move where another rover was previously
    plateau = Plateau(5, 5)
    
    rover1 = Rover(Position(1, 2, CompassDirection.NORTH))
    plateau.add_rover(rover1)
    
    # Rover1 moves North, vacating (1, 2)
    rover1.process_instructions([Instruction.MOVE], plateau)
    assert rover1.position == Position(1, 3, CompassDirection.NORTH)
    
    # Rover2 tries to move to (1, 2) - should succeed since it's now vacant
    rover2 = Rover(Position(0, 2, CompassDirection.EAST))
    plateau.add_rover(rover2)
    rover2.process_instructions([Instruction.MOVE], plateau)
    assert rover2.position == Position(1, 2, CompassDirection.EAST)

def test_rovers_can_occupy_same_path_sequentially():
    """Test that rovers can follow the same path one after another"""
    plateau = Plateau(5, 5)
    
    rover1 = Rover(Position(0, 0, CompassDirection.EAST))
    plateau.add_rover(rover1)
    
    # Rover1 moves East to (1, 0), then (2,0)
    rover1.process_instructions([Instruction.MOVE, Instruction.MOVE], plateau)
    assert rover1.position == Position(2, 0, CompassDirection.EAST)
    
    # Now (0, 0) and (1,0) should be vacant
    # Rover2 can now start at (0, 0) then move to (1,0)
    rover2 = Rover(Position(0, 0, CompassDirection.EAST))
    plateau.add_rover(rover2) 
    rover2.process_instructions([Instruction.MOVE], plateau)
    
    assert rover2.position == Position(1, 0, CompassDirection.EAST)
