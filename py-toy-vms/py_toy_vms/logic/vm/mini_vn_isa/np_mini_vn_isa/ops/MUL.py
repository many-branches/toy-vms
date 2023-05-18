from ..base import Base
from typing import List

class MUL(Base):
    
    def MUL(self, lr: int, rr: int, sr: int):
        self.register_file[sr] = self.register_file[lr] * self.register_file[rr]
        
    MUL_lr_mask : int = 2**Base.register_file_addressability - 1
    MUL_lr_lshift : int = Base.width - Base.opcode_width - Base.register_file_addressability
    MUL_rr_mask : int = 2**Base.register_file_addressability - 1
    MUL_rr_lshift : int = MUL_lr_lshift - Base.register_file_addressability
    MUL_sr_mask : int = 2 ** (Base.program_space_addressability) - 1
    MUL_sr_lshift : int = 0
        
    def assemble_MUL(self, args : List[str])->int:
        if len(args) != 3:
            raise Exception("Invalid arguments to MUL.")
        lr = (args[0] & self.MUL_lr_mask) << self.MUL_lr_lshift
        rr = (args[1] & self.MUL_rr_mask) << self.MUL_rr_lshift
        sr = (args[2] & self.MUL_sr_mask) << self.MUL_sr_lshift
        return self.form_opcode("MUL") + lr + rr + sr
    
    def proffer_MUL(self, add : int)->List[int]:
        lr = ((self.MUL_lr_mask << self.MUL_lr_lshift) & add) >> self.MUL_lr_lshift
        rr = ((self.MUL_rr_mask << self.MUL_rr_lshift) & add) >> self.MUL_rr_lshift
        sr = ((self.MUL_sr_mask << self.MUL_sr_lshift) & add) >> self.MUL_sr_lshift
        return [lr, rr, sr]