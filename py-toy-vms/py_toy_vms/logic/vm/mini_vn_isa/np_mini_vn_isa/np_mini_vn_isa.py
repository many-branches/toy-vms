from ..mini_vn_isa import MiniVnIsa
import numpy as np
from typing import Dict, List
from .base import Base
from .ops import ADD, SUB, MUL, DIV, SET, GOTO, LDR, STR, Bnzp, Cnzp, JUMP
from .asm import Assembler

class NpMiniVnIsa(
    ADD,
    SUB,
    MUL,
    DIV,
    SET,
    GOTO, 
    LDR,
    STR,
    Bnzp, 
    Cnzp,
    JUMP,
    Assembler,
    Base
):
    
    def __init__(self) -> None:
        super().__init__()