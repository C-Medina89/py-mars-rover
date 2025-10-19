from input_layer.input_types.position import Position, CompassDirection

class PositionParser:

    def parse_position(self, position_str):
        # This function will convert string input such as '2 1 S' into a position object
        str_parts = position_str.split()
    
        if len(str_parts) != 3:
            raise ValueError("Position should have 3 parts (X, Y, Direction)")
    
        x =  int(str_parts[0])
        y =  int(str_parts[1])
        direction_char = str_parts[2]

        if direction_char == 'N':
            direction = CompassDirection.NORTH
        elif direction_char == 'S':
            direction = CompassDirection.SOUTH
        elif direction_char == 'E':
            direction = CompassDirection.EAST
        elif direction_char == 'W':
            direction = CompassDirection.WEST
        else :
            raise ValueError(f"Invalid direction: {direction_char}")
    
        return Position(x,y,direction)