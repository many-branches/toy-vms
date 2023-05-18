import unittest
from .ADD import ADD

class TestADD(unittest.TestCase):
    
    def test_add_assemble_and_proffer(self):
        
        add_vm = ADD()
        syllables = [2, 7, 40]
        asm = add_vm.assemble_ADD(syllables)
        self.assertEqual(asm, 0b100101110000000000000000101000)
        args = add_vm.proffer_ADD(asm)
        self.assertEqual(args, syllables)
    