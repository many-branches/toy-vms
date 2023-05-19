from ..mini_vn_isa import MiniVnIsa
import numpy as np
from typing import Dict, List

class Base(MiniVnIsa):
    
    width : int = 32
    opcode_width : int = 4
    register_file_addressability : int = 3
    program_space_addressability : int = 8
    control_bit : int = 0
    
    register_file : np.ndarray
    program_memory : np.ndarray
    states : np.ndarray
    
    pc_addr: int = 0
    
    def __init__(self) -> None:
        super().__init__()
        self.register_file = np.random.randint(2**self.width, size=2**self.register_file_addressability)
        self.program_memory = np.random.randint(2**self.width, size=2**self.program_space_addressability)
        self.states = np.ndarray(2**self.register_file_addressability + 2**self.program_space_addressability)
        self.control_bit = 0
        
    def record_transition(self):
        self.states = np.append(
            self.states,
            np.concatenate(
                self.register_file,
                self.program_memory
            )
        )
        
    def get_pc(self) -> int:
        return self.register_file[self.pc_addr]
    
    
    def set_pc(self, val : int) -> int:
        self.register_file[self.pc_addr] = val
        return val
        
    def get_register_file(self) -> np.ndarray:
        return self.register_file
        
    def get_program_memory(self) -> np.ndarray:
        return self.program_memory
    
    def get_states(self) -> np.ndarray:
        return self.states
    
    instruct_to_opcode : Dict[str, int] = {
        "NULL" : 0,
        "SET" : 0b0001,
        "ADD" : 0b0010,
        "SUB" : 0b0011,
        "MUL" : 0b0100,
        "DIV" : 0b0101,
        "LDR" : 0b0110,
        "STR" : 0b0111,
        "Cnzp" : 0b1000,
        "GOTO" : 0b1001,
        "Bnzp" : 0b1010,
        "JUMP" : 0b1100
    }
    
    opcode_to_instruct : Dict[int, str] = {
        v:k  for k,v in instruct_to_opcode.items()
    }
    
    def form_opcode(self, instruct : str)->int:
        opcode = self.instruct_to_opcode.get(instruct, 0)
        return opcode << (self.width - self.opcode_width)
    
    def get_instruction_name(self, instruct : int)->str:
        opcode = (instruct >> (self.width - self.opcode_width)) & ((2**4) - 1)
        return self.opcode_to_instruct.get(opcode, "NULL")
    
    def nzp(self, nzp : int, val : int)->int:
        
        n = True
        z = True
        p = True
        
        n_mask = nzp & 0b100
        z_mask = nzp & 0b010
        p_mask = nzp & 0b001
        
        if n_mask > 0:
            n = val < 0
            
        if z_mask > 0:
            z = val == 0
            
        if p_mask > 0:
            p = val > 0
            
        return int(n and z and p)
    
    def compute(self, instr : int):
        opcode_name = self.get_instruction_name(instr)
        operation = getattr(self, opcode_name)
        profferer = getattr(self, f"proffer_{opcode_name}")
        operation(*profferer(instr))
    
    def tick(self):
        pc = self.get_pc()
        instruction = self.program_memory[pc]
        self.compute(instruction)
        if self.control_bit > 0:
            self.control_bit = 0
        else:
            self.set_pc(pc + 1)
        
    
    def NULL(self, *args):
        pass
        
    def assemble_NULL(self, args : List[str])->int:
        return 0
    
    def proffer_NULL(self, add : int)->List[int]:
        return []