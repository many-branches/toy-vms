from typing import Protocol
import numpy as np

class Vm(Protocol):
    
    def load_asm(self, asm : str, address : int):
        pass
    
    def tick(self):
        pass
    
    def get_register_file(self)->np.ndarray:
        pass
    
    def get_program_memory(self)->np.ndarray:
        pass
    
    def get_states(self)->np.ndarray:
        pass