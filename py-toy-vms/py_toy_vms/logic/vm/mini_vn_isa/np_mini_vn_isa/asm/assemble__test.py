import unittest
from .assemble import Assembler

class TestAssemble(unittest.TestCase):
    
    def test_loads(self):
        
        asmblr = Assembler()
        
        program = """
NULL 123 456

#START
NULL 567 321

NULL #START 456

#BIG_NUM=12234
NULL #BIG_NUM
"""

        asmblr.load_asm(program, 20)