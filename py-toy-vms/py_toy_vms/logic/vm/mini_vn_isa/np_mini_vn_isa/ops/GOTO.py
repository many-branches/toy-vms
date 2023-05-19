from ..base import Base
from typing import List

class GOTO(Base):
    
    def GOTO(self, sr : int):
        self.control_bit = 1
        self.set_pc(self.register_file[sr])
        
    GOTO_sr_mask : int = 2**Base.register_file_addressability - 1
    GOTO_sr_lshift : int = Base.width - Base.opcode_width - Base.register_file_addressability
        
    def assemble_GOTO(self, args : List[str])->int:
        if len(args) != 1:
            raise Exception("Invalid arguments to GOTO.")
        sr = (args[0] & self.GOTO_sr_mask) << self.GOTO_sr_lshift
        return self.form_opcode("GOTO") + sr
    
    def proffer_GOTO(self, add : int)->List[int]:
        sr = ((self.GOTO_sr_mask << self.GOTO_sr_lshift) & add) >> self.GOTO_sr_lshift
        return [sr]