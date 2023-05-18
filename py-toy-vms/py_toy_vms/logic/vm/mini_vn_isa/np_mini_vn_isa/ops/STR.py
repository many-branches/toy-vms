from ..base import Base
from typing import List

class STR(Base):
    
    def STR(self, lr : int, sr : int):
        self.program_memory[sr] = self.register_file[lr]
        
    STR_lr_mask : int = 2**Base.register_file_addressability - 1
    STR_lr_lshift : int = Base.width - Base.opcode_width - Base.register_file_addressability
    STR_sr_mask : int = 2 ** (Base.program_space_addressability) - 1
    STR_sr_lshift : int = 0
        
    def assemble_STR(self, args : List[str])->int:
        if len(args) != 3:
            raise Exception("Invalid arguments to STR.")
        lr = (args[0] & self.STR_lr_mask) << self.STR_lr_lshift
        sr = (args[2] & self.STR_sr_mask) << self.STR_sr_lshift
        return self.form_opcode("STR") + lr + sr
    
    def proffer_STR(self, add : int)->List[int]:
        lr = ((self.STR_lr_mask << self.STR_lr_lshift) & add) >> self.STR_lr_lshift
        sr = ((self.STR_sr_mask << self.STR_sr_lshift) & add) >> self.STR_sr_lshift
        return [lr, sr]