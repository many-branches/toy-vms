from ..base import Base
from typing import List

class LDR(Base):
    
    def LDR(self, lr : int, sr : int):
        self.register_file[sr] = self.program_memory[lr]
        
    LDR_lr_mask : int = 2**Base.register_file_addressability - 1
    LDR_lr_lshift : int = Base.width - Base.opcode_width - Base.register_file_addressability
    LDR_sr_mask : int = 2 ** (Base.program_space_addressability) - 1
    LDR_sr_lshift : int = 0
        
    def assemble_LDR(self, args : List[str])->int:
        if len(args) != 2:
            raise Exception("Invalid arguments to LDR.")
        lr = (args[0] & self.LDR_lr_mask) << self.LDR_lr_lshift
        sr = (args[1] & self.LDR_sr_mask) << self.LDR_sr_lshift
        return self.form_opcode("LDR") + lr + sr
    
    def proffer_LDR(self, add : int)->List[int]:
        lr = ((self.LDR_lr_mask << self.LDR_lr_lshift) & add) >> self.LDR_lr_lshift
        sr = ((self.LDR_sr_mask << self.LDR_sr_lshift) & add) >> self.LDR_sr_lshift
        return [lr, sr]