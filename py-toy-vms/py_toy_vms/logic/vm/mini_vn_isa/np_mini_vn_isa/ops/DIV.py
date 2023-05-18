from ..base import Base
from typing import List

class DIV(Base):
    
    def DIV(self, lr: int, rr: int, sr: int):
        self.register_file[sr] = self.register_file[lr] // self.register_file[rr]
        
    DIV_lr_mask : int = 2**Base.register_file_addressability - 1
    DIV_lr_lshift : int = Base.width - Base.opcode_width - Base.register_file_addressability
    DIV_rr_mask : int = 2**Base.register_file_addressability - 1
    DIV_rr_lshift : int = DIV_lr_lshift - Base.register_file_addressability
    DIV_sr_mask : int = 2 ** (Base.program_space_addressability) - 1
    DIV_sr_lshift : int = 0
        
    def assemble_DIV(self, args : List[str])->int:
        if len(args) != 3:
            raise Exception("Invalid arguments to DIV.")
        lr = (args[0] & self.DIV_lr_mask) << self.DIV_lr_lshift
        rr = (args[1] & self.DIV_rr_mask) << self.DIV_rr_lshift
        sr = (args[2] & self.DIV_sr_mask) << self.DIV_sr_lshift
        return self.form_opcode("DIV") + lr + rr + sr
    
    def proffer_DIV(self, add : int)->List[int]:
        lr = ((self.DIV_lr_mask << self.DIV_lr_lshift) & add) >> self.DIV_lr_lshift
        rr = ((self.DIV_rr_mask << self.DIV_rr_lshift) & add) >> self.DIV_rr_lshift
        sr = ((self.DIV_sr_mask << self.DIV_sr_lshift) & add) >> self.DIV_sr_lshift
        return [lr, rr, sr]