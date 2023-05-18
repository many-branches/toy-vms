from ..base import Base
from typing import List

class SET(Base):
    
    def SET(self, sr: int, val: int):
        self.register_file[sr] = val
        
    SET_lr_mask : int = 2**Base.register_file_addressability - 1
    SET_lr_lshift : int = Base.width - Base.opcode_width - Base.register_file_addressability
    SET_val_mask : int = 2 ** (Base.program_space_addressability) - 1
    SET_val_lshift : int = 0
        
    def assemble_SET(self, args : List[str])->int:
        if len(args) != 3:
            raise Exception("Invalid arguments to SET.")
        lr = (args[0] & self.SET_lr_mask) << self.SET_lr_lshift
        sr = (args[2] & self.SET_val_mask) << self.SET_val_lshift
        return self.form_opcode("SET") + lr + sr
    
    def proffer_SET(self, add : int)->List[int]:
        lr = ((self.SET_lr_mask << self.SET_lr_lshift) & add) >> self.SET_lr_lshift
        sr = ((self.SET_val_mask << self.SET_val_lshift) & add) >> self.SET_val_lshift
        return [lr, sr]