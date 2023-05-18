from ..vm import Vm

# an ISA feature basic arithmetic and control flow instructions
# Vn for von Neumann
class MiniVnIsa(Vm):
    
    def get_pc(self)->int:
        pass
    
    def set_pc(self, val : int)->int:
        pass
    
    def NULL(self, *args):
        pass
    
    def SET(self, sr : int, val : int):
        pass
    
    def ADD(self, lr : int, rr : int, sr : int):
        pass
    
    def SUB(self, lr : int, rr : int, sr : int):
        pass

    def MUL(self, lr : int, rr : int, sr : int):
        pass
    
    def DIV(self, lr : int, rr : int, sr : int):
        pass
    
    def LDR(self, lr : int, sr : int):
        pass
    
    def STR(self, lr : int, sr : int):
        pass
    
    def Cnzp(self, lr : int, rr : int, nzp : int, sr : int):
        pass
    
    def GOTO(self, pc : int):
        pass
    
    def Bnzp(self, lr : int, rr : int, nzp : int, goto : int):
        pass
    
    def assemble(self, asm_line : str)->int:
        pass
    
    def disassemble(self, instr : int)->str:
        pass
    
    def compute(self, instr : int):
        pass