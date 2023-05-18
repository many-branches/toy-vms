from ..base import Base
from typing import List

class Cnzp(Base):
    
    def Cnzp(self, lr: int, rr: int, nzp: int, sr: int):
        self.register_file[sr] = self.nzp(
            nzp,
            self.register_file[lr] - self.register_file[rr]
        )
        
    Cnzp_lr_mask : int = 2**Base.register_file_addressability - 1
    Cnzp_lr_lshift : int = Base.width - Base.opcode_width - Base.register_file_addressability
    Cnzp_rr_mask : int = 2**Base.register_file_addressability - 1
    Cnzp_rr_lshift : int = Cnzp_lr_lshift - Base.register_file_addressability
    Cnzp_nzp_mask : int = 2**3 - 1
    Cnzp_nzp_lshift : int = Cnzp_rr_lshift - Base.register_file_addressability
    Cnzp_sr_mask : int = 2 ** (Base.program_space_addressability) - 1
    Cnzp_sr_lshift : int = 0
        
    def assemble_Cnzp(self, args : List[str])->int:
        if len(args) != 3:
            raise Exception("Invalid arguments to Cnzp.")
        lr = (args[0] & self.Cnzp_lr_mask) << self.Cnzp_lr_lshift
        rr = (args[1] & self.Cnzp_rr_mask) << self.Cnzp_rr_lshift
        sr = (args[2] & self.Cnzp_sr_mask) << self.Cnzp_sr_lshift
        return self.form_opcode("Cnzp") + lr + rr + sr
    
    def proffer_Cnzp(self, add : int)->List[int]:
        lr = ((self.Cnzp_lr_mask << self.Cnzp_lr_lshift) & add) >> self.Cnzp_lr_lshift
        rr = ((self.Cnzp_rr_mask << self.Cnzp_rr_lshift) & add) >> self.Cnzp_rr_lshift
        nzp = ((self.Cnzp_nzp_mask << self.Cnzp_rr_lshift) & add) >> self.Cnzp_nzp_lshift
        sr = ((self.Cnzp_sr_mask << self.Cnzp_sr_lshift) & add) >> self.Cnzp_sr_lshift
        return [lr, rr, nzp, sr]