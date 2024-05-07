from typing import List


class PivotPoint:
    def __init__(self,x,p:float):
        self.X = x
        self.price:float = p
        self.support:bool = False
        self.degree:int = 1

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self,other):
        return self.price <= other.price


def prices(self,points:List[PivotPoint]) -> List[float]:
        return [x.price for x in points]

def first_degree(self,points:List[PivotPoint]) -> List[PivotPoint]:
    return [x for x in points if x.degree == 1]

def second_degree(self,points:List[PivotPoint]) -> List[PivotPoint]:
    return [x for x in points if x.degree == 2]

def third_degree(self,points:List[PivotPoint]) -> List[PivotPoint]:
    return [x for x in points if x.degree == 3]