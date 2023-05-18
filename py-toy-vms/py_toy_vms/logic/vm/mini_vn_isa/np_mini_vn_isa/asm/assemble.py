from ..base import Base
from typing import Dict, Optional

class Assembler(Base):

    def assemble(self, asm_line: str) -> int:

        spl = asm_line.strip().split()
        if len(spl) < 1:
            raise Exception("Empty line not ignored.")
        
        opcode_name = spl[0]
        args = spl[1:]
        assmbl = getattr(self, f"assemble_{opcode_name}")
        return assmbl([int(arg) for arg in args])
    
    def handle_label_line(self, line : str, line_count : int, labels : Dict[str, int])->Optional[str]:
    
        terms = line.split()
        line = terms[0]
        
        if line.find("=") > 0:
            spl = line.split("=")
            name = spl[0][1:]
            val = int(spl[1])
            labels[name] = val
            return None
        
        name = line[1:]
        labels[name] = line_count
        return None
        
    
    def handle_line(self, line : str, line_count : int, labels : Dict[str, int])->Optional[str]:
        
        line = line.strip()
        if len(line) < 1:
            return None
        if line.startswith("//"):
            return None
        if line.startswith("#"):
            return self.handle_label_line(line, line_count, labels)
        
        line_terms = []
        for val in line.split():
            if val.startswith("#"):
                label_value = labels.get(val[1:], None)
                if label_value is None:
                    raise Exception(f"Reference to unitialized label: {val}")
                line_terms.append(str(label_value))
            else:
                line_terms.append(val)
        
        return " ".join(line_terms)
        
    def load_asm(self, asm: str, address: int):
        
        asm = asm.strip()
        lines = []
        labels : Dict[str, int] = {}
        for line in asm.splitlines():
            asm_line = self.handle_line(line, address + len(lines), labels)
            if asm_line is None:
                continue
            print(line, asm_line)
            lines.append(self.assemble(asm_line))
        
        for i, line in enumerate(lines):
            self.program_memory[address + i] = line
            
                
                    
        