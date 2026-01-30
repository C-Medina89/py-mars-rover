# from input_layer.parsers.plateau_parser import PlateauParser
# from input_layer.parsers.position_parser import PositionParser
# from input_layer.parsers.instruction_parser import InstructionParser
# from logic_layer.plateau import Plateau
# from logic_layer.rover import Rover
# from logic_layer.mission_control import MissionControl

# # def main():
# #     # Read input (for now, hardcoded as per the example)
# #     input_data = """5 5
# # 1 2 N
# # LMLMLMLMM
# # 3 3 E
# # MMRMMRMRRM"""
    
# #     lines = input_data.strip().split('\n')
    
# #     # Parse plateau
# #     plateau_parser = PlateauParser()
# #     plateau_size = plateau_parser.parse_plateau(lines[0])
# #     plateau = Plateau(plateau_size.max_x, plateau_size.max_y)
    
# #     # Create mission control
# #     mission_control = MissionControl(plateau)
    
# #     # Parse and process each rover
# #     position_parser = PositionParser()
# #     instruction_parser = InstructionParser()
    
# #     rover_positions = []
    
# #     # Process rovers in pairs (position line + instruction line)
# #     for i in range(1, len(lines), 2):
# #         if i + 1 < len(lines):
# #             position_str = lines[i]
# #             instruction_str = lines[i + 1]
            
# #             position = position_parser.parse_position(position_str)
# #             instructions = instruction_parser.parse_instructions(instruction_str)
            
# #             final_pos = mission_control.land_and_move_rover(position, instructions)
# #             rover_positions.append(final_pos)
    
# #     # Output results
# #     for pos in rover_positions:
# #         print(f"{pos.x} {pos.y} {pos.direction.value}")

# # if __name__ == "__main__":
# #     main()

# def simple_interactive_mode():
#     """Simple interactive UI"""
#     print("=== Mars Rover Control ===")
#     print()
    
#     # Get plateau size
#     plateau_input = input("Enter plateau size (e.g., '5 5'): ")
#     plateau_parser = PlateauParser()
#     plateau_size = plateau_parser.parse_plateau(plateau_input)
#     plateau = Plateau(plateau_size.max_x, plateau_size.max_y)
    
#     mission_control = MissionControl(plateau)
#     position_parser = PositionParser()
#     instruction_parser = InstructionParser()
    
#     results = []
    
#     # Get rover data
#     rover_count = 1
#     while True:
#         print(f"\n--- Rover {rover_count} ---")
#         position_input = input(f"Enter rover {rover_count} position (e.g., '1 2 N') or 'done' to finish: ")
        
#         if position_input.lower() == 'done':
#             break
        
#         instruction_input = input(f"Enter rover {rover_count} instructions (e.g., 'LMLMLMLMM'): ")
        
#         try:
#             position = position_parser.parse_position(position_input)
#             instructions = instruction_parser.parse_instructions(instruction_input)
            
#             final_pos = mission_control.land_and_move_rover(position, instructions)
#             results.append(f"{final_pos.x} {final_pos.y} {final_pos.direction.value}")
            
#             print(f"Rover {rover_count} landed and moved successfully!")
#             rover_count += 1
            
#         except Exception as e:
#             print(f"Error: {e}")
#             print("Please try again.")
    
#     # Show results
#     print("\n=== Final Positions ===")
#     for result in results:
#         print(result)

# if __name__ == "__main__":
#     simple_interactive_mode()
import sys
from ui_layer.terminal_ui import main as terminal_main

def main():
    """Simple entry point that launches the terminal UI"""
    print("Starting Mars Rover Terminal Interface...")
    terminal_main()

if __name__ == "__main__":
    main()