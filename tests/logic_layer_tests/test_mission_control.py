from input_layer.input_types.instructions import Instruction
from input_layer.input_types.position import Position
from input_layer.input_types.compass_directions import CompassDirection
from logic_layer.plateau import Plateau
from logic_layer.mission_control import MissionControl
import pytest

def test_mission_control_lands_and_moves_rovers():
    plateau = Plateau(5, 5)
    mission_control = MissionControl(plateau)
    
    pos1 = Position(1, 2, CompassDirection.NORTH)
    instructions1 = [Instruction.LEFT, Instruction.MOVE, Instruction.LEFT]
    
    pos2 = Position(3, 3, CompassDirection.EAST)
    instructions2 = [Instruction.MOVE, Instruction.MOVE]
    
    final1 = mission_control.land_and_move_rover(pos1, instructions1)
    final2 = mission_control.land_and_move_rover(pos2, instructions2)
    
    assert len(mission_control.get_all_final_positions()) == 2

def test_mission_control_prevents_invalid_landing():
    plateau = Plateau(5, 5)
    mission_control = MissionControl(plateau)
    
    # First rover lands at (1, 2)
    pos1 = Position(1, 2, CompassDirection.NORTH)
    mission_control.land_and_move_rover(pos1, [])
    
    # Second rover tries to land at same spot - should fail
    pos2 = Position(1, 2, CompassDirection.EAST)
    with pytest.raises(ValueError):
        mission_control.land_and_move_rover(pos2, [])