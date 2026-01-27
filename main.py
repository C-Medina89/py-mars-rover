from input_layer.parsers.plateau_parser import PlateauParser
from input_layer.parsers.position_parser import PositionParser
from input_layer.parsers.instruction_parser import InstructionParser
from logic_layer.plateau import Plateau
from logic_layer.rover import Rover
from logic_layer.mission_control import MissionControl

def main():
    # Read input (for now, hardcoded as per the example)
    input_data = """5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM"""
    
    lines = input_data.strip().split('\n')
    
    # Parse plateau
    plateau_parser = PlateauParser()
    plateau_size = plateau_parser.parse_plateau(lines[0])
    plateau = Plateau(plateau_size.max_x, plateau_size.max_y)
    
    # Create mission control
    mission_control = MissionControl(plateau)
    
    # Parse and process each rover
    position_parser = PositionParser()
    instruction_parser = InstructionParser()
    
    rover_positions = []
    
    # Process rovers in pairs (position line + instruction line)
    for i in range(1, len(lines), 2):
        if i + 1 < len(lines):
            position_str = lines[i]
            instruction_str = lines[i + 1]
            
            position = position_parser.parse_position(position_str)
            instructions = instruction_parser.parse_instructions(instruction_str)
            
            final_pos = mission_control.land_and_move_rover(position, instructions)
            rover_positions.append(final_pos)
    
    # Output results
    for pos in rover_positions:
        print(f"{pos.x} {pos.y} {pos.direction.value}")

if __name__ == "__main__":
    main()