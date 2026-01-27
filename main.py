from input_layer.parsers.plateau_parser import PlateauParser
from input_layer.parsers.position_parser import PositionParser
from input_layer.parsers.instruction_parser import InstructionParser
from logic_layer.plateau import Plateau
from logic_layer.rover import Rover
from logic_layer.mission_control import MissionControl

def main():
    # Example input from the Mars Rover brief
    plateau_input = "5 5"

    # rover 1 data
    rover1_position_input = "1 2 N"
    rover1_instruction_input = "LMLMLMLMM"

    # rover 2 data
    rover2_position_input = "3 3 E"
    rover2_instruction_input = "MMRMMRMRRM"

    # Create parser instances
    plateau_parser = PlateauParser()
    position_parser = PositionParser()
    instruction_parser = InstructionParser()

    # Parse each input
    plateau_size = plateau_parser.parse_plateau(plateau_input)
    # position = position_parser.parse_position(rover_position_input)
    # instructions = instruction_parser.parse_instructions(rover_instruction_input)

    # Create plateau and rover instances
    plateau = Plateau(plateau_size.max_x, plateau_size.max_y)
    # rover = Rover(position)

    # Create mission control
    mission_control = MissionControl(plateau)



    # process rover 1 
    rover1_position = position_parser.parse_position(rover1_position_input)
    rover1_instructions = instruction_parser.parse_instructions(rover1_instruction_input)
    final_pos1 = mission_control.land_and_move_rover(rover1_position, rover1_instructions)

    # Process rover 2
    rover2_position = position_parser.parse_position(rover2_position_input)
    rover2_instructions = instruction_parser.parse_instructions(rover2_instruction_input)
    final_pos2 = mission_control.land_and_move_rover(rover2_position, rover2_instructions)
    

    # # Process instructions
    # rover.process_instructions(instructions, plateau)
    
    # # Print final position
    # print(f"{rover.position.x} {rover.position.y} {rover.position.direction.value}")

    # Output results
    print(f"{final_pos1.x} {final_pos1.y} {final_pos1.direction.value}")
    print(f"{final_pos2.x} {final_pos2.y} {final_pos2.direction.value}")


if __name__ == "__main__":
    main()