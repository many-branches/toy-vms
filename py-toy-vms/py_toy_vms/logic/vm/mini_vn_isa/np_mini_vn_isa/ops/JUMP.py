from ..base import Base
from typing import List

class JUMP(Base):
    
    def JUMP(self, val : int):
        self.control_bit = 1
        self.set_pc(val)
        
    JUMP_val_mask : int = 2**Base.program_space_addressability - 1
    JUMP_val_lshift : int = Base.width - Base.opcode_width - Base.program_space_addressability
        
    def assemble_JUMP(self, args : List[str])->int:
        if len(args) != 1:
            raise Exception("Invalid arguments to JUMP.")
        val = (args[0] & self.JUMP_val_mask) << self.JUMP_val_lshift
        return self.form_opcode("JUMP") + val
    
    def proffer_JUMP(self, add : int)->List[int]:
        val = ((self.JUMP_val_mask << self.JUMP_val_lshift) & add) >> self.JUMP_val_lshift
        return [val]