import unittest
from .np_mini_vn_isa import NpMiniVnIsa

class TestNpMiniVnIsa(unittest.TestCase):
    
    def test_adder_program(self):
        
        vm = NpMiniVnIsa()
        
        program = """
SET 1 1
SET 2 2

#LOOP
ADD 1 2 1 
JUMP #LOOP
"""

        vm.load_asm(program, 20)
        vm.set_pc(20)

        for i in range(0, 10_000):
            print(i, vm.register_file[1])
            vm.tick()
