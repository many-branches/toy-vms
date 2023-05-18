from ..mini_vn_isa import MiniVnIsa
import numpy as np
from typing import Dict, List
import math

class NpMiniVnIs(MiniVnIsa):
    
    width : int = 32
    opcode_width : int = 4
    register_file_size : int = 8
    program_space_addressability : int = 8
    
    register_file : np.ndarray
    program_memory : np.ndarray
    states : np.ndarray
    
    def __init__(self) -> None:
        super().__init__()
        self.register_file = np.random.randint(2**self.width, size=self.register_file_size)
        self.program_memory = np.random.randint(2**self.width, size=2**self.program_space_addressability)
        self.states = np.ndarray(2**self.width, self.register_file_size + 2**self.program_space_addressability)
        
    def record_transition(self):
        self.states = np.append(
            self.states,
            np.concatenate(
                self.register_file,
                self.program_memory
            )
        )
        
    def get_register_file(self) -> np.ndarray:
        return self.register_file
        
    def get_program_memory(self) -> np.ndarray:
        return self.program_memory
    
    def get_states(self) -> np.ndarray:
        return self.states
    
    instruct_to_opcode : Dict[int, int] = {
        "SET" : 0b0001,
        "ADD" : 0b0010,
        "SUB" : 0b0011,
        "MUL" : 0b0100,
        "DIV" : 0b0101,
        "LDR" : 0b0110,
        "STR" : 0b0111,
        "Cnzp" : 0b1000,
        "GOTO" : 0b1001,
        "Bnzp" : 0b1010
    }
    
    def SET(self, sr: int, val: int):
        self.register_file[sr] = val
        
    SET_sr_mask : int = 2 ** (program_space_addressability) - 1
    SET_sr_lshift : int = width - opcode_width
    SET_val_mask : int = width - opcode_width - program_space_addressability
    SET_val_lshift : int = 0
    
    def assemble_SET(self, args : List[str])->int:
        if len(args) != 2:
            raise Exception("Invalid arguments to SET.")
        sr = args[0] & self.SET_sr_mask << self.SET_sr_lshift
        val = args[1] & (self.SET_val_mask) << self.SET_val_lshift
        return self.instruct_to_opcode["SET"] + sr + val
    
    def ADD(self, lr: int, rr: int, sr: int):
        self.register_file[sr] = self.register_file[lr] + self.register_file[rr]
        
    ADD_lr_mask : int = register_file_size - 1
    ADD_lr_lshift : int = width - register_file_size
    ADD_rr_mask : int = register_file_size - 1
    ADD_rr_lshift : int = width - (register_file_size * 2)
    ADD_sr_mask : int = 2 ** (program_space_addressability) - 1
    ADD_sr_lshift : int = 0
        
    def assemble_ADD(self, args : List[str])->int:
        if len(args) != 3:
            raise Exception("Invalid arguments to ADD.")
        lr = args[0] & self.ADD_lr_mask << self.ADD_lr_lshift
        rr = args[1] & self.ADD_rr_mask << self.ADD_rr_lshift
        sr = args[2] & self.ADD_sr_mask << self.ADD_sr_lshift
        return self.instruct_to_opcode["ADD"] + lr + rr + sr
        
    def SUB(self, lr: int, rr: int, sr: int):
        self.register_file[sr] = self.register_file[lr] + self.register_file[rr]
        
    def MUL(self, lr: int, rr: int, sr: int):
        self.register_file[sr] = self.register_file[lr] * self.register_file[rr]
        
    def DIV(self, lr: int, rr: int, sr: int):
        self.register_file[sr] = self.register_file[lr] // self.register_file[rr]
        
    def LDR(self, lr : int, sr : int):
        self.register_file[sr] = self.program_memory[lr]
    
    def STR(self, lr : int, sr : int):
        
        self.program_memory[sr] = self.register_file[lr]
        
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
        
        
    def Cnzp(self, lr: int, rr: int, nzp: int, sr: int):
        self.register_file[sr] = self.nzp(
            nzp,
            lr - rr
        )
        
    def GOTO(self, pc: int):
        return self.set_pc(pc)
    
    def Bnzp(self, lr: int, rr: int, nzp: int, goto: int):
        if self.nzp(
            nzp,
            lr - rr
        ) > 0:
            self.set_pc(goto)
        else: self.set_pc(self.get_pc() + 1)
        
    def assemble(self, asm_line : str)->int:
        split = asm_line.split()
        
    
    def disassemble(self, instr : int)->str:
        pass
    