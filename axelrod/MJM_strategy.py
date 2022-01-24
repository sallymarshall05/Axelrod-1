from _typeshed import Self
from typing import Dict, List, Optional, Tuple
from axelrod import action
from axelrod.action import Action
from axelrod.player import Player
from axelrod.strategies.zero_determinant import LRPlayer, ZDExtortion
import warnings

C, D = Action.C, Action.D

class SJM_strategy(ZDExtortion):
    
    name = "TheMarshall"


    classifier = {
        "memory_depth": 1,  # Memory-one Four-Vector
        "stochastic": True,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def __init__(self, phi: float = 0.2, s: float = 0.1, l: float = 1) -> None:
        super().__init__(phi, s, l)

    def strategy(self, opponent: LRPlayer) -> Action:
        if not self.history:
            return C
        if (self.history % 5)==4:
           return opponent.history[-1]
        else:
            return  self





