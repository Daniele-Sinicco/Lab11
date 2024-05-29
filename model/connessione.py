from dataclasses import dataclass

from model.products import Prodotto


@dataclass
class Connessione:
    p1: Prodotto
    p2: Prodotto

    def __str__(self):
        return f'({self.p1.p_number}, {self.p2.p_number})'
