from input_layer.input_types.instructions import Instruction  


class InstructionParser:
     
    def parse_instructions(self, instruction_str):
    # This function will convert a string input such as "MLRLRM" to a list of instructions
        instructions_list = []

        for char in instruction_str.upper():
            if char == 'R':
                instructions_list.append(Instruction.RIGHT)
            elif char == 'L':
                instructions_list.append(Instruction.LEFT)
            elif char == 'M':
                instructions_list.append(Instruction.MOVE)
        

        return instructions_list

