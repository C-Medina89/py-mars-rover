from input_layer.input_types.plateau_size import PlateauSize

class PlateauParser:

    def parse_plateau(self, plateau_str):
        # This function converts a string such as "6 6" into a plateau size object
        str_parts = plateau_str.split()

        if len(str_parts) != 2:
            raise ValueError("Plateau size should have 2 parts: max_x max_y")
    
        max_x = int(str_parts[0])
        max_y = int(str_parts[1])
    
        return PlateauSize(max_x, max_y)