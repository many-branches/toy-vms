from ..base import Base
from typing import List

class SUB(Base):
    
    def SUB(self, lr: int, rr: int, sr: int):
        self.register_file[sr] = self.register_file[lr] - self.register_file[rr]
        
    SUB_lr_mask : int = 2**Base.register_file_addressability - 1
    SUB_lr_lshift : int = Base.width - Base.opcode_width - Base.register_file_addressability
    SUB_rr_mask : int = 2**Base.register_file_addressability - 1
    SUB_rr_lshift : int = SUB_lr_lshift - Base.register_file_addressability
    SUB_sr_mask : int = 2 ** (Base.program_space_addressability) - 1
    SUB_sr_lshift : int = 0
        
    def assemble_SUB(self, args : List[str])->int:
        if len(args) != 3:
            raise Exception("Invalid arguments to SUB.")
        lr = (args[0] & self.SUB_lr_mask) << self.SUB_lr_lshift
        rr = (args[1] & self.SUB_rr_mask) << self.SUB_rr_lshift
        sr = (args[2] & self.SUB_sr_mask) << self.SUB_sr_lshift
        return self.form_opcode("SUB") + lr + rr + sr
    
    def proffer_SUB(self, add : int)->List[int]:
        lr = ((self.SUB_lr_mask << self.SUB_lr_lshift) & add) >> self.SUB_lr_lshift
        rr = ((self.SUB_rr_mask << self.SUB_rr_lshift) & add) >> self.SUB_rr_lshift
        sr = ((self.SUB_sr_mask << self.SUB_sr_lshift) & add) >> self.SUB_sr_lshift
        return [lr, rr, sr]