from ..base import Base
from typing import List

class SET(Base):
    
    def SET(self, sr: int, val: int):
        self.register_file[sr] = val
        
    SET_sr_mask : int = 2**Base.register_file_addressability - 1
    SET_sr_lshift : int = Base.width - Base.opcode_width - Base.register_file_addressability
    SET_val_mask : int = 2 ** (Base.program_space_addressability) - 1
    SET_val_lshift : int = 0
        
    def assemble_SET(self, args : List[str])->int:
        if len(args) != 2:
            raise Exception("Invalid arguments to SET.")
        sr = (args[0] & self.SET_sr_mask) << self.SET_sr_lshift
        val = (args[1] & self.SET_val_mask) << self.SET_val_lshift
        return self.form_opcode("SET") + sr + val
    
    def proffer_SET(self, add : int)->List[int]:
        sr = ((self.SET_sr_mask << self.SET_sr_lshift) & add) >> self.SET_sr_lshift
        val = ((self.SET_val_mask << self.SET_val_lshift) & add) >> self.SET_val_lshift
        return [sr, val]