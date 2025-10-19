
from input_layer.parsers.plateau_parser import PlateauParser
from input_layer.parsers.position_parser import PositionParser
from input_layer.parsers.instruction_parser import InstructionParser

def main():
    # Example input from the Mars Rover brief
    plateau_input = "5 5"
    rover_position_input = "1 2 N"
    rover_instruction_input = "LMLMLMLMM"

    # Create parser instances
    plateau_parser = PlateauParser()
    position_parser = PositionParser()
    instruction_parser = InstructionParser()

    # Parse each input
    plateau = plateau_parser.parse_plateau(plateau_input)
    position = position_parser.parse_position(rover_position_input)
    instructions = instruction_parser.parse_instructions(rover_instruction_input)

    # Print parsed data to confirm it’s working
    print("Parsed Plateau:", plateau)
    print("Parsed Rover Position:", position)
    print("Parsed Instructions:", instructions)


main()