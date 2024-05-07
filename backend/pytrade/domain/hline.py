from typing import List

from pytrade.domain.pivot_point import PivotPoint, prices


class HLine:
    def __init__(self,price:float,pivots:List[PivotPoint]):
        self.price = price
        self.pivots = pivots

    def __repr__(self):
        return f"{self.price}"

    def __str__(self):
        return f"{self.price}"

    def is_support(self,price:float) -> bool:
        return price > self.price

    def is_resistance(self, price: float) -> bool:
        return price < self.price

    def contain(self,price:float,tolorance:float) -> bool:
        return price<self.price + tolorance and price >= self.price-tolorance

    def exmine_points(self,points :List[PivotPoint], tolorance:float):
        for x in points:
            if self.contain(x.price,tolorance):
                self.pivots.append(x)
    def total_pivot_count(self)->int:
        return len(self.pivots)

def compute_hline(points:List[PivotPoint], tolorance:float) -> List[HLine]:
    result = []

    # find    the    min    pivot    point
    min_p = min(prices(points))
    # find the max pivot point
    max_p = max(prices(points))

    step = (max_p - min_p) / 100
    tolorance = step * 3

    print("min_p %f, max_p:%f, tolorance %f \n", min_p, max_p, tolorance)
    x = max_p+tolorance
    while(x < max_p+tolorance):

        line  = HLine(x)
        line.exmine_points(points, tolorance)
        if line.total_pivot_count() > 2:
            print("line @ %f\n", x)
            result.append(line)
        x = x + (2 * tolorance)

    return result