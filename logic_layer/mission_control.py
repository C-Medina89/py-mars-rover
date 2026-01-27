class MissionControl:
    def __init__(self, plateau):
        self.plateau = plateau
        self.rovers = []
    
    def land_and_move_rover(self, position, instructions):
        # Land a new rover and process its instructions immediately , returns the final position
    
        rover = Rover(position)
        
        # Land the rover (adds to plateau with validation)
        self.plateau.add_rover(rover)
        self.rovers.append(rover)
        
        # Process instructions
        rover.process_instructions(instructions, self.plateau)
        
        return rover.position
    
    def get_all_final_positions(self):
        #Get final positions of all rovers in landing order
        return [rover.position for rover in self.rovers]