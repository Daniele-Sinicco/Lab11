from dataclasses import dataclass


@dataclass
class Prodotto:
    p_number: int
    line: str
    type: str
    product: str
    brand: str
    color: str
    u_cost: float
    u_price: float

    def __str__(self):
        return self.product

    def __hash__(self):
        return self.p_number