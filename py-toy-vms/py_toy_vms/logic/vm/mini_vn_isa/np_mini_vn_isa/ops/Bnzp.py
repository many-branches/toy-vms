from ..base import Base
from typing import List

class Bnzp(Base):
    
    def Bnzp(self, lr: int, rr: int, nzp: int, goto: int):
        if self.nzp(
            nzp,
            self.register_file[lr] - self.register_file[rr]
        ) > 0:
            self.set_pc(goto)
        
    Bnzp_lr_mask : int = 2**Base.register_file_addressability - 1
    Bnzp_lr_lshift : int = Base.width - Base.opcode_width - Base.register_file_addressability
    Bnzp_rr_mask : int = 2**Base.register_file_addressability - 1
    Bnzp_rr_lshift : int = Bnzp_lr_lshift - Base.register_file_addressability
    Bnzp_nzp_mask : int = 2**3 - 1
    Bnzp_nzp_lshift : int = Bnzp_rr_lshift - Base.register_file_addressability
    Bnzp_sr_mask : int = 2 ** (Base.program_space_addressability) - 1
    Bnzp_sr_lshift : int = 0
        
    def assemble_Bnzp(self, args : List[str])->int:
        if len(args) != 4:
            raise Exception("Invalid arguments to Bnzp.")
        lr = (args[0] & self.Bnzp_lr_mask) << self.Bnzp_lr_lshift
        rr = (args[1] & self.Bnzp_rr_mask) << self.Bnzp_rr_lshift
        sr = (args[2] & self.Bnzp_sr_mask) << self.Bnzp_sr_lshift
        return self.form_opcode("Bnzp") + lr + rr + sr
    
    def proffer_Bnzp(self, add : int)->List[int]:
        lr = ((self.Bnzp_lr_mask << self.Bnzp_lr_lshift) & add) >> self.Bnzp_lr_lshift
        rr = ((self.Bnzp_rr_mask << self.Bnzp_rr_lshift) & add) >> self.Bnzp_rr_lshift
        nzp = ((self.Bnzp_nzp_mask << self.Bnzp_rr_lshift) & add) >> self.Bnzp_nzp_lshift
        sr = ((self.Bnzp_sr_mask << self.Bnzp_sr_lshift) & add) >> self.Bnzp_sr_lshift
        return [lr, rr, nzp, sr]