import unittest
from .np_mini_vn_isa import NpMiniVnIsa
import numpy as np

class TestNpMiniVnIsa(unittest.TestCase):
    
    def test_adder_program(self):
        
        vm = NpMiniVnIsa()
        
        program = """
SET 1 1 // start at one
SET 2 2 // add two

#LOOP
ADD 1 2 1 
JUMP #LOOP
"""

        vm.load_asm(program, 20)
        vm.set_pc(20)

        for i in range(0, 100):
            print(i, vm.register_file[1])
            vm.tick()
        
        states = vm.get_states()
        print(states)
        d1 = []
        for i in range(1, len(states)):
            d1.append(
                np.subtract(states[i], states[i-1])
            )
        print(d1)