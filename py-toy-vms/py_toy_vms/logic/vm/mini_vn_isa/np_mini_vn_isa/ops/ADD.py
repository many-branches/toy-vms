from ..base import Base
from typing import List

class ADD(Base):
    
    def ADD(self, lr: int, rr: int, sr: int):
        self.register_file[sr] = self.register_file[lr] + self.register_file[rr]
        
    ADD_lr_mask : int = 2**Base.register_file_addressability - 1
    ADD_lr_lshift : int = Base.width - Base.opcode_width - Base.register_file_addressability
    ADD_rr_mask : int = 2**Base.register_file_addressability - 1
    ADD_rr_lshift : int = ADD_lr_lshift - Base.register_file_addressability
    ADD_sr_mask : int = 2 ** (Base.program_space_addressability) - 1
    ADD_sr_lshift : int = 0
        
    def assemble_ADD(self, args : List[str])->int:
        if len(args) != 3:
            raise Exception("Invalid arguments to ADD.")
        lr = (args[0] & self.ADD_lr_mask) << self.ADD_lr_lshift
        rr = (args[1] & self.ADD_rr_mask) << self.ADD_rr_lshift
        sr = (args[2] & self.ADD_sr_mask) << self.ADD_sr_lshift
        return self.form_opcode("ADD") + lr + rr + sr
    
    def proffer_ADD(self, add : int)->List[int]:
        lr = ((self.ADD_lr_mask << self.ADD_lr_lshift) & add) >> self.ADD_lr_lshift
        rr = ((self.ADD_rr_mask << self.ADD_rr_lshift) & add) >> self.ADD_rr_lshift
        sr = ((self.ADD_sr_mask << self.ADD_sr_lshift) & add) >> self.ADD_sr_lshift
        return [lr, rr, sr]