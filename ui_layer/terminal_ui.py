import sys
from input_layer.parsers.plateau_parser import PlateauParser
from input_layer.parsers.position_parser import PositionParser
from input_layer.parsers.instruction_parser import InstructionParser
from logic_layer.plateau import Plateau
from logic_layer.mission_control import MissionControl
from logic_layer.rover import Rover

class VisualDisplay:
    """Simple visual display for Mars Plateau"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def display_grid(self, rovers, title="Mars Plateau"):
        """Display a simple grid showing rover positions"""
        print(f"\n{'=' * 40}")
        print(f"🛰️  {title}")
        print(f"{'=' * 40}")
        
        # Create empty grid
        grid = []
        for y in range(self.height + 1):
            row = []
            for x in range(self.width + 1):
                row.append('.')
            grid.append(row)
        
        # Place rovers on grid
        rover_symbols = {'N': '↑', 'S': '↓', 'E': '→', 'W': '←'}
        for rover in rovers:
            x = rover.position.x
            y = rover.position.y
            if 0 <= x <= self.width and 0 <= y <= self.height:
                grid[y][x] = rover_symbols.get(rover.position.direction.value, 'R')
        
        # Display grid (y=0 at bottom)
        print("Y")
        for y in range(self.height, -1, -1):  # Reverse for correct orientation
            print(f"{y:2} ", end="")
            for x in range(self.width + 1):
                print(f"[{grid[y][x]}]", end="")
            print()
        
        # X-axis labels
        print("   ", end="")
        for x in range(self.width + 1):
            print(f" {x:2} ", end="")
        print(" X")
        
        print("\nLegend: ↑=N ↓=S →=E ←=W .=Empty")
        print("=" * 40)

class TerminalUI:
    def __init__(self):
        self.plateau = None
        self.mission_control = None
        self.visual_display = None
        self.visual_mode = False
    
    def run(self):
        """Main interactive terminal interface"""
        print("=" * 50)
        print("🚀 MARS ROVER MISSION CONTROL")
        print("=" * 50)
        
        # Ask about visual mode
        self.visual_mode = self.ask_visual_mode()
        
        # Step 1: Setup Plateau
        self.setup_plateau()
        
        # Step 2: Process Rovers
        self.process_rovers()
        
        # Step 3: Show Results
        self.show_results()
    
    def ask_visual_mode(self):
        """Ask if user wants visual display"""
        print("\n👁️  VISUAL DISPLAY OPTION")
        print("-" * 25)
        return self.ask_yes_no("Enable visual display of rovers?")
    
    def setup_plateau(self):
        """Get plateau size from user"""
        print("\n📐 STEP 1: SETUP PLATEAU")
        print("-" * 30)
        
        while True:
            try:
                plateau_input = input("Enter plateau size (format: 'width height' e.g., '5 5'): ").strip()
                
                if not plateau_input:
                    print("Using default: 5 5")
                    plateau_input = "5 5"
                
                plateau_parser = PlateauParser()
                plateau_size = plateau_parser.parse_plateau(plateau_input)
                self.plateau = Plateau(plateau_size.max_x, plateau_size.max_y)
                self.mission_control = MissionControl(self.plateau)
                
                # Create visual display if enabled
                if self.visual_mode:
                    self.visual_display = VisualDisplay(plateau_size.max_x, plateau_size.max_y)
                    print("\n👁️  Visual display enabled!")
                    # Show empty plateau
                    self.visual_display.display_grid([], "Initial Empty Plateau")
                
                print(f"✓ Plateau created: {plateau_size.max_x}x{plateau_size.max_y} grid")
                break
                
            except ValueError as e:
                print(f"❌ Error: {e}")
                print("Please try again.")
            except Exception as e:
                print(f"❌ Unexpected error: {e}")
    
    def process_rovers(self):
        """Process multiple rovers interactively"""
        print("\n🤖 STEP 2: DEPLOY ROVERS")
        print("-" * 30)
        
        rover_count = 1
        
        while True:
            print(f"\nRover #{rover_count}")
            
            # Get rover position
            position = self.get_rover_position(rover_count)
            if position is None:  # User wants to stop
                break
            
            # Show visual if enabled (before movement)
            if self.visual_mode and position:
                # Create temp rover for display
                temp_rover = Rover(position)
                self.visual_display.display_grid([temp_rover], f"Rover #{rover_count} Landing Position")
            
            # Get rover instructions
            instructions = self.get_rover_instructions(rover_count)
            if instructions is None:  # User wants to stop
                break
            
            try:
                # Deploy and move rover
                final_pos = self.mission_control.land_and_move_rover(position, instructions)
                print(f"✓ Rover #{rover_count} deployed and moved!")
                print(f"  Final position: {final_pos.x} {final_pos.y} {final_pos.direction.value}")
                
                # Show updated visual if enabled
                if self.visual_mode:
                    self.visual_display.display_grid(
                        self.mission_control.rovers, 
                        f"After Rover #{rover_count} Movement"
                    )
                
                rover_count += 1
                
                # Ask if user wants to add another rover
                if not self.ask_yes_no("Add another rover?"):
                    break
                    
            except ValueError as e:
                print(f"❌ Error: {e}")
                if self.ask_yes_no("Try again with different position?"):
                    continue
                else:
                    break
    
    def get_rover_position(self, rover_number):
        """Get valid rover position from user"""
        while True:
            try:
                position_input = input(f"Enter Rover #{rover_number} starting position (format: 'x y direction' e.g., '1 2 N'): ").strip()
                
                if not position_input:
                    if rover_number == 1:
                        print("Using example position: 1 2 N")
                        position_input = "1 2 N"
                    else:
                        print("❌ Position cannot be empty")
                        continue
                
                position_parser = PositionParser()
                position = position_parser.parse_position(position_input)
                
                # Validate position is within plateau bounds
                if not self.plateau.is_rover_within_bounds(position.x, position.y):
                    print(f"❌ Position ({position.x}, {position.y}) is outside plateau!")
                    continue
                
                return position
                
            except ValueError as e:
                print(f"❌ Error: {e}")
            except Exception as e:
                print(f"❌ Unexpected error: {e}")
            
            # Ask if user wants to cancel
            if not self.ask_yes_no("Try entering position again?"):
                return None
    
    def get_rover_instructions(self, rover_number):
        """Get valid rover instructions from user"""
        while True:
            try:
                instruction_input = input(f"Enter Rover #{rover_number} instructions (L=Left, R=Right, M=Move): ").strip()
                
                if not instruction_input:
                    if rover_number == 1:
                        print("Using example instructions: LMLMLMLMM")
                        instruction_input = "LMLMLMLMM"
                    else:
                        print("❌ Instructions cannot be empty")
                        continue
                
                instruction_parser = InstructionParser()
                instructions = instruction_parser.parse_instructions(instruction_input)
                
                if not instructions:
                    print("❌ No valid instructions found")
                    continue
                
                print(f"✓ Parsed {len(instructions)} instructions")
                return instructions
                
            except Exception as e:
                print(f"❌ Error: {e}")
            
            # Ask if user wants to cancel
            if not self.ask_yes_no("Try entering instructions again?"):
                return None
    
    def show_results(self):
        """Display final results"""
        print("\n" + "=" * 50)
        print("📊 MISSION RESULTS")
        print("=" * 50)
        
        if not self.mission_control.rovers:
            print("No rovers were deployed.")
            return
        
        print(f"\nTotal rovers deployed: {len(self.mission_control.rovers)}")
        print("\nFinal positions:")
        print("-" * 20)
        
        for i, rover in enumerate(self.mission_control.rovers, 1):
            pos = rover.position
            print(f"Rover #{i}: {pos.x} {pos.y} {pos.direction.value}")
        
        # Show final visual if enabled
        if self.visual_mode:
            print("\n👁️  FINAL VISUALIZATION")
            print("-" * 25)
            self.visual_display.display_grid(self.mission_control.rovers, "Final Rover Positions")
        
        # Save option
        if self.ask_yes_no("\nSave results to file?"):
            self.save_results()
    
    def save_results(self):
        """Save results to a file"""
        try:
            filename = input("Enter filename (default: 'results.txt'): ").strip() or "results.txt"
            
            with open(filename, 'w') as f:
                f.write(f"Mars Rover Mission Results\n")
                f.write("=" * 30 + "\n")
                f.write(f"Plateau: {self.plateau.width}x{self.plateau.height}\n")
                f.write(f"Rovers deployed: {len(self.mission_control.rovers)}\n\n")
                
                for i, rover in enumerate(self.mission_control.rovers, 1):
                    pos = rover.position
                    f.write(f"Rover #{i}: {pos.x} {pos.y} {pos.direction.value}\n")
            
            print(f"✓ Results saved to {filename}")
            
        except Exception as e:
            print(f"❌ Could not save file: {e}")
    
    def ask_yes_no(self, question):
        """Ask a yes/no question, return True for yes"""
        while True:
            answer = input(f"{question} (y/n): ").strip().lower()
            if answer in ['y', 'yes']:
                return True
            elif answer in ['n', 'no']:
                return False
            else:
                print("Please answer 'y' or 'n'")

def main():
    """Entry point for terminal UI"""
    try:
        ui = TerminalUI()
        ui.run()
        
        print("\n" + "=" * 50)
        print("🎉 Mission complete! Thanks for using Mars Rover Control.")
        print("=" * 50)
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Mission aborted by user.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("Please check your input and try again.")

if __name__ == "__main__":
    main()