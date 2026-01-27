import pytest
from input_layer.parsers.plateau_parser import PlateauParser
from input_layer.parsers.position_parser import PositionParser
from input_layer.parsers.instruction_parser import InstructionParser
from logic_layer.plateau import Plateau
from logic_layer.mission_control import MissionControl

def test_full_example_from_brief():
    """Test the complete example from the Mars Rover brief"""
    # Input from the brief
    input_lines = [
        "5 5",           # Plateau size
        "1 2 N",         # Rover 1 position
        "LMLMLMLMM",     # Rover 1 instructions
        "3 3 E",         # Rover 2 position
        "MMRMMRMRRM"     # Rover 2 instructions
    ]
    
    # Parse plateau
    plateau_parser = PlateauParser()
    plateau_size = plateau_parser.parse_plateau(input_lines[0])
    plateau = Plateau(plateau_size.max_x, plateau_size.max_y)
    
    # Create mission control
    mission_control = MissionControl(plateau)
    
    # Parse and process rovers
    position_parser = PositionParser()
    instruction_parser = InstructionParser()
    
    # Process first rover
    rover1_pos = position_parser.parse_position(input_lines[1])
    rover1_instr = instruction_parser.parse_instructions(input_lines[2])
    final1 = mission_control.land_and_move_rover(rover1_pos, rover1_instr)
    
    # Process second rover
    rover2_pos = position_parser.parse_position(input_lines[3])
    rover2_instr = instruction_parser.parse_instructions(input_lines[4])
    final2 = mission_control.land_and_move_rover(rover2_pos, rover2_instr)
    
    # Verify results match expected output
    assert final1.x == 1 and final1.y == 3 and final1.direction.value == 'N'
    assert final2.x == 5 and final2.y == 1 and final2.direction.value == 'E'

def test_single_rover_movement():
    """Test a simple single rover scenario"""
    input_lines = [
        "5 5",
        "0 0 N",
        "MMRMM"
    ]
    
    plateau_parser = PlateauParser()
    plateau_size = plateau_parser.parse_plateau(input_lines[0])
    plateau = Plateau(plateau_size.max_x, plateau_size.max_y)
    
    mission_control = MissionControl(plateau)
    position_parser = PositionParser()
    instruction_parser = InstructionParser()
    
    position = position_parser.parse_position(input_lines[1])
    instructions = instruction_parser.parse_instructions(input_lines[2])
    final = mission_control.land_and_move_rover(position, instructions)
    
    
    assert final.x == 2 and final.y == 2 and final.direction.value == 'E'

def test_rover_hits_boundary():
    """Test that rover stops at plateau boundary"""
    input_lines = [
        "3 3",
        "0 0 N",
        "MMMMM"  
    ]
    
    plateau_parser = PlateauParser()
    plateau_size = plateau_parser.parse_plateau(input_lines[0])
    plateau = Plateau(plateau_size.max_x, plateau_size.max_y)
    
    mission_control = MissionControl(plateau)
    position_parser = PositionParser()
    instruction_parser = InstructionParser()
    
    position = position_parser.parse_position(input_lines[1])
    instructions = instruction_parser.parse_instructions(input_lines[2])
    final = mission_control.land_and_move_rover(position, instructions)
    
    # Should stop at y=3 (max boundary)
    assert final.x == 0 and final.y == 3 and final.direction.value == 'N'
    

def test_multiple_rovers_collision_prevention():
    """Test that rovers don't collide"""
    input_lines = [
        "5 5",
        "1 1 N",
        "M",      # Rover 1 moves to (1,2)
        "1 2 N",  # Rover 2 tries to land where Rover 1 moved to
        "M"
    ]
    
    plateau_parser = PlateauParser()
    plateau_size = plateau_parser.parse_plateau(input_lines[0])
    plateau = Plateau(plateau_size.max_x, plateau_size.max_y)
    
    mission_control = MissionControl(plateau)
    position_parser = PositionParser()
    instruction_parser = InstructionParser()
    
    # First rover should land and move successfully
    rover1_pos = position_parser.parse_position(input_lines[1])
    rover1_instr = instruction_parser.parse_instructions(input_lines[2])
    final1 = mission_control.land_and_move_rover(rover1_pos, rover1_instr)
    assert final1.x == 1 and final1.y == 2
    
    # Second rover should fail to land at occupied position
    rover2_pos = position_parser.parse_position(input_lines[3])
    rover2_instr = instruction_parser.parse_instructions(input_lines[4])
    
    with pytest.raises(ValueError, match="already occupied"):
        mission_control.land_and_move_rover(rover2_pos, rover2_instr)